def create_new_df(df):
    """ Main function that calls the other and create all the needed dataframes

    Args:
        df ([pandas.Dataframe]): Dataframe containing all the data
    """
    df["interaction"] = df["like"] + df["retweet"] + df["reply"]
    df = df.drop(columns = ["like","reply","retweet"])

    tweet_tag = df_tweet_tag(df)
    tweet_user = df_tweet_user(df, 10)
    tweet_day = df_tweet_day(df)
    return[tweet_tag, tweet_user, tweet_day]

def df_tweet_tag(df):
    """Generate a dataframe that contains the number of interaction and tweet for a given date and tag

    Args:
        df ([pandas.Dataframe]): Dataframe containing all the data

    Returns:
        [pandas.Dataframe]: dataframe returned
    """
    print("Tweet and tag dataframe")    
    tweet_tag = df.drop(columns = ["username",'interaction'])
    tweet_tag_final = tweet_tag.drop(columns = ["id"])
    tweet_tag_final = tweet_tag_final.groupby(["tag", "date"]).sum()
    tweet_tag_final = tweet_tag_final.reset_index()

    count = tweet_tag.groupby(["tag", "date"])["id"].count().values
    # interaction = tweet_tag.groupby(["tag", "date"])["interaction"].sum().values

    tweet_tag_final["count"] = count
    # tweet_tag_final["interaction"] = interaction
    
    return tweet_tag_final

def df_tweet_user(df, nb_users):
    """ Generate a dataframe that contains the number of interaction of the biggest (nb_users) twitter account.
    The interactions of all others users are contained as the usernamed "Autres"

    Args:
        df ([pandas.Dataframe]): dataframe that contains all the data
        nb_users (int): Nombre d'utilisateur à garder

    Returns:
        [pandas.Dataframe]: dataframe returned
    """
    print("Tweet user tag dataframe")
    tweet_data = df.drop_duplicates(subset='id', keep="last")
    tweet_user = tweet_data.drop(columns=["tag", "id", "date"])
    tweet_user = tweet_user.reset_index()
    tweet_user = tweet_user.groupby(["username"]).sum()
    tweet_user = tweet_user.drop(columns=["index"])
    tweet_user = tweet_user.sort_values(["interaction"], ascending = False)
    tweet_user = tweet_user.reset_index()

    biggest_users = tweet_user[:nb_users]
    the_rest = tweet_user[nb_users:]
    biggest_users = biggest_users.append({"username" : "Autres", "interaction" : the_rest["interaction"].sum()}, ignore_index=True)

    return biggest_users

def df_tweet_day(df):
    """ Generate a dataframe that contains the number of tweet and interaction of a given day

    Args:
        df ([pandas.Dataframe]): dataframe that contains all the data

    Returns:
        [pandas.Dataframe]: dataframe returned
    """
    print("Tweet per day dataframe")
    tweet_day = df.drop_duplicates(subset='id', keep="last")
    tweet_day = tweet_day.reset_index()
    tweet_day_final = tweet_day.drop(columns=["tag","username"])    
    tweet_day_final = tweet_day_final.groupby(["date"]).count()    
    tweet_day_final = tweet_day_final.drop(columns=["index"])
    tweet_day_final = tweet_day_final.rename(columns = {"id" : "count"})

    interaction = tweet_day.groupby(["date"])["interaction"].sum().values
    tweet_day_final["interaction"] = interaction
    tweet_day_final = tweet_day_final.reset_index()


    return tweet_day_final
