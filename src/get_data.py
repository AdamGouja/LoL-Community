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

def get_data_from_mongo(collection_name):
    """Gets the data from le collection called "collection_name" and puts it in a dataframe

    Args:
        collection_name (String): Name of the collection

    Returns:
        pd.Dataframe: Dataframe of the data in the collection
    """
    client = MongoClient('localhost',27017)
    db = client.project
    collection_names = db.list_collection_names()
    if collection_name not in collection_names:
        print ("The collection '"+collection_name+"' doesn't exist !")
        return
    col = db[collection_name]
    df = pd.DataFrame(list(col.find()))
    return df
