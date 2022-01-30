from traceback import print_tb
import pandas as pd
import os

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
    col = db[collection_name]
    df = pd.DataFrame(list(col.find()))
    return df
