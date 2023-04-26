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
    #mongo_db_url:str = os.getenv("mongodb+srv://sumaykumar369:12345@cluster1.qmvcnwu.mongodb.net/?retryWrites=true&w=majority")

env_var = EnvironmentError()
mongo_client = pymongo.MongoClient("mongodb+srv://sumaykumar369:12345@cluster1.qmvcnwu.mongodb.net/?retryWrites=true&w=majority")
TARGET_COLUMN = "Time_taken(min)"


