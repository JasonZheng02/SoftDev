from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["database"]
col = db["restaurants"]

file = open("primer-dataset.json", "r")
content = file.readlines()
for line in content:
    col.insert_one(line)

#getting this error
#document must be an instance of dict, bson.son.SON,
#bson.raw_bson.RawBSONDocument, or a type that inherits
#from collections.MutableMapping
