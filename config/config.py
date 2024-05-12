from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
import configparser

config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))

uri = config['DEFAULT']['DB_URI']

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.Blogging
blogs_collection = db["blog_data"]

db_connection = blogs_collection
