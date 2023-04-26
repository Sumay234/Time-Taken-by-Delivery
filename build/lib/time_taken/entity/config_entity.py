import os,sys

from time_taken.exception import deliveryexception
from time_taken.logger import logging
from datetime import datetime


# Training Pipeline
class TrainingPipelineConfig:
    def __init__(self):
        try:
            self.artifact_dir = os.path.join(os.getcwd(), "artifact", f"{datetime.now().strftime('%m%d%Y_%H%M%S')}")
        except Exception as e:
            raise deliveryexception(e,sys)    

class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            self.database_name = "DELIVERY_TIMETAKEN"
            self.collection_name = "DELIVERY_TIMETAKEN_PROJECT"
            self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir,"data_ingestion")
            self.feature_store_file_path = os.path.join(self.data_ingestion_dir,"feature_store",FILE_NAME)   # to store
            self.train_file_path = os.path.join(self.data_ingestion_dir,"dataset", TRAIN_FILE_NAME)   # Training file 
            self.test_file_path = os.path.join(self.data_ingestion_dir, "dataset", TEST_FILE_NAME)    # Testing file

        except Exception as e:
            raise Exception(e,sys)
        
## Convert Data into Dictinoray:
    def to_dict(self)->dict:
        try:
            return self.__dict__
        except Exception as e:
            raise deliveryexception(e,sys)
        
class DataValidation:
    pass
