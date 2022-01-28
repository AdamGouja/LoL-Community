# importing libraries and packages
import pandas as pd
from scrapping import twitter_scrapping

#TO DO
# Recuperer les données de mongo et reprendre le scrap à partir de la derniere date scrappée 
# Recuperer la colonne id du df recupéré pour ne pas rescrap certains tweets

id_list = []
last_date="2021-11-14"

df = twitter_scrapping(id_list, last_date)

df.to_csv("data.csv")


## Trouver des mots clefs
## Recuperer les tweets 
## Affectation aux categories 
## Machine learning

## Scrapping