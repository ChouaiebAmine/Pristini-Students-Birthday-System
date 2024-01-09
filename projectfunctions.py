import mysql.connector
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import operator
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

#gets "birthdate" as a variable of date type
def closest(birthdate):
    date = birthdate
    # get today's date and put it in a variable "copy"
    today = datetime.datetime.today()
    copy = today
    #day counter "track"
    track = 0
    while (copy.month != date.month) or (copy.day != date.day):
        copy += datetime.timedelta(days=1)
        track += 1
    return track
def send_email(receiver_email,subject,body):
    # email configuration
    sender_email = "pristiniproject1@gmail.com"

    # SMTP server configuration (for gmail)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "pristiniproject1@gmail.com"
    smtp_password = "dfpi hmdy ybui fmzv"
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))
def birthday_wish():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin"
    )
    cursor = mydb.cursor()
    cursor.execute("USE pristini")

    dict1 = {}
    birthday_today= list()
    lst = []

    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()
    for x in result:
        num = closest(x[4])
        dict1.update({x[1]: num})

    sorted_dict = dict(sorted(dict1.items(), key=operator.itemgetter(1)))

    for x, y in sorted_dict.items():
        if y==0:
            birthday_today.append(x)

    for x in result:
        if x[1] in birthday_today:
            body = f"Happy birthday {x[1]},\n Enjoy your Day <3"
            send_email(x[5], "Happy Birthday", body)
            print("Email Sent")
