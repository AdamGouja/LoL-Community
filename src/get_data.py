from traceback import print_tb
import pandas as pd
import os

path_to_csv = "data.csv"

def get_data_from_csv():
    print("Get data from csv")
    if(os.path.exists(path_to_csv)):
        print("Data already existing")
        df = pd.read_csv(path_to_csv, index_col=0)
    else: 
        print("No data found")
        df = pd.DataFrame()
    return df

def get_data_from_mongo():
    print("TODO from mongo")
