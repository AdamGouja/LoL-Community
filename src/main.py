import pandas as pd
import tweepy
import json

keys = json.load(open('./keys.json'))
auth = tweepy.OAuthHandler(keys['key'], keys['secret_key'])
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

## Trouver des mots clefs
## Recuperer les tweets 
## Affectation aux categories 
## Machine learning

## Scrapping
