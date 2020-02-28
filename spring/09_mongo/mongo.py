# Jason Zheng
# SoftDev Pd. 2
# K09: Yummy Mongo Py
# 2020-02-28

from pymongo import MongoClient

client = MongoClient()
db = client.database
restaurants = db.restaurants

f = open("primer-dataset.json", 'r')
lines = f.readlines()
restaurants.insert_many(lines)

def find_borough(borough):
    return(restaurants.find({"borough": borough}))

def find_zip(zip):
    return(restaurants.find({"address.zipcode": zipcode}))

def find_zip_grade(zipcode, grade):
    return restaurants.find({"address.zipcode" : zipcode, "grades.grade" : grade})

def find_zip_score(zipcode, score):
    return restaurants.find({"address.zipcode": zipcode, "grades.score" : {"$lt" : score}})
