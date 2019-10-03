# Jason Zheng
# SoftDev1 pd09
# K
# Date

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def login():
	return render_template("login.html", foo = "Login Page")

@app.route("/Welcome")
def welcome():
	return render_template("welcome.html",
							foo = "Welcome Page",
							user = request.args['username'],
							pword = request.args['password'])

if __name__ == "__main__":
	app.debug = True
	app.run()
