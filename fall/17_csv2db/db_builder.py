#Jason Zheng
#SoftDev1 pd09
#skeleton :: SQLITE3 BASICS
#Oct 10 2019

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

command = "CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER);"          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

with open('courses.csv', 'r') as csvfile:
    file = csv.DictReader(csvfile, delimiter = ",")
    for line in file:
        command = "INSERT INTO courses VALUES (\"" + line['code'] + "\"," + line['mark'] + "," + line['id'] + ");"
        c.execute(command)

command = "CREATE TABLE students (name TEXT,  age INTEGER, id INTEGER);"
c.execute(command)

with open('students.csv', 'r') as csvfile:
    file = csv.DictReader(csvfile, delimiter = ",")
    for line in file:
        command = "INSERT INTO students VALUES (\"" + line['name'] + "\"," + line['age'] + "," + line['id'] + ");"
        # insert name, age, id into table
        c.execute(command)

db.commit() #save changes
db.close()  #close database
