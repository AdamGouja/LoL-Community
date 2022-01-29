# importing libraries and packages
from datetime import datetime
import pandas as pd

from create_new_df import create_new_df
from get_data import get_data_from_csv, get_data_from_mongo
from push_data import push_data_to_csv, push_data_to_mongo
from scrapping import twitter_scrapping

#TO DO
# Recuperer les données de mongo et reprendre le scrap à partir de la derniere date scrappée 
# Recuperer la colonne id du df recupéré pour ne pas rescrap certains tweets

def main_function():
    #df = get_data_from_mongo()
    df = get_data_from_csv()
    df = df.dropna()

    last_date = "2021-11-15"
    id_list = []
    if(df.size != 0):
        dates = df["date"].values        
        dates = [datetime.strptime(element, "%Y-%m-%d").date() for element in dates]
        last_date = max(dates)
        last_date = datetime.strftime(last_date, "%Y-%m-%d")
        id_list = df[df["date"] == last_date].index.to_list()
        
    print(last_date)
    
    ##scrapped_df = twitter_scrapping(id_list, last_date)

    ##df = df.append(scrapped_df)

    push_data_to_csv(df)

    df1, df2, df3 = create_new_df(df)

    return [df, df1, df2, df3]

main_function()