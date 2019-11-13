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
    url = urlopen("https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/Jason8924?api_key=RGAPI-ab734053-2408-4416-85a9-274df0786d20")
    response = url.read()
    data = json.loads(response)
    return render_template("data.html", championLevel = data['url'])

if __name__ == "__main__":
    app.debug = True
    app.run()
