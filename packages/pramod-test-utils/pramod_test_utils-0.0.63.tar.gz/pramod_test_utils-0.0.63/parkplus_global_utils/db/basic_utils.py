from .app_logger import AppLogger


class BasicUtils:
    logger = AppLogger()

    def __init__(self, *args, **kwargs):
        self.init_logger()

    def init_logger(self):
        tag = self.__class__.__name__
        self.logger = AppLogger(tag=tag)
