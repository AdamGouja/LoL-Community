def create_new_df(df):
    df1 = df_tweet_tag(df)
    df2 = df_tweet_user(df)
    df3 = df2
    df4 = df_tweet_day(df)
    return[df1, df2, df3, df4]

def df_tweet_tag(df):
    print("Tweet and tag dataframe")
    to_return = df.drop(columns = ["content","like","reply","retweet","username"])
    to_return = to_return.reset_index()
    to_return = to_return.groupby(["tag", "date"]).count()
    to_return = to_return.drop(columns=["index"])
    to_return = to_return.rename(columns = {"id" : "count"})
    to_return = to_return.reset_index()
    return to_return

def df_tweet_user(df):
    print("Tweet user tag dataframe")
    to_return = df.drop_duplicates(subset='id', keep="last")
    to_return = to_return.reset_index()
    to_return["interaction"] = to_return["like"] + to_return["retweet"] + to_return["reply"]
    to_return = to_return.drop(columns=["content", "tag", "id", "date", "like", "retweet", "reply"])
    to_return = to_return.groupby(["username"]).sum()
    to_return = to_return.reset_index()
    return to_return

def df_tweet_day(df):
    print("Tweet per day dataframe")
    to_return = df.drop_duplicates(subset='id', keep="last")
    to_return = to_return.reset_index()
    to_return = to_return.drop(columns=["content", "tag","like","reply","retweet","username"])    
    to_return = to_return.groupby(["date"]).count()    
    to_return = to_return.drop(columns=["index"])
    to_return = to_return.rename(columns = {"id" : "count"})
    to_return = to_return.reset_index()
    return to_return
