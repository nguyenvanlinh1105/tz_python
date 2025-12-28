import logging
import sys


class ColoredFormatter(logging.Formatter):
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format_str = "%(levelname)s: [%(asctime)s] - %(message)s"

    FORMATS = {
        logging.DEBUG: grey + format_str + reset,
        logging.INFO: "\x1b[32;20m" + format_str + reset,  # Green
        logging.WARNING: yellow + format_str + reset,
        logging.ERROR: red + format_str + reset,
        logging.CRITICAL: bold_red + format_str + reset,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def setup_logging():
    logger = logging.getLogger("app")
    logger.setLevel(logging.INFO)

    handler = sys.stdout
    console_handler = logging.StreamHandler(handler)
    console_handler.setFormatter(ColoredFormatter())

    logger.addHandler(console_handler)
    return logger


logger = setup_logging()
