# Jason Zheng
# SoftDev1 pd09
# K#24: A RESTful Journey Skyward
# 2019-11-12

from flask import Flask, render_template
import urllib.request as request
import json

app = Flask(__name__)

@app.route("/")
def root():
    url = urlopen("https://api.nasa.gov/planetary/apod?api_key=yJxn9KVczLWFlRaJBVCSlsGGtn8wkRKO0ic1rWcu")
    response = url.read()
    data = json.loads(response)
    return render_template("image.html", image = data['url'])

if __name__ == "__main__":
    app.debug = True
    app.run()