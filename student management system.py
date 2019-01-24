import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import *


connection=sqlite3.connect("Student_portal.db")
# connection = sqlite3.connect("student1.db")

stdportal=tk.Tk()
stdportal.title(" Student Portal ")
stdportal.geometry("1100x500")
# stdportal.config(font=("Arial" ,20))
# stdportal.grid(row=0, column=0)
heading=tk.Label(stdportal, text= "Enter your Details below", width=50)
heading.config(font=("arial", 18))
heading.grid(row=0, column=1, pady=(10,10))

stu_name=tk.Label(stdportal, text= "Enter your name", width=30)
stu_name.config(font=("arial", 15))
stu_name.grid(row=1, column=0, pady=(10,10))
Student_name= tk.Entry(stdportal)
Student_name.config(font=("arial", 30))
Student_name.grid(row=1, column=1, pady=(0,10))

stu_Id=tk.Label(stdportal, text= "Enter your ID", width=30)
stu_Id.config(font=("arial", 15))
stu_Id.grid(row=2, column=0, pady=(0,10) )
Student_ID= tk.Entry(stdportal)
Student_ID.config(font=("arial", 30))
Student_ID.grid(row=2, column=1, pady=(0,10) )


stu_college=tk.Label(stdportal, text= "Enter your college", width=30)
stu_college.config(font=("arial", 15))
stu_college.grid(row=3, column=0, pady=(0,10) )
Student_college= tk.Entry(stdportal)
Student_college.config(font=("arial", 30))
Student_college.grid(row=3, column=1, pady=(0,10) )

stu_add=tk.Label(stdportal, text= "Enter your address", width=30)
stu_add.config(font=("arial", 15))
stu_add.grid(row=4, column=0, pady=(0,10) )
Student_address= tk.Entry(stdportal)
Student_address.config(font=("arial", 30))
Student_address.grid(row=4, column=1, pady=(0,10) )

stu_ph=tk.Label(stdportal, text= "Enter your phone", width=30)
stu_ph.config(font=("arial", 15))
stu_ph.grid(row=5, column=0, pady=(0,10) )
Student_phone= tk.Entry(stdportal)
Student_phone.config(font=("arial", 30))
Student_phone.grid(row=5, column=1, pady=(0,10))

# Table_name = "student1_table"

Table_name1 = "stdportal_table"
Student_ID1 = "stdportal_ID"
Student_name1 = "stdportal_name"
Student_college1 = "stdportal_college"
Student_address1 = "stdportal_address"
Student_phone1 = "stdportal_phone"

def ret():
    global secondwinow
    secondwinow = tk.Tk()

    secondwinow.title("display result")

    appLabel = tk.Label(secondwinow, text="Student management system", fg="#06a099", width=30)
    appLabel.config(font=("Sylfaen", 25))
    appLabel.grid(row=0, column=1)

    tree = ttk.Treeview(secondwinow)
    tree["columns"] = ("one", "two", "three", "four")
    tree.heading("one", text="student name")
    tree.heading("two", text="college name")
    tree.heading("three", text="student address")
    tree.heading("four", text="student phone no.")


    cursor =connection.execute("SELECT * FROM " + Table_name1 + " ;")
    i = 0

    for row in cursor:
        tree.insert('', i, text="student" + str(row[0]),
                    values=(row[1], row[2], row[3], row[4]))
        i = i + 1

    tree.grid(row=2, column=1)
    connection.close()
    secondwinow.mainloop()

def input1():
    global Table_name1
    Table_name1 = "stdportal_table"  # table name
    Student_ID1 = "stdportal_ID"
    Student_name1 = "stdportal_name"
    Student_college1 = "stdportal_college"
    Student_address1 = "stdportal_address"
    Student_phone1 = "stdportal_phone"


    ID1 = Student_ID.get()
    name1 = Student_name.get()
    college1 = Student_college.get()
    address1 = Student_address.get()
    phone1 = Student_phone.get()
    # stdportal.geometry("800+400+500+700")


    connection.execute(" CREATE TABLE IF NOT EXISTS " + Table_name1 + " ( " + Student_ID1 + " INTEGER PRIMARY KEY AUTOINCREMENT, "
                       + Student_name1 + " TEXT, " + Student_college1 + " TEXT, " + Student_address1
                       + " TEXT, " + Student_phone1 + " INTEGER);")

    connection.execute(" INSERT INTO " + Table_name1 + " ( " + Student_name1 + " , " + Student_college1 + " , " + Student_address1 + " , "
        + Student_phone1 + " ) VALUES ('" + name1 + "' , '" + college1 + "' , '" + address1 + "' , " + str(phone1) + " ); ")
    connection.commit()


def retr():
    cursor1 = connection.execute("SELECT * FROM " + Table_name1 + ";")
    for row in cursor1:
        print("Student ID id : ", row[0])
        print("Student name : ", row[1])
        print("Student college : ", row[2])
        print("Student address : ", row[3])
        print("Student phone number : ", row[4])

    connection.close()


button= tk.Button(stdportal, text= "  LOGIN  " , command= lambda: input1())
button.config(font=("arial", 18))
button.grid(row=7, column=1, pady=(0,10))

retri = tk.Button(stdportal, text= "Retrive the entered details : " , command= lambda: retr())
retri.config(font=("arial", 18))
retri.grid(row=8, column=0, pady=(0,10))


listoftable = tk.Button(stdportal, text= "  GET ENTERED VALUES : " , command= lambda: ret())
listoftable.config(font=("arial", 18))
listoftable.grid(row=8, column=1, pady=(0,10))
stdportal.mainloop()
