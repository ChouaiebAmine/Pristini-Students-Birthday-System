import operator
import mysql.connector
import csv
import datetime
import projectfunctions
import re

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin"
)
mycursor= mydb.cursor()
mycursor.execute("USE pristini")
"""""""""
#entering data from a csv file to MySQL 
mycursor.execute("CREATE TABLE STUDENTS(student_id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(50),age INT,class VARCHAR(20),birthday DATE)")

with open("test.csv") as file:
    reader=csv.DictReader(file)
    for row in reader:
        name=row["FullName"]
        age=projectfunctions.age(datetime.datetime.strptime(row["Birthday"],"%m/%d/%Y").date())
        #class_s=row["class"]
        bday=datetime.datetime.strptime(row["Birthday"],"%m/%d/%Y").date()
        insert_query="INSERT INTO STUDENTS(name,age,birthday) VALUES (%s,%s,%s)"
        mycursor.execute(insert_query,(name,age,bday))
"""""""""
#----------------------------------------------------
def showallstudents():
    mycursor.execute("SELECT * FROM students")
    result=mycursor.fetchall()
    for x in result:
        print(x[1])
        
def orderASC():
    mycursor.execute("SELECT * FROM students ORDER BY age ASC")
    result=mycursor.fetchall()
    for x in result:
        print(f"Name:{x[1]},Age:{x[2]}")
        
def orderDSC():
    mycursor.execute("SELECT * FROM students ORDER BY age DESC")
    result=mycursor.fetchall()
    for x in result:
        print(f"Name : {x[1]}, Age : {x[2]}")
        
def showclosestbd():
    dict1={}
    lst=[]
    mycursor.execute("SELECT * FROM students")
    result=mycursor.fetchall()
    for x in result:
        num=projectfunctions.closest(x[4])
        dict1.update({x[1]:num})
    sorted_dict=dict(sorted(dict1.items(),key=operator.itemgetter(1)))
    for x,y in sorted_dict.items():
        print(f"Name : {x}, Days Before Birthday: {y}")

#----------------------------------------------------
#mycursor.execute("SELECT * FROM STUDENTS")
choice=None
"""while(choice!="0"):
    print("1-Show all Student's Names \n2-order students by age (ascending)\n3-order students by age (descending)\n4-show students closest birthday\n0-Quit Program")
    choice=input("enter your choice:")
    if not re.fullmatch("[0-4]",choice):
        print("Wrong input!")
    match choice:
        case "1":
            
        case "2":
            
        case "3":
            
        case "4":"""
"""""""""
mycursor.execute("SELECT * FROM students ORDER BY age DESC")
result=mycursor.fetchall()
for x in result:
    print(x[1])
    #mydb.commit()



#for x in lst:
 #   print(x)

lst=list()
with open("Students.csv") as file:
    reader=csv.DictReader(file)
    for row in reader:
        lst.append(sorted(row.items()))
#write the data into a new file "test"
with open("test.csv","a",newline="") as file:
    writer=csv.writer(file)
    for dict in lst:
        if dict['University']=='Pristini':
            writer.writerow([dict["FullName"],dict["Birthday"]])
"""""""""
