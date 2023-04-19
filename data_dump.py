#  pip install pymongo
import pymongo
import pandas as pd
import json

## connecting with database and VSCode
client=pymongo.MongoClient("mongodb+srv://sumaykumar369:12345@cluster1.qmvcnwu.mongodb.net/?retryWrites=true&w=majority")
#mongodb+srv://sumaykumar369:12345@cluster1.qmvcnwu.mongodb.net/?retryWrites=true&w=majority
#mongodb+srv://sumaykumar369:12345@cluster0.ajwyq8o.mongodb.net/?retryWrites=true&w=majority


## giving the csv path to open the file
DATA_FILE_PATH=r'C:\Users\win11\Project-TimeTaken-Delivery\Time-Taken-by-Delivery\finalTrain.csv'

DATABASE_NAME="DELIVERY_TIMETAKEN"
COLLLECTION_NAME="DELIVERY_TIMETAKEN_PROJECT"


## Defining function to run it
if __name__=="__main__":
    df=pd.read_csv(DATA_FILE_PATH)
    print(f"rows and columns: {df.shape}")
    
    ## Transpposing the data as MonogoDB takes key:value pair data
    json_record=list(json.loads(df.T.to_json()).values())
    
    ## Inserting the data into MongoDB after Transposing it into key value pair
    client[DATABASE_NAME][COLLLECTION_NAME].insert_many(json_record)
    