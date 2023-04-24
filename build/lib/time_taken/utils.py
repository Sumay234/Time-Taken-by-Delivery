import pandas as pd
import numpy as np
import os
import sys

from time_taken.logger import logging
from time_taken.exception import deliveryexception
from time_taken.config import mongo_client


## To read data from the database MongoDB
def get_collection_as_dataframe(database_name:str,collection_name:str):
    try:
        logging.info(f"Reading data from databas : {database_name} and collection name: {collection_name}")
        df = pd.DataFrame(mongo_client[database_name][collection_name].find())
        logging.info(f"Find columns: {df.columns}")
        if "_id" in df.columns:
            logging.info(f"Dropping columns: _id")
            df = df.drop("_id",axis=1)
        logging.info(f"Rows and Columns in df : {df.shape}")
        return df
        
    except Exception as e:
        raise deliveryexception(e,sys)