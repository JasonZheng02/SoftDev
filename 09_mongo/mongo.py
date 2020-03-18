# Jason Zheng
# SoftDev Pd. 2
# K09: Yummy Mongo Py
# 2020-02-28

from pymongo import MongoClient
from bson.json_util import loads

client = MongoClient('localhost', 27017)
db = client["test"]
col = db["restaurants"]

f = open("primer-dataset.json", 'r')
lines = f.readlines()
for line in lines:
    col.insert_one(loads(line))

def find_borough(borough):
    cursor = col.find({"borough": borough})
    
    for document in cursor:
        print(document)

def find_zip(zipcode):
    cursor = col.find({"address.zipcode": zipcode})
    
    for document in cursor:
        print(document)

def find_zip_grade(zipcode, grade):
    cursor = col.find({"address.zipcode": zipcode, "grades.0.grade": grade})
    
    for document in cursor:
        print(document)

def find_zip_score(zipcode, score):
    cursor = col.find({"address.zipcode": zipcode, "grades.0.score": { "$lt": score } })
    
    for document in cursor:
        print(document)

#find_borough("Manhattan")
#find_zip("10009")
#find_zip_grade("10009", "A")
find_zip_score("10009", 1)
