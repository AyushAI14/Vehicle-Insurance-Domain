import os 
import logging
from logging.handlers import RotatingFileHandler
from from_root import from_root
from datetime import datetime


# defining variables
LOG_DIR = 'logs'
LOG_FILENAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_SIZE = 5 * 1024 * 1024
LOG_BACKUP = 3 


#constructing paths for  dir , files
log_dir_path = os.path.join(from_root(),LOG_DIR)
os.makedirs(log_dir_path,exist_ok=True)
log_file_path = os.path.join(log_dir_path,LOG_FILENAME)


#defining a function for log_configuration
def configure_logs():
    """
    configuring loggger | filehandler | consolehandler
    """

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # defining formating
    formatting = logging.Formatter("[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s ")

    # defining filehandler 
    filehandler = RotatingFileHandler(log_file_path,maxBytes=LOG_SIZE,backupCount=LOG_BACKUP)
    filehandler.setFormatter(formatting)
    filehandler.setLevel(logging.DEBUG)


    # defining consolehandler 
    consolehandler = logging.StreamHandler()
    consolehandler.setFormatter(formatting)
    consolehandler.setLevel(logging.DEBUG)


    logger.addHandler(consolehandler)
    logger.addHandler(filehandler)

configure_logs()