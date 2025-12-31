from pymongo import MongoClient
from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

MONGO_HOST=os.getenv("MONGO_HOST")
MONGO_PORT=os.getenv("MONGO_PORT")
MONGO_DB=os.getenv("MONGO_DB")

MONGO_URI = f'mongodb://{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}'
MONGO_COLLECTION = "contacts"

class MongoDB:
    def __init__(self, uri=MONGO_URI, db_name=MONGO_DB, collection_name=MONGO_COLLECTION):
        self.db_name = db_name
        self.collection_name = collection_name
        self.client = MongoClient(uri)
        
    def close_connection(self):
        try:
            self.client.close()
        except Exception as e:
            raise e
    
    def get_db(self):
        try:
            db = self.client[self.db_name]
            return db
        except Exception as e:
            raise e

    def get_collection_name(self):
        return self.collection_name
