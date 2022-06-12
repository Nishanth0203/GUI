from tkinter import *
import sqlite3

root=Tk()

l1=Label(root,text="BookingId")
l2=Label(root,text="Passenger Name")
l3=Label(root,text="Flight")
l4=Label(root,text="Source")
l5=Label(root,text="Duration")

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
Source=""
def select():
    if radio.get()==1:
        Source="Delhi"
    elif radio.get()==2:
        Source="Mumbai"
    elif radio.get()==3:
        Source="Chennai"
    else:
        Source="Kolkata"
rb1=Radiobutton(root,text="Delhi",variable=radio,value=1,command=select)
rb2=Radiobutton(root,text="Mumbai",variable=radio,value=2,command=select)
rb3=Radiobutton(root,text="Chennai",variable=radio,value=3,command=select)
rb4=Radiobutton(root,text="Kolkata",variable=radio,value=4,command=select)
rb1.grid(row=4,column=2)
rb2.grid(row=4,column=3)
rb3.grid(row=4,column=4)
rb4.grid(row=4,column=5)

spin=Spinbox(root,from_=0,to=30)
spin.grid(row=5,column=2)

def insert():
    strng="Insert into Flight values(?,?,?,?,?)"
    curs.execute(strng,(e1.get(),e2.get(),e3.get(),Source,spin.get()))
    conn.commit()
def delete():
    pass
def update():
    pass
def select():
    pass
b1=Button(root,text="Insert",command=insert)
b2=Button(root,text="delete",command=update)
b3=Button(root,text="update",command=delete)
b4=Button(root,text="select",command=select)

b1.grid(row=6,column=1)
b2.grid(row=6,column=2)
b3.grid(row=7,column=1)
b4.grid(row=7,column=2)

conn=sqlite3.connect('ex4.db')
curs = conn.cursor()

strng='CREATE TABLE Flight(BookingId char(10),Passenger Name varchar(40), Flight char(7),Source char(7),Durationint)'
curs.execute(strng)

mainloop()