import sqlite3
import tkinter as tk
from tkinter import *
# connection=sqlite3.connect("Student_portal.db")
connection = sqlite3.connect("student1.db")

stdportal=tk.Tk()
# stdportal.configure(background="Blue")
heading=tk.Label(stdportal, text= "Enter your Details")
heading.pack()
# Table_name= tk.Entry(stdportal)
stu_name=tk.Label(stdportal, text= "Enter your name")
stu_name.pack()
Student_name= tk.Entry(stdportal)
Student_name.pack()

stu_Id=tk.Label(stdportal, text= "Enter your ID")
stu_Id.pack()
Student_ID= tk.Entry(stdportal)
Student_ID.pack()


stu_college=tk.Label(stdportal, text= "Enter your college")
stu_college.pack()
Student_college= tk.Entry(stdportal)
Student_college.pack()

stu_add=tk.Label(stdportal, text= "Enter your address")
stu_add.pack()
Student_address= tk.Entry(stdportal)
Student_address.pack()

stu_ph=tk.Label(stdportal, text= "Enter your phone")
stu_ph.pack()
Student_phone= tk.Entry(stdportal)
Student_phone.pack()


# Table_name.pack()
Table_name= "student1_table"

# Table_name = "stdportal_table"
Student_ID1 = "stdportal_ID"
Student_name1 = "stdportal_name"
Student_college1 = "stdportal_college"
Student_address1 = "stdportaladdress"
Student_phone1 = "stdportal_phone"

def input1 ():
    # global Table_name

    Student_ID1=Student_ID.get()
    Student_name1=Student_name.get()
    Student_college1=Student_college.get()
    Student_address1=Student_address.get()
    Student_phone1= Student_phone.get()

    # stdportal.geometry("800+400+500+700")

    connection.execute(" CREATE TABLE IF NOT EXISTS " + Table_name + " ( " + Student_ID1 + " INTEGER PRIMARY KEY AUTOINCREMENT, " + Student_name1
                       + " TEXT, " + Student_college1 + " TEXT, " + Student_address1 + " TEXT, " + Student_phone1 + " INTEGER);")
    connection.commit()
    connection.execute(" INSERT INTO " + Table_name + " ( " + Student_name1 + " , "  + Student_college1 + " , " + Student_address1
                       + " , " + Student_phone1 + " ) VALUES ( 'Anvi' , 'DIT' , 'Dehradun, Uttrakhand', 9876553214 ); " )
    connection.commit()


def retr():
    cursor = connection.execute("SELECT * FROM " + Table_name + ";")
    for row in cursor:
        print("Student ID id : ", row[0])
        print("Student ID name : ", row[1])
        print("Student ID college : ", row[2])

    connection.close()


button= tk.Button(stdportal, text= ("Enter") , command= lambda:input1())
button.pack()

ret=tk.Button(stdportal, text= "retrive the entered details : " , command= lambda: retr())
ret.pack()


stdportal.mainloop()
