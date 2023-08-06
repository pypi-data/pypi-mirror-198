import asyncio
from typing import Any, Type

from rich.console import RenderableType
from rich.text import Text
from textual.app import App, ComposeResult, CSSPathType
from textual.binding import Binding
from textual.containers import Container, Horizontal
from textual.driver import Driver
from textual.keys import Keys
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import DataTable, Footer, Input, Label, Static, Switch, Tree

from kayak import logger
from kayak.ksql.ksql_service import KsqlService
from kayak.styles.colors import DESIGN, GREEN
from kayak.widgets.header import Header


class Status(Widget):
    active = reactive(False)

    def render(self) -> RenderableType:
        return (
            Text.from_markup(f"STATUS: [{GREEN}]ACTIVE[/]")
            if self.active
            else Text.from_markup("STATUS: IDLE")
        )


class Settings(Container):
    earliest = True

    def on_switch_changed(self, event: Switch.Changed) -> None:
        self.earliest = event.value

    def compose(self) -> ComposeResult:
        yield Label("Settings", classes="title")
        yield Horizontal(
            Static("earliest:     ", classes="label"), Switch(value=self.earliest)
        )


class Tui(App[None]):
    CSS_PATH = "tui.css"
    BINDINGS = [
        Binding(Keys.ControlC, "quit", "QUIT"),
        Binding(Keys.F1, "push_screen('help')", "HELP"),
        Binding(Keys.ControlX, "kill_query", "KILL QUERY"),
        Binding(Keys.ControlS, "toggle_settings", "TOGGLE SETTINGS"),
    ]

    active = reactive(False)
    query_id: str | None = None

    def __init__(
        self,
        server: str,
        user: str | None,
        password: str | None,
        driver_class: Type[Driver] | None = None,
        css_path: CSSPathType | None = None,
        watch_css: bool = False,
    ):
        super().__init__(driver_class, css_path, watch_css)
        self.ksql_service = KsqlService(server, user, password)
        self.server = self.ksql_service.info()
        self.topics = self.ksql_service.topics()
        self.streams = self.ksql_service.streams()

    def on_mount(self) -> None:
        input_query = self.query_one(Input)
        input_query.placeholder = "QUERY"
        input_query.focus()

        header = self.query_one(Header)
        header.server = self.server

        tree = self.query_one(Tree)
        tree.show_root = False
        tree.root.expand()
        tree.cursor_line = -1

        stream_node = tree.root.add("STREAMS", expand=True)
        for stream in self.streams:
            stream_node.add_leaf(stream.name)

        topic_node = tree.root.add("TOPICS", expand=True)
        for topic in self.topics:
            topic_node.add_leaf(topic.name)

        table = self.query_one(DataTable)
        table.cursor_type = "row"

        self.design = DESIGN
        self.refresh_css()

    async def action_kill_query(self) -> None:
        logger.debug("Killing query %s", self.query_id)
        if self.query_id:
            self.ksql_service.close_query(self.query_id)

    async def action_toggle_settings(self) -> None:
        input = self.query_one(Input)

        settings = self.query_one(Settings)
        switch = settings.query_one(Switch)

        if switch.has_focus:
            input.focus()
        else:
            switch.focus()

    def watch_active(self, active: bool) -> None:
        status = self.query_one(Status)
        status.active = active

    async def on_input_submitted(self, message: Input.Submitted) -> None:
        if not message.value:
            return

        await self.action_kill_query()

        settings = self.query_one(Settings)

        table = self.query_one(DataTable)
        table.focus()
        table.clear(columns=True)

        def on_close() -> None:
            self.active = False
            self.query_id = None

        def on_init(data: dict[str, str]) -> None:
            self.active = True
            self.query_id = data["queryId"]
            for column in data["columnNames"]:
                table.add_column(column)

        def on_new_row(row: list[Any]) -> None:
            table.add_row(*row)
            table.scroll_end()

        asyncio.create_task(
            self.ksql_service.query(
                query=message.value,
                earliest=settings.earliest,
                on_init=on_init,
                on_new_row=on_new_row,
                on_close=on_close,
            )
        )

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Settings(classes="-hidden")
        yield Tree("")
        with Container():
            yield Input()
            yield DataTable()
            yield Status()
