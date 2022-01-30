import pandas as pd
from search_def import get_all_tags

def create_new_df(df):
    df1 = df_tweet_tag(df)
    df2 = df_tweet_lang(df)
    df3 = df_tweet_user(df)
    return[df1, df2, df3]

def df_tweet_tag(df):
    all_tags = get_all_tags()
    to_return = pd.DataFrame()    
    print(to_return)

def df_tweet_lang(df):
    print("TO DO")

def df_tweet_user(df):
    print("TO DO")


