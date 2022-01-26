# importing libraries and packages
import snscrape.modules.twitter as sntwitter
import pandas as pd
import json

tag_dict = {
    "LEC": {
        "tag" : "lec",
        "teams": {
            "Astralis" : {
                "tag" : ["astralis"],
                "players" : {
                    "WhiteKnight" : ["whiteknight"],
                    "Zanzarah" : ["zanzarah"],
                    "Dajor" : ["dajor"],
                    "Kobbe" : ["kobbe"],
                    "Promisq" : ["promisq"],
                }
            },
            "Excel" : {
                "tag": ["excel"],
                "players" : {
                    "Finn" : ["finn"],
                    "Markoon" : ["markoon"],
                    "Nukeduck" : ["nukeduck"],
                    "Patrik" : ["patrik"],
                    "Advienne" : ["promisq"],
                    "MikyX": ["mikyx"]
                }
            },
            "Fnatic" : {
                "tag" : ["fnatic"],
                "players" : {
                    "Wunder" : ["wunder"],
                    "Razork" : ["razork"],
                    "Humanoid" : ["humanoid"],
                    "Upset" : ["upsed"],
                    "Hylissang" : ["hylissang", "hyli"]
                }
            },
            "G2" : { 
                "tag" : ["g2"],
                "players" : {
                    "Broken Blade" : ["brokenblade", "bb"],
                    "Jankos" : ["jankos"],
                    "CaPs" : ["caps", "craps", "claps"],
                    "Flakked" : ["flakked"],
                    "Targamas" : ["targamas", "targou"]
                }
            },
            "Mad Lions" : {
                "tag" : ["madlions"],
                "players" : {
                    "Armut" : ["Armut"],
                    "Elyoya" : ["elyoya", "yoya"],
                    "Reeker" : ["reeker"],
                    "Unforgiven" : ["unforgiven"],
                    "Kaiser" : ["kaiser"]
                }
            },
            "Misfits" : {
                "tag" : ["misfits"],
                "players" : {
                    "Hirit" : ["hirit"],
                    "Shlatan" : ["shlatan"],
                    "Vetheo" : ["vetheo"],
                    "Neon" : ["neon"],
                    "Marsa" : ["marsa"]
                }
            },
            "Rogue" : {
                "tag" : ["rogue"],
                "players" : {
                    "Odoamne" : ["odoamne", "odo"],
                    "Malrang" : ["malrang"],
                    "Larssen" : ["larssen"],
                    "Comp" : ["comp"],
                    "Trymbi" : ["trymbi"]
                }
            },
            "SK Gaming" : {
                "tag" : ["skgaming"],
                "players" : {
                    "Jenax" : ["jenax"],
                    "Gilius" : ["gilius"],
                    "Sertuss" : ["sertuss"],
                    "Jezu" : ["jezu"],
                    "Treatz" : ["treatz"]
                }
            },
            "BDS" : {
                "tag" : ["bds"],
                "players" : {
                    "Adam" : ["adam"],
                    "Cinkrof" : ["cinkrof"],
                    "NuclearInt" : ["nuclearint", "nuclear", "nuc"],
                    "Xmatty" : ["xmatty", "matty"],
                    "Limit" : ["limit"]
                }
            },
            "Vitality" : {
                "tag" : ["vitality", "vita"],
                "players" : {
                    "Alphari" : ["alphari"],
                    "Selfmade" : ["selfmade"],
                    "Perkz" : ["perkz"],
                    "Carzzy" : ["carzzy"],
                    "Labrov" : ["labrov"]
                }
            },
        }
    },
    "LFL": {
        "tag" : "lfl",
        "teams": {
            "KCORP" : {
                "tag" : ["kcorp"],
                "players" : {
                    "Cabochard" : ["cabochard", "cabo"],
                    "113" : ["113"],
                    "Saken" : ["saken"],
                    "Rekkles" : ["rekkles"],
                    "Hantera" : ["hantera"],
                }
            },
            "Gamers Origin" : {
                "tag": ["gamersorigin"],
                "players" : {
                    "Vizicsacsi" : ["vizicsacsi"],
                    "Karimkt" : ["karimkt"],
                    "Ronaldo" : ["ronaldo"],
                    "Smiley" : ["smiley"],
                    "Enjawve" : ["enjawve"]
                }
            },
            "Solary" : {
                "tag" : ["solary"],
                "players" : {
                    "Kio" : ["kio"],
                    "Djoko" : ["djoko"],
                    "Scarlet" : ["scarlet"],
                    "Asza" : ["asza"],
                    "Steelback" : ["steelback"]
                }
            },
            "Gameward" : { 
                "tag" : ["gameward"],
                "players" : {
                    "Melonik" : ["melonik"],
                    "Akabane" : ["akabane"],
                    "Czekoload" : ["czekoload"],
                    "Innaxe" : ["innaxe"],
                    "Kamilius" : ["kamilius"]
                }
            },
            "LDLC OL" : {
                "tag" : ["ldlc"],
                "players" : {
                    "Ragner" : ["ragner"],
                    "Yike" : ["yike"],
                    "Eika" : ["eika"],
                    "Exakick" : ["exakick"],
                    "Doss" : ["doss"]
                }
            },
            "Vitality B" : {
                "tag" : ["vitality", "vita"],
                "players" : {
                    "Szygenda" : ["szygenda"],
                    "Skeanz" : ["skeanz"],
                    "Diplex" : ["diplex"],
                    "Jeskla" : ["jeskla"],
                    "Jactroll" : ["jactroll"]
                }
            },
            "Misfits Academy" : {
                "tag" : ["misfits"],
                "players" : {
                    "Irrelevant" : ["irrelevant"],
                    "Tynx" : ["tynx"],
                    "Czajek" : ["czajek"],
                    "Woolite" : ["woolite"],
                    "Erdote" : ["erdote"]
                }
            },
            "BDS Academy" : {
                "tag" : ["bds"],
                "players" : {
                    "Agresivoo" : ["agresivoo"],
                    "Sheo" : ["sheo"],
                    "Xico" : ["xico"],
                    "Crownshot" : ["crownshot"],
                    "Treatz" : ["treatz"]
                }
            },
            "Elyandra" : {
                "tag" : ["elyandra"],
                "players" : {
                    "Badlulu" : ["badlulu"],
                    "Memento" : ["memento"],
                    "Rangjun" : ["rangjun"],
                    "Codysun" : ["codysun"],
                    "Raxo" : ["raxo"]
                }
            },
            "Oplon" : {
                "tag" : ["oplon"],
                "players" : {
                    "Darlik" : ["darlik"],
                    "Bruness" : ["bruness"],
                    "Peng" : ["peng"],
                    "Tiger" : ["tiger"],
                    "Absolute" : ["absolute"]
                }
            },
        }
    }
}


def generate_search_list(tag_dict):
    list_of_search = []
    ligues = tag_dict.keys()
    for ligue_id in ligues:
        ligue_data = tag_dict[ligue_id]
        ligue_teams = ligue_data["teams"]
        ligue_tag = ligue_data["tag"]
        for team_id in ligue_teams.keys():
            team_data = ligue_teams[team_id]
            team_players = team_data["players"]
            team_tags = team_data["tag"]
            for team_tag in team_tags : 
                for player_id in team_players.keys():
                    player_data = team_players[player_id]
                    for tag in player_data:
                        search = {"tag" : [player_id, team_id, ligue_id], "search" : (tag + " " + team_tag)}
                        list_of_search.append(search)
                search = {"tag" : [team_id, ligue_id], "search" : team_tag}
                list_of_search.append(search)
        search = {"tag" : [ligue_id], "search" : ligue_tag}
        list_of_search.append(search)
    return(list_of_search)

def twitter_scrapping(): 
    tweets_dict = {}
    id_list = []

    # Using TwitterSearchScraper to scrape data and append tweets to list
    for search in generate_search_list(tag_dict):

        tags = search["tag"]
        to_search = search["search"]
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper(to_search + ' since:2022-01-21').get_items()):
            print(str(i) + " tweet recupéré pour " + to_search)
            if i>10:
                break
            if tweet.id not in id_list :
                id_list.append(tweet.id)
                tweets_dict[tweet.id] = {"date" : tweet.date, "content" :tweet.content, "like" : tweet.likeCount, "reply" : tweet.replyCount, "retweet" : (tweet.retweetCount + tweet.quoteCount),"username" : tweet.user.username, "tag" : tags}
            else :
                current_list = tweets_dict[tweet.id]["tag"]
                new_list = list(set(current_list) | set(tags))
                tweets_dict[tweet.id]["tag"] = new_list

    # Creating a dataframe from the tweets list above
    tweets_df = pd.DataFrame(tweets_dict)
    return tweets_df.T

df = twitter_scrapping()


## Trouver des mots clefs
## Recuperer les tweets 
## Affectation aux categories 
## Machine learning

## Scrapping