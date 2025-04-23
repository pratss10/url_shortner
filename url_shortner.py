"""
# import datetime   # This will be needed later
# import os
# from pprint import pprint
# from dotenv import load_dotenv
# from pymongo import MongoClient
# #0-9,a-z,A-Z

# cntr = 0

# def base62_convert(num):
#     base = 62
#     cntr+=1
#     chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     result = ""
#     while num > 0:
#         result = chars[num % base] + result
#         num //= base
#     return result

# def encode_url(url):
#     # Check if the URL is already in the database
#     existing_url = urls.find_one({"url": url})
#     if existing_url:
#         return existing_url['short_url']

#     # If not, create a new short URL

#     short_url = base62_convert(cntr)
#     urls.insert_one({"url": url, "short_url": short_url})
#     return short_url

# def decode_url(short_url):
#     # Find the original URL using the short URL
#     original_url = urls.find_one({"short_url": short_url})
#     if original_url:
#         return original_url['url']
#     else:
#         return None

# load_dotenv()
# MONGODB_URI = os.environ['MONGODB_URI']

# client = MongoClient(MONGODB_URI)

# # for db_info in client.list_database_names():
# #    print(db_info)

# db = client['URLs']
# collections = db.list_collection_names()

# urls = db["URLs"]




    """
#the above code was me testing the db now using the well formated api 

import datetime
import os
from pprint import pprint
from dotenv import load_dotenv
from pymongo import MongoClient

class URLShortener:
    def __init__(self):
        load_dotenv()
        self.MONGODB_URI = os.environ['MONGODB_URI']
        self.client = MongoClient(self.MONGODB_URI)
        self.db = self.client['URLs']
        self.urls = self.db["URLs"]
        #create a persistent counter
        if "counter" not in self.db.list_collection_names():
            self.db["counter"].insert_one({"_id": "url_counter", "value": 1})
    
    def get_next_counter(self):
        # Get and increment the counter atomically
        counter_doc = self.db["counter"].find_one_and_update(
            {"_id": "url_counter"},
            {"$inc": {"value": 1}},
            return_document=True
        )
        return counter_doc["value"]

    def base62_convert(self, num):
        base = 62
        chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        if num == 0:
            result = chars[0]
        while num > 0:
            result = chars[num % base] + result
            num //= base
        result = "chotiurl.com/" + result
        return result

    def encode_url(self, url):
        existing_url = self.urls.find_one({"long_URL": url})
        if existing_url:
            return existing_url['short_URL']
        counter = self.get_next_counter()
        short_url = self.base62_convert(counter)
        self.urls.insert_one({"long_URL": url, "short_URL": short_url})
        return short_url

    def decode_url(self, short_url):
        original_url = self.urls.find_one({"short_URL": short_url})
        if original_url:
            return original_url['long_URL']
        return None