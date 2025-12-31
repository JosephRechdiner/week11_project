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
    def __init__(self, db=MONGO_DB, uri=MONGO_URI, collection=MONGO_COLLECTION):
        self.db = db
        self.uri = uri
        self.collection = collection
        self.client = None

    def get_collection(self):
        try:
            if not self.client:
                self.client = self.get_client()
                db = self.client[self.db]
                return db[self.collection]
        except Exception as e:
            raise e
        
    def get_db(self):
        try:
            if not self.client:
                self.client = self.get_client()
                db = self.client[self.db]
                return db
        except Exception as e:
            raise e

    def get_client(self):
        try:
            if not self.client:
                self.client = MongoClient(self.uri)
            return self.client
        except Exception as e:
            raise e
        
    def close_connection(self):
        try:
            self.client.close()
        except Exception as e:
            raise e