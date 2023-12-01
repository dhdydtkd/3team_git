from pymongo import MongoClient

def mongoInsert(event_data):
    client = MongoClient('mongodb://localhost:27017')
    db = client['reports']
    collection = db['events']
    
    collection.insert_one(event_data)