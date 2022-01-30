import snscrape.modules.twitter as sntwitter
import pandas as pd

from search_def import generate_search_list, tag_dict

def twitter_scrapping(id_list, last_date): 
    print("Scrapping data since " + last_date + " : ")
    tweets_dict = {}
    nb_tweet = 0

    search_list = generate_search_list()
    search_list_len = len(search_list)
    actual_search = 0

    # Using TwitterSearchScraper to scrape data and append tweets to list
    for search in search_list:
        nb_actual = 0
        to_search = search["search"]
        print(str(actual_search) + "/" + str(search_list_len) + ": Beginning of " + to_search)
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper(to_search + ' since:' + last_date).get_items()):
            nb_actual+=1
            nb_tweet+=1
            if(nb_actual%100==0):
                print("En cours : " + str(nb_actual) + " tweets")
            if tweet.id not in id_list :
                id_list.append(tweet.id)
                all_tags = add_all_tags(tweet.user.username + tweet.content)
                for tag in all_tags:
                    tweets_dict[nb_tweet] = {"id" : tweet.id, "date" : tweet.date.date(), "content" :tweet.content, "like" : tweet.likeCount, "reply" : tweet.replyCount, "retweet" : (tweet.retweetCount + tweet.quoteCount),"username" : tweet.user.username, "tag" : tag}
        print(str(nb_actual) + " tweets recupéré pour " + to_search)
        print()
        actual_search+=1

    # Creating a dataframe from the tweets list above
    print("Nombre de tweet scrappé : " + str(nb_tweet))
    tweets_df = pd.DataFrame(tweets_dict)
    return tweets_df.T

def add_all_tags(text_to_check):
    text_to_check = text_to_check.lower()
    tags = set()
    ligues = tag_dict.keys()
    for ligue_id in ligues:
        ligue_data = tag_dict[ligue_id]
        ligue_teams = ligue_data["teams"]
        ligue_tag = ligue_data["tag"]
        if(ligue_tag in text_to_check and ligue_id not in tags) : 
            tags.add(ligue_id)
        for team_id in ligue_teams.keys():
            team_data = ligue_teams[team_id]
            team_players = team_data["players"]
            team_tags = team_data["tag"]
            for team_tag in team_tags : 
                if(team_tag in text_to_check and team_id not in tags) : 
                    tags.add(team_id)
            for player_id in team_players.keys():
                player_data = team_players[player_id]
                for tag in player_data:
                    if(tag in text_to_check and player_id not in tags) :
                        tags.add(team_id)
    return tags