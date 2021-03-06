import logging
import os

from data.constants import LOG_LEVEL, LOGGING_FILE, VERSION


def clear_log(log_file: str) -> None:
    if os.path.isfile(log_file):
        f = open(log_file, 'r+')
        f.truncate(0)
    else:
        make_log(log_file)


def make_log(log_file: str) -> None:
    basedir = os.path.dirname(log_file)
    if not os.path.exists(basedir):
        os.makedirs(basedir)
    open(log_file, 'a').close()


def initialize_logging() -> None:
    log_file = LOGGING_FILE
    clear_log(log_file)

    fmt = '%(asctime)s {} [%(levelname)s]  %(message)s'.format(VERSION)
    formatter = logging.Formatter(fmt)
    logger = logging.getLogger()
    logger.setLevel(LOG_LEVEL)

    # file_logger = logging.FileHandler(log_file)
    # file_logger.setFormatter(formatter)
    # logger.addHandler(file_logger)

    console_logger = logging.StreamHandler()
    console_logger.setFormatter(formatter)
    logger.addHandler(console_logger)
