import pandas as pd
import twint

twint_c = twint.Config()
twint_c.Search = ['LOL']
twint_c.Limit = 500
twint_c.Store_csv = True
twint_c.Output = "data/lol_tweet.csv"

twint.run.Search(twint_c)


## Trouver des mots clefs
## Recuperer les tweets 
## Affectation aux categories 
## Machine learning

## Scrapping
