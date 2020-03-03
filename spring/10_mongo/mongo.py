#Team Rocket | Kevin Li & Jason Zheng
#SoftDev pd2
#K10 -- Mongo Import/Export
#2020-02-29

#Dataset is put into the rocket database
#Link to raw data
#https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json
#Opens json file and insert into the collection the 
#loaded pokemon part of the json file

from pymongo import MongoClient
import json

client = MongoClient('localhost', 27017)
db = client['rocket']
col = db['pokedex']

file = open('pokedex.json', 'r')
col.insert_many(json.load(file)['pokemon'])

def get_type(type):
    cursor = col.find({"type": type})
    for document in cursor:
        print(document)
        print('')

def get_rarity(spawn_Percentage):
    cursor = col.find({"spawn_chance": {"$lt": spawn_Percentage / 100} })
    for document in cursor:
        print(document)
        print('')

#def get_rarity_name(spawn_Percentage, first_Letter):
#    cursor = col.find({"spawn_chance": {"$lt": spawn_Percentage / 100}, "name":  })

#get_type("Electric")
get_rarity(1)
