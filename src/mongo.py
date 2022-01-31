import pymongo
from pymongo import MongoClient

from get_data import get_data_from_csv, get_data_from_mongo, unzip_data
from push_data import push_data_to_csv, push_data_to_mongo

client = MongoClient('localhost',27017)
db = client.project

all_data = db['all_data']
tag = db['tweets_tag']

myquery = {"tag": "KCORP" }