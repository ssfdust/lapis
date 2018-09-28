from mongoengine import connect
import os

MONGO_URL = os.getenv('MONGO_URL') or 'mongodb://localhost:27017/lazuli'
connect(host=MONGO_URL)
