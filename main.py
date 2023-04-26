from time_taken.logger import logging
from time_taken.exception import deliveryexception
from time_taken.utils import get_collection_as_dataframe

from time_taken.config import EnvironmentVariable
from time_taken.entity.config_entity import DataIngestionConfig
from time_taken.entity import config_entity

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
        #get_collection_as_dataframe(database_name="DELIVERY_TIMETAKEN",collection_name="DELIVERY_TIMETAKEN_PROJECT")
        training_pipeline_config = config_entity.TrainingPipelineConfig()
        data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config = training_pipeline_config)
        print(data_ingestion_config.to_dict)
        
    except Exception as e:
        print(e)
        