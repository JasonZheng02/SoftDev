# Team Green Cheese
# Jason Zheng
# SoftDev1 pd09
# K#15 Do I Know You?
# 2019-10-07

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def login():
	return render_template("login.html")

@app.route("/Welcome")
def welcome():
    if request.args['username'] == "Bob" and request.args['password'] == "Green Cheese":
        return render_template("welcome.html",
                                user = request.args['username'])
    elif request.args['username'] != "Bob":
        return render_template("failuser.html",
                                user = request.args['username'])
    else:
        return render_template("failpword.html",
                                user = request.args['username'])

if __name__ == "__main__":
	app.debug = True
	app.run()
