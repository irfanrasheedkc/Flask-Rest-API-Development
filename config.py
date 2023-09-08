from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve MongoDB username and password from environment variables
mongo_username = os.getenv("MONGO_USERNAME")
mongo_password = os.getenv("MONGO_PASSWORD")

# Construct the MongoDB URI
uri = f"mongodb+srv://{mongo_username}:{mongo_password}@cluster0.mznznpy.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['DATA']


# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Connected to database")
except Exception as e:
    print(e)
