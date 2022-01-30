from warnings import catch_warnings
import pandas as pd
from langdetect import detect

def create_new_df(df):
    df1 = df_tweet_tag(df)
    df2 = df_tweet_user(df)
    return[df1, df2]

def df_tweet_tag(df):
    print("Tweet and tag dataframe")
    to_return = df.groupby(["tag", "date"]).count()
    to_return = to_return.reset_index()
    to_return = to_return.drop(columns = ["content","like","reply","retweet","username"])
    return to_return

def df_tweet_user(df):
    print("Tweet user tag dataframe")
    to_return = df.drop_duplicates(subset='id', keep="last")
    to_return = to_return.reset_index()
    to_return = to_return.drop(columns=["content", "tag", "id"])
    to_return = to_return.groupby(["username", "date"]).sum()
    to_return = to_return.reset_index()
    return to_return

