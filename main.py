from time_taken.logger import logging
from time_taken.exception import deliveryexception
from time_taken.utils import get_collection_as_dataframe

from time_taken.config import EnvironmentVariable

import os
import sys

#def test_logger_and_exception():
   # try:
   #     logging.info("Starting the test_logger_and_exception")
   #     result = 3/10
   #     print(result)
   #     logging.info("Ending point of the test_logger_and_exception")
   # except Exception as e:
   #     logging.debug(str(e))
   #     raise deliveryexception(e,sys)

    
if __name__ == "__main__":
    try:
        #test_logger_and_exception()
        get_collection_as_dataframe(database_name="DELIVERY_TIMETAKEN",collection_name="DELIVERY_TIMETAKEN_PROJECT")
    except Exception as e:
        print(e)
        