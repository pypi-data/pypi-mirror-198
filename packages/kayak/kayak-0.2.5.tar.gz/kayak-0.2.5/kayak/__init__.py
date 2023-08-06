import logging
from pathlib import Path

__version__ = VERSION = "0.2.5"
NAME = "kayak"


def get_home() -> Path:
    user_home = Path.home()
    app_home = user_home.joinpath("." + NAME)
    if not app_home.exists():
        app_home.mkdir()
    return app_home


LOG = get_home().joinpath(NAME + ".log")

logger_handler = logging.FileHandler(LOG)
logger_handler.setFormatter(
    logging.Formatter("%(asctime)-15s %(levelname)-8s %(message)s")
)

logger = logging.getLogger()
logger.addHandler(logger_handler)
logger.setLevel(logging.INFO)
