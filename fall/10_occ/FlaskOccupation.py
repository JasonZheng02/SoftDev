# Marxist_ZhengJ_ChinK
# Jason Zheng
# SoftDev1 pd09
# Template flask app
# 2019-09-23

from flask import Flask, render_template
import random
app = Flask(__name__) #create instance of class Flask

def MakeArray():
    array = []
    file = open("occupations.csv",'r')
    file.readline()
    for line in file:
        if '"' in line:
            array.append(line.split('"')[1:])
        else:
            array.append(line.split(','))
    array = array[:-1]
    for line in array:
        line[1] = line[1][:-1]
        if ',' in line[1]:
            line[1] = line[1][1:]
    return array

def MakeDict(array):
    dic = {}
    x = round(random.uniform(0,99.8),1)
    y = 0
    for line in array:
        dic[line[0]] = line[1]
        y += float(line[1])
        if y > x:
            return(line[0])

def RandomOccupation():
    return(MakeDict(MakeArray()))

@app.route("/")
def hello_world():
    return "Hey there"

@app.route("/occupyflaskst")
def occupation():
    occupation = RandomOccupation()
    coll = MakeArray()
    return render_template(
        'occupations.html',
        foo = "Marxist",
        collection = coll,
        job = occupation)

if __name__ == "__main__":
    app.debug = True
    app.run()
