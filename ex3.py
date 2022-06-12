from tkinter import *
import sqlite3

root=Tk()

l1=Label(root,text="Empid")
l2=Label(root,text="Employee Name:")
l3=Label(root,text="Job")
l4=Label(root,text="Employee type")
l5=Label(root,text="Salary")

l1.grid(row=1,column=1)
l2.grid(row=2,column=1)
l3.grid(row=3,column=1)
l4.grid(row=4,column=1)
l5.grid(row=5,column=1)

e1=Entry(root)
e2=Entry(root)
e3=Entry(root)

e1.grid(row=1,column=2)
e2.grid(row=2,column=2)
e3.grid(row=3,column=2)

radio=IntVar()
Employeetype=""
def select():
    if radio.get()==1:
        Employeetype="Regular"
    else:
        Employeetype="Temporary"
rb1=Radiobutton(root,text="Regular",variable=radio,value=1,command=select)
rb2=Radiobutton(root,text="Temporary",variable=radio,value=2,command=select)
rb1.grid(row=4,column=2)
rb2.grid(row=4,column=3)

spin=Spinbox(root,from_=0,to=30)
spin.grid(row=5,column=2)

def insert():
    strng="Insert into Employee values(?,?,?,?,?)"
    curs.execute(strng,(e1.get(),e2.get(),e3.get(),Employeetype,spin.get()))
    conn.commit()
    
def update():
    pass
def delete():
    pass
def select():
    pass

b1=Button(root,text="Insert",command=insert)
b2=Button(root,text="Update",command=update)
b3=Button(root,text="Delete",command=delete)
b4=Button(root,text="Select",command=select)

b1.grid(row=6,column=1)
b2.grid(row=6,column=2)
b3.grid(row=7,column=1)
b4.grid(row=7,column=2)

conn=sqlite3.connect('ex3.db')
curs=conn.cursor()

strng='CREATE TABLE Employee(Empid char(10),Employee Name char(100),Job char(20),salary char(7),salaryint)'
curs.execute(strng)

mainloop()

