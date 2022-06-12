from tkinter import *
import sqlite3

root=Tk()

l1=Label(root,text="Movie Booking id")
l2=Label(root,text="Person Name")
l3=Label(root,text="Movie Name")
l4=Label(root,text="Class")
l5=Label(root,text="No of Tickets")

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

slide=Scale(root,from_=0, to=200,orient=HORIZONTAL)
slide.grid(row=5,column=2)

radio=IntVar()
Class=""
def select():
    if radio.get()==1:
        Class="Saving"
    else:
        Class="Non Saving"
rb1=Radiobutton(root,text="A",variable=radio,value=1,command=select)
rb2=Radiobutton(root,text="B Time of show",variable=radio,value=2,command=select)
rb1.grid(row=4,column=2)
rb2.grid(row=4,column=3)

def display():
    pass

var1=IntVar()
var2=IntVar()

t1=Checkbutton(root,text="7:15",variable=var1,onvalue=1,offvalue=0,command=display)
t2=Checkbutton(root,text="9",variable=var2,onvalue=1,offvalue=0,command=display)

t1.grid(row=4,column=4)
t2.grid(row=4,column=5)

def insert():
    pass
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

mainloop()