import pandas as pd
import os
import shutil
import pymongo
from pymongo import MongoClient

def unzip_data(filename):
    shutil.unpack_archive(filename, ".")

def get_data_from_csv(csv_name):
    """Creates a dataframe from a csv

    Args:
        csv_name (String): Name of the csv file

    Returns:
        pd.Dataframe: Dataframe from the CSV
    """
    print("Get data from csv")
    if(os.path.exists(csv_name)):
        print("Data already existing")
        df = pd.read_csv(csv_name, index_col=0)
    else: 
        print("No data found")
        df = pd.DataFrame()
    return df

def get_data_from_mongo(db, collection_name):
    """[summary]

    Args:
        db (mongo.database): Database
        collection_name (String): Name of the collection

    Returns:
        [type]: [description]
    """
    client = MongoClient('localhost',27017)
    dbnames = client.list_database_names()
    if db not in dbnames:
        print ("This database doesn't exist !")
        pass
    collection_names = db.list_collection_names()
    if collection_name not in collection_names:
        print ("This collection doesn't exist !")
        pass
    col = db[collection_name]
    df = pd.DataFrame(list(col.find()))
    return df
