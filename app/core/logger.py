import sys
from loguru import logger

logger.remove()

logger.add(
    sys.stdout,
    level="INFO",
    colorize=True,
)

logger.add(
    "logs/application.log",
    rotation="5 MB",
    retention=10,
)
