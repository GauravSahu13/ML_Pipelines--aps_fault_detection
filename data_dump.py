import pymongo
import pandas as pd
import json

from sensor.config import mongo_client


client = pymongo.MongoClient("mongodb+srv://onShore:sahu9821@cluster0.a6ot5gp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.test

DATABASE_NAME=  "aps"
COLLECTION_NAME= "sensor"

if __name__=="__main__":
    df = pd.read_csv(r"C:\Users\Gaurav\PycharmProjects\app-fault-detection\aps_failure_training_set1.csv")
    print(f"Rows and columns: {df.shape}")

    #Convert dataframe to json so that we can dump these record in mongo db
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    #insert converted json record to mongo db
    mongo_client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

    print("Data dumped in MongoDB")