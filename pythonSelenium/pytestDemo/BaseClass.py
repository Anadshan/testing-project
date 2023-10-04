import logging


class BaseClass:
    def getLogger(self):
        logger = logging.getLogger(__name__)
        filehandler = logging.FileHandler('logfile.log')
        logger.addHandler(filehandler)  # filehandler object
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler.setFormatter(formatter)  # to connect filehandling and formatter

        logger.setLevel(logging.INFO)
        return logger
