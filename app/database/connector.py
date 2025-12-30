from pymongo import MongoClient
from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

MONGO_HOST=os.getenv("MONGO_HOST")
MONGO_PORT=os.getenv("MONGO_PORT")
MONGO_DB=os.getenv("MONGO_DB")

MONGO_URI = f'mongodb://{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}'

def get_db():
    try:
        client = MongoClient(MONGO_URI)
        db = client[MONGO_DB]
        return db
    except Exception as e:
        raise e