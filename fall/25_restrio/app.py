# Jason Zheng
# SoftDev1 pd09
# K#25: Getting More REST
# 2019-11-13

from flask import Flask, render_template
import urllib.request as request
from urllib.request import urlopen
import json

app = Flask(__name__)

@app.route("/")
def root():
    return ""
    
@app.route("/taco")
def taco():
    url = urlopen("http://taco-randomizer.herokuapp.com/random/")
    response = url.read()
    data = json.loads(response)
    food = data["condiment"]
    return render_template("taco.html", name = food["name"], recipe = food["recipe"])
    
@app.route("/country")
def country():
    url = urlopen("https://restcountries.eu/rest/v2")
    response = url.read()
    data = json.loads(response)
    country = data[10]
    return render_template("country.html", name=country['name'],capital=country['capital'])
    
@app.route("/currency")
def currency():
    url = urlopen("https://api.exchangerate-api.com/v4/latest/USD")
    response = url.read()
    data = json.loads(response)
    return render_template("currency.html", currency = data["base"], rate = data["rates"]["AUD"])

if __name__ == "__main__":
    app.debug = True
    app.run()
