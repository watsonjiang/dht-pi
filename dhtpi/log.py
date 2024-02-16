import logging
import sys
from logging.handlers import TimedRotatingFileHandler

LOGGER = logging.getLogger("dhtpi.app")


def init_logging(log_to_console=False):
    handlers = [TimedRotatingFileHandler('pi.log', when='D', backupCount=5)]
    if log_to_console:
        handlers.append(logging.StreamHandler(stream=sys.stdout))
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                        handlers=handlers)
