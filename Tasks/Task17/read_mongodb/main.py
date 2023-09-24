import pandas as pd
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
# Make sure to replace `'mongodb://localhost:27017/'` with the appropriate connection string for your MongoDB server.

db = client['your_database_name']
collection = db['your_collection_name']
# Replace `'your_database_name'` and `'your_collection_name'` with the actual names of your database and collection.

data = list(collection.find())
# This retrieves all the documents from the collection and stores them in a list.

df = pd.DataFrame(data)
# The `pd.DataFrame()` function converts the list of documents into a pandas DataFrame.
