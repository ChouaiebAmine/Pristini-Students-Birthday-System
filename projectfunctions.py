import mysql.connector
import datetime
import operator
from tkinter import messagebox
mydb = mysql.connector.connect(host="localhost", user="root", password="admin")
cursor = mydb.cursor()
mycursor= mydb.cursor()
mycursor.execute("USE pristini")

def age(birthdate):
    today = datetime.date.today()
    age = (
        today.year
        - birthdate.year
        - ((today.month, today.day) < (birthdate.month, birthdate.day))
    )
    return age


def closest(birthdate):
    date = birthdate
    today = datetime.datetime.today()
    copy = today
    track = 0
    while (copy.month != date.month) or (copy.day != date.day):
        copy += datetime.timedelta(days=1)
        track += 1
    print(track)


def showallstudents():
    mycursor.execute("SELECT * FROM students")
    result = mycursor.fetchall()
    #msg=messagebox.showinfo(result)
    for x in result:
        print(x[1])


def orderASC():
    mycursor.execute("SELECT * FROM students ORDER BY age ASC")
    result = mycursor.fetchall()
    for x in result:
        print(f"Name:{x[1]},Age:{x[2]}")


def orderDSC():
    mycursor.execute("SELECT * FROM students ORDER BY age DESC")
    result = mycursor.fetchall()
    for x in result:
        print(f"Name : {x[1]}, Age : {x[2]}")


def showclosestbd():
    dict1 = {}
    lst = []
    mycursor.execute("SELECT * FROM students")
    result = mycursor.fetchall()
    for x in result:
        num = closest(x[4])
        dict1.update({x[1]: num})
    sorted_dict = dict(sorted(dict1.items(), key=operator.itemgetter(1)))
    for x, y in sorted_dict.items():
        print(f"Name : {x}, Days Before Birthday: {y}")
