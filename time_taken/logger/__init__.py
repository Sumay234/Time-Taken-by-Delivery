import logging
from datetime import datetime
import os

LOG_DIR="timetaken_log"   ## folder name

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

LOG_FILE_NAME=f"log_{CURRENT_TIME_STAMP}.log"  ## File name

os.makedirs(LOG_DIR,exist_ok=True)  ## It will check and create if LOG_DIR is create or not


LOG_FILE_PATH=os.path.join(LOG_DIR,LOG_FILE_NAME)  ## TO define log path



logging.basicConfig(
    filename=LOG_FILE_PATH,
    filemode='w',
    format= '[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
