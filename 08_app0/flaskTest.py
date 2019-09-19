# Jason Zheng
# SoftDev1 pd09
# 3 route flask app
# 2019-09-18

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    print(__name__)
    return "no hablo quesooooooo!"

@app.route("/1")
def hello():
    return "BOB"

@app.route("/8924")
def hello1():
    return "8924"

if __name__ == "__main__":
    app.debug = True
    app.run()
