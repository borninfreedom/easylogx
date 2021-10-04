from typing import Any, Union
import logging

# CRITICAL = 50
# FATAL = CRITICAL
# ERROR = 40
# WARNING = 30
# WARN = WARNING
# INFO = 20
# DEBUG = 10
# NOTSET = 0


MODE = Union['w', 'a']


class EasyLog:
    def __init__(self, logger_name: str = __name__, log_level: int = logging.DEBUG) -> None:
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(log_level)
        self.log_level = log_level
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)

        self.logger.addHandler(console_handler)

    def add_filehandler(self, filename: str = 'default.log', mode: MODE = 'w'):
        file_handler = logging.FileHandler(filename, mode)
        file_handler.setLevel(self.log_level)
        self.logger.addHandler(file_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

    def warn(self, message):
        self.logger.warning(message)

    def critical(self, message):
        self.logger.critical(message)


if __name__ == '__main__':
    logger = EasyLog()
    logger.logger.debug('nihao')
    n = 3
    logger.debug(f'nihao={n}')
    logger.info(f'nihao={n}')

    logger.add_filehandler()
    logger.debug(f'nnnn={n}')
