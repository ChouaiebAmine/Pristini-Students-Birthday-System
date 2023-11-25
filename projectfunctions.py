import mysql.connector
import datetime

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin"
)
cursor = mydb.cursor()


def age(birthdate):
    today = datetime.date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age
def closest(birthdate):
    date = birthdate
    today = datetime.datetime.today()
    copy = today
    track = 0
    while (copy.month != date.month) or (copy.day != date.day):
        copy += datetime.timedelta(days=1)
        track += 1
    return track



