# Jason Zheng
# SoftDev pd02

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/animation")
def animation():
    return render_template("animation.html")

@app.route("/animation2")
def animation2():
    return render_template("animation2.html")

@app.route("/animation3")
def animation3():
    return render_template("animation3.html")

@app.route("/animation4")
def animation4():
    return render_template("animation4.html")

@app.route("/animation5")
def animation5():
    return render_template("animation5.html")

@app.route("/animation6")
def animation6():
    return render_template("animation6.html")

@app.route("/animation7")
def animation7():
    return render_template("animation7.html")

@app.route("/animation8")
def animation8():
    return render_template("animation8.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
