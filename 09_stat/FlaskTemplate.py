# Marxist_ZhengJ_ChinK
# Jason Zheng
# SoftDev1 pd09
# Template flask app
# 2019-09-19

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "HELLO WORLD"

@app.route("/my_foist_template")
def test_tmplt():
    coll = [0, 1, 1, 2, 3, 5, 8]
    return render_template('my_foist_template.html', foo = "Marxist", collection = coll)
    print(__name__)

if __name__ == "__main__":
    app.debug = True
    app.run()
