from time_taken.logger import logging
from time_taken.exception import deliveryexception

import os
import sys

def test_logger_and_exception():
    try:
        logging.info("Starting the test_logger_and_exception")
        result = 3/10
        print(result)
        logging.info("Ending point of the test_logger_and_exception")
    except Exception as e:
        logging.debug(str(e))
        raise deliveryexception(e,sys)

    
if __name__ == "__main__":
    try:
        test_logger_and_exception()
    except Exception as e:
        print(e)