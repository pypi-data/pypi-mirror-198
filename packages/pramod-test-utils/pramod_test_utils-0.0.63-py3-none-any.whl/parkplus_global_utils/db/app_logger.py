import logging


class AppLogger:
    def __init__(self, logger_type="primary", tag=None):
        self.logger = logging.getLogger(logger_type)
        self.tag = tag

    def info(self, message, tag=None, extra=None):
        if self.tag:
            self.logger.info(f"[{self.tag}] {message}", extra=extra)
        else:
            self.logger.info(message, extra=extra)

    def error(self, message, tag=None):
        if self.tag:

            self.logger.error(f"[{self.tag}] {message}")
        else:
            self.logger.error(message)

    def debug(self, message, tag=None):
        if self.tag:
            self.logger.debug(f"[{self.tag}] {message}")
        else:
            self.logger.debug(message)
