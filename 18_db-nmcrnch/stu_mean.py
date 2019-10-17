# Derek Leung + Jason Zheng [Team Submarine Cable Map]
# SoftDev1 pd09
# K18 -- No Trouble
# 2019-10-15
#print("ooga booga")

import sqlite3
import csv

DB_FILE = "Talos.db"
db = sqlite3.connect(DB_FILE)
c= db.cursor()
#===============================================================================
adding = True
print("Add new courses: Type \"end\" to stop")
while(adding):
    code = input("Course code: ")
    if code == "end":
        adding = False
        break
    mark = input("Mark: ")
    if mark == "end":
        adding = False
        break
    id = input("ID: ")
    if id == "end":
        adding = False
        break
    command = "INSERT INTO COURSES VALUES ({},{},{})".format(code,mark,id)
    c.execute(command)


c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='stu_avgs' ''')
if c.fetchone()[0] < 1:
    command = "CREATE TABLE stu_avgs (id INT, average FLOAT);"
    c.execute(command)
command = "SELECT name, students.id, avg(mark) FROM students, courses WHERE students.id = courses.id GROUP BY students.id;"
c.execute(command)
rows = c.fetchall()
for row in rows:
    print((" Name: {} \n ID: {} \n Average: {} \n").format(row[0],row[1],row[2]))
    c.execute("INSERT INTO stu_avgs (id,average) VALUES({},{})".format(row[1],row[2]))


#===============================================================================
db.commit()
db.close()
