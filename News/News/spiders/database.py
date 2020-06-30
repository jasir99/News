from mongoalchemy.session import Session
from pymongo import MongoClient

session = Session.connect('news')
client = MongoClient('mongodb://localhost:27017')
