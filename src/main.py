# importing libraries and packages
import snscrape.modules.twitter as sntwitter
import pandas as pd

tag_dict = {
    "lec": {
        "teams": {
            "astralis",
            "excel",
            "fnatic",
            "g2",
            "madlions",
            "misfits",
            "rogue",
            "skgaming",
            "bds",
            "vitality"
        },
        "players" : {
            "astralis" : ["whiteknight","zanzarah","dajor","kobbe","promisq"],
            "excel": ["finn", "markoon", "nukeduck", "patrik","advienne"],
            "fnatic":["wunder", "razork", "humanoid", "upset","hylissang"],
            "g2":["bb", "brokenblade", "jankos", "caps", "flakked", "targamas", "targou"],
            "madlions":["armut", "elyoya", "reeker", "unforgiven", "kaiser"],
            "misfits":["hirit", "shlatan", "vetheo", "neon", "mersa"],
            "rogue":["odoamne", "odo", "malrang", "larssen", "comp", "trymbi"],
            "skgaming":["jenax", "gilius", "sertuss", "jezu", "treatz"],
            "bds":["adam", "cinkrof", "nuclearint", "xmatty", "matty", "limit"],
            "vitality":["alphari", "selfmade", "perkz", "carzzy", "labrov"]
        }
    },
    'lfl' : {
        "teams": {
            'kcorp',
            'gamersorigin',
            'solary',
            'gameward',
            'ldlc',
            'vitality',
            'misfits',
            'bds',
            'elyandra',
            'oplon',
        },
        "players" : {
            "kcorp" : ["cabochard","113","saken","rekkles","hantera"],
            "gamersorigin": ["vizicsacsi", "karimkt", "ronaldo", "smiley","enjawve"],
            "solary":["kio", "djoko", "scarlet", "asza","steelback"],
            "gameward":["melonik", "akabane", "czekoload", "innaxe", "kamilius"],
            "ldlc":["ragner", "yike", "eika", "exakick", "doss"],
            "vitality":["szygenda", "skeanz", "diplex", "jeskla", "jactroll"],
            "misfits":["irrelevant", "tynx", "czajek", "woolite", "vander"],
            "bds":["agresivoo", "sheo", "xico", "crownshot", "erdote"],
            "elyandra":["badlulu", "memento", "rangjun", "codysun", "raxo"],
            "oplon":["darlik", "bruness", "peng", "tiger", "absolute"]
        }
    }
}


def generate_search_list(tag_dict):
    list_of_search = []
    ligues = tag_dict.keys()
    for ligue in ligues:
        ligue_data = tag_dict[ligue]
        teams = ligue_data["teams"]
        players = ligue_data["players"]
        for team in teams:
            player_of_team = players[team]
            for player in player_of_team:
                search = player + " " + team
                list_of_search.append(search)
            list_of_search.append(team)
        list_of_search.append(ligue)
    return(list_of_search)


def twitter_scrapping(): 
    tweets_dict = {}
    id_list = []

    # Using TwitterSearchScraper to scrape data and append tweets to list
    for tag in generate_search_list(tag_dict):

        for i,tweet in enumerate(sntwitter.TwitterSearchScraper(tag+' since:2022-01-21 until:2022-01-23').get_items()):
            if i>1:
                break
            tag_list = tag.split(" ")
            if tweet.id not in id_list :
                id_list.append(tweet.id)
                tweets_dict[tweet.id] = {"date" : tweet.date, "content" :tweet.content, "like" : tweet.likeCount, "reply" : tweet.replyCount, "retweet" : (tweet.retweetCount + tweet.quoteCount),"username" : tweet.user.username, "tag" : tag_list}
            else :
                current_list = tweets_dict[tweet.id]["tag"]
                new_list = list(set(current_list) | set(tag_list))
                tweets_dict[tweet.id]["tag"] = new_list

    # Creating a dataframe from the tweets list above
    tweets_df = pd.DataFrame(tweets_dict)
    return tweets_df.T
    
print(twitter_scrapping().head(10))

## Trouver des mots clefs
## Recuperer les tweets 
## Affectation aux categories 
## Machine learning

## Scrapping