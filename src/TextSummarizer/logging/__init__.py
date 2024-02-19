import os
import sys
import logging

# logging format => ascii time, level of logging, module name (i.e. main.py is root), message
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
# logging file directory
log_dir = "logs"
# logging file
log_filepath = os.path.join(log_dir,"running_logs.log")
# create logging file in the directory if not exist
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        # logging in file
        logging.FileHandler(log_filepath),
        # logging in termical
        logging.StreamHandler(sys.stdout)
    ]
)

# export as logger 
logger = logging.getLogger("textSummarizerLogger")