import pymongo
import pandas as pd
import numpy as np
import json
import os
import sys

from dataclasses import dataclass

@dataclass
class EnvironmentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_PATH")
    

env_var = EnvironmentError()
mongo_client = pymongo.MongoClient(env_var,mongo_db_url)
TARGET_COLUMN = "Time_taken(min)"

print(env_var.mongo_db_url)
