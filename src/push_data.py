import pandas as pd
import os

path_to_csv = "data.csv"

def push_data_to_csv(df):
    print("Push data to CSV")
    if(os.path.exists(path_to_csv)):
        os.remove("data.csv")
    df.to_csv("data.csv")

def push_data_to_mongo(df):
    print("TO DO")
