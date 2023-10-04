# debug
# info
# warning
# error
# critical
# format : 2023-08-05 01:35:50, 798: ERROR: <Testcasename>: a major error happening cannot continue
import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)
    filehandler = logging.FileHandler('logfile.log')
    logger.addHandler(filehandler)  # filehandler object
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    filehandler.setFormatter(formatter)  # to connect filehandling and formatter

    logger.setLevel(logging.INFO)
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("Something is in warning mode")
    logger.error("A major error has happened")
    logger.critical("critical issue")
