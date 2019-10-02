# Jason Zheng
# SoftDev1 pd09
# K
# Date

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def login():
	return render_template("login.html", foo = "Login Page")

@app.route("/foo.html")
def html():
	return render_template("Static.html", foo = "title")

if __name__ == "__main__":
	app.debug = True
	app.run()
