from loguru import logger
from pathlib import Path


LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logger.remove()

logger.add(
    LOG_DIR / "angrybird.log",
    rotation="10 MB",
    retention="10 days",
    level="DEBUG",
)

logger.add(
    sink=lambda msg: print(msg, end=""),
    level="INFO",
)


def get_logger():
    return logger