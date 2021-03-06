# importing libraries and packages
from datetime import datetime

from create_new_df import create_new_df
from get_data import get_data_from_csv, unzip_data
from push_data import push_data_to_csv, push_data_to_mongo
from scrapping import twitter_scrapping

#TO DO
# Recuperer les données de mongo et reprendre le scrap à partir de la derniere date scrappée 
# Recuperer la colonne id du df recupéré pour ne pas rescrap certains tweets



def main_function():
    """Main function that get the data from the given zip then scrap and create the simplified dataframe 
    """
    path_to_csv = "data.csv"
    unzip_data("data.csv.zip")

    df = get_data_from_csv(path_to_csv)
    df = df.dropna()
    df = df.astype({"id" : int, "retweet" : int, "like" : int, "reply" : int})


    last_date = "2021-11-14"
    id_list = []
    if(df.size != 0):
        dates = df["date"].values        
        dates = [datetime.strptime(element, "%Y-%m-%d").date() for element in dates]
        last_date = max(dates)
        last_date = datetime.strftime(last_date, "%Y-%m-%d")
        id_list = df[df["date"] == last_date].index.to_list()

    ## Last date of scrapping by the creators : 30/01/2022
    # scrapped_df = twitter_scrapping(id_list, last_date)
    # df = df.append(scrapped_df)

    df1, df2, df3 = create_new_df(df)

    # push_data_to_csv(df1, "df1_data.csv")
    # push_data_to_csv(df2, "df2_data.csv")
    # push_data_to_csv(df3, "df3_data.csv")

    push_data_to_mongo(df,'all_data')
    push_data_to_mongo(df1,'tweets_tag')
    push_data_to_mongo(df2,'tweets_user')
    push_data_to_mongo(df3,'tweets_day')
