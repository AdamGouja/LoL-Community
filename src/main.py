# importing libraries and packages
from datetime import datetime
import pandas as pd

from create_new_df import create_new_df
from get_data import get_data_from_csv, get_data_from_mongo, unzip_data
from push_data import push_data_to_csv, push_data_to_mongo
from scrapping import twitter_scrapping

#TO DO
# Recuperer les données de mongo et reprendre le scrap à partir de la derniere date scrappée 
# Recuperer la colonne id du df recupéré pour ne pas rescrap certains tweets

path_to_csv = "data.csv"

def main_function():
    unzip_data("data.csv.zip")

    df = get_data_from_csv(path_to_csv)
    df = df.dropna()
    df = df.astype({"retweet" : int, "like" : int, "reply" : int})

    last_date = "2021-11-14"
    id_list = []
    if(df.size != 0):
        dates = df["date"].values        
        dates = [datetime.strptime(element, "%Y-%m-%d").date() for element in dates]
        last_date = max(dates)
        last_date = datetime.strftime(last_date, "%Y-%m-%d")
        id_list = df[df["date"] == last_date].index.to_list()

    # scrapped_df = twitter_scrapping(id_list, last_date)
    # df = df.append(scrapped_df)

    df1, df2 = create_new_df(df)

    push_data_to_csv(df1, "df1_data.csv")
    push_data_to_csv(df2, "df2_data.csv")

main_function()

