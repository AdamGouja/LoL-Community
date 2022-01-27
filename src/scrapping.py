import snscrape.modules.twitter as sntwitter
import pandas as pd

from search_def import generate_search_list, tag_dict

def twitter_scrapping(id_list, last_date): 
    tweets_dict = {}
    nb_tweet = 0

    search_list = generate_search_list(tag_dict)
    search_list_len = len(search_list)
    actual_search = 0

    # Using TwitterSearchScraper to scrape data and append tweets to list
    for search in search_list:
        nb_actual = 0
        tags = search["tag"]
        to_search = search["search"]
        print(str(actual_search) + "/" + str(search_list_len) + ": Beginning of " + to_search)
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper(to_search + ' since:' + last_date).get_items()):
            nb_actual+=1
            if(nb_actual%100==0):
                print("En cours : " + str(nb_actual) + " tweets")
            if tweet.id not in id_list :
                id_list.append(tweet.id)
                tweets_dict[tweet.id] = {"id" : tweet.id, "date" : tweet.date.date(), "content" :tweet.content, "like" : tweet.likeCount, "reply" : tweet.replyCount, "retweet" : (tweet.retweetCount + tweet.quoteCount),"username" : tweet.user.username, "tag" : tags}
            else :
                current_list = tweets_dict[tweet.id]["tag"]
                new_list = list(set(current_list) | set(tags))
                tweets_dict[tweet.id]["tag"] = new_list
        print(str(nb_actual) + " tweets recupéré pour " + to_search)
        print()
        nb_tweet+=nb_actual
        actual_search+=1

    # Creating a dataframe from the tweets list above
    print("Nombre de tweet scrappé : " + str(nb_tweet))
    tweets_df = pd.DataFrame(tweets_dict)
    tweets_df.reset_index()
    return tweets_df.T