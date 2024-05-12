from pymongo.mongo_client import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
import os

uri = os.environ.get('DB_URI')

# Create a new client and connect to the server
client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))
db = client.Blogging
blogs_collection = db["blogs"]

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)