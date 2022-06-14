from tkinter import *
import sqlite3
root=Tk()

l1=Label(root,text="Reg.No.")
l2=Label(root,text="Name")
l3=Label(root,text="Dept")
l4=Label(root,text="Gender")
l5=Label(root,text="Age")



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

radio = IntVar()
gender=""
def select():
    if radio.get()==1:
        gender="Male"
    else:
        gender="Female"
rb1=Radiobutton(root,text="Male",variable=radio,value=1)
rb2=Radiobutton(root,text="Female",variable=radio,value=2)
rb1.grid(row=4,column=2)
rb2.grid(row=4,column=3)


spin=Spinbox(root,from_=1,to=24)
spin.grid(row=5,column=2)


def insert():
    strng="Insert into student values(?,?,?,?,?)"
    if radio.get()==1:
        gender="Male"
    else:
        gender="Female"
    curs.execute(strng,(e1.get(),e2.get(),e3.get(),gender,spin.get()))
    conn.commit()
def delete():
    strng1="delete from student where regno=?" 
    curs.execute(strng1,(e1.get(),))
    conn.commit()
def update():
    strng2="update student set name=? where regno=?"
    curs.execute(strng2,(e2.get(),str(e1.get())))
    conn.commit()
def select():
    strng3="SELECT * FROM ex1.db"
    curs.execute(strng3)
    conn.commit()
b1=Button(root,text="Insert",command=insert)
b2=Button(root,text="delete",command=delete)
b3=Button(root,text="update",command=update)
b4=Button(root,text="select",command=select)

b1.grid(row=6,column=1)
b2.grid(row=6,column=2)
b3.grid(row=7,column=1)
b4.grid(row=7,column=2)

conn=sqlite3.connect('ex1.db')
curs = conn.cursor()

strng='CREATE TABLE student(regno char(10),name varchar(40), dept char(7),gender char(7),age int)'
curs.execute(strng)

mainloop()

#edited one