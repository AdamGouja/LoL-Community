from modulefinder import packagePathMap
import pandas as pd
import os
import pymongo
from pymongo import MongoClient
import json

def push_data_to_csv(df, path_to_csv):
    """Function that creates a csv from the dataframe passed in arguments

    Args:
        df (pd.Dataframe): Name of the dataframe to push
    """
    print("Push data to CSV")
    if(os.path.exists(path_to_csv)):
        os.remove(path_to_csv)
    df.to_csv(path_to_csv)

def push_data_to_mongo(df, collection_name):
    """Function that push the dataframe in arguments into the Mongo collection called "collection_name" in the database "project"

    Args:
        df (pd.Dataframe): Name of the dataframe to push
        collection_name (String): Name of the collection where the dataframe should be pushed
    """
    client = MongoClient('localhost',27017)
    db = client.project
    collection_names = db.list_collection_names()
    if collection_name in collection_names:
        print ("The collection '"+collection_name+"' already exists !")
        return
    collection = db[collection_name]
    data = json.loads(df.T.to_json()).values()
    collection.insert_many(data)
    print("The collection '"+collection_name+"' has been added successfully to the database !")
