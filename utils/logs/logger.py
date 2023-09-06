# Dreams without Goals are just Dreams
#
# - @lucaimbalzano


import logging
from logging.handlers import TimedRotatingFileHandler
from selenium.webdriver.remote.remote_connection import LOGGER as seleniumLogger
from urllib3.connectionpool import log as urllibLogger
import datetime
import re

class WebDriverFilter(logging.Filter):
    def filter(self, record):
        # Ignore log messages that contain "WebDriver" or other patterns
        return "WebDriver" not in record.msg and not re.match(r"POST http://.*session", record.msg)

def selenium_logger_setup():
    # Set the threshold for selenium to WARNING
    seleniumLogger.setLevel(logging.WARNING)
    # Set the threshold for urllib3 to WARNING
    urllibLogger.setLevel(logging.WARNING)

def setup_logger():

    # Create a logger
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    logger.propagate = False
    
    # Create a TimedRotatingFileHandler and set the logging level
    current_time = datetime.datetime.now()
    time =  f"{current_time.year}-{current_time.month:02d}-{current_time.day:02d}_{current_time.hour:02d}-{current_time.minute:02d}-{current_time.second:02d}"
    path_logger = './utils/logs/'
    file_handler = TimedRotatingFileHandler(path_logger+time+'_logger.log', when="midnight", interval=7, backupCount=10)
    file_handler.setLevel(logging.DEBUG)

    # Create a console handler and set the logging level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Create a formatter and attach it to the handlers
    formatter = logging.Formatter('%(asctime)s - [%(levelname)s]: %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # print in the terminal
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG) 
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    
    selenium_logger_setup()

    # Inspect the root logger and modify its behavior (if WebDriver uses the root logger)
    root_logger = logging.getLogger()
    for handler in root_logger.handlers:
        handler.addFilter(WebDriverFilter())

    return logger

