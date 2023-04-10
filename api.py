from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel
from typing import List

class Intent(BaseModel):
   name : str
   example: List["str"]

app = FastAPI()

def connecdb(table):
    client = MongoClient('mongodb://localhost:27017')
    db = client['dbchatbot']
    collection = db[table]
    return collection

    
@app.post("/create_intent")
def create_intent(intent: Intent):
    collection = connecdb('intents')
    document = {"name": intent.name, "example": intent.example}
    try:
        collection.insert_one(document)
        return True
    except:
        return 1

    