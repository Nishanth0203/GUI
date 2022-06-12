from cgitb import text
from tkinter import *
import sqlite3

root=Tk()

l1=Label(root,text="Contact List")
l1.grid(row=1,column=2)

text_box=Text(root,height=13,width=40)
text_box.grid(row=2,column=2)

def select():
    pass
b1=Button(root,text="Display Contact",command=select)
b1.grid(row=3,column=2)

l2=Label(root,text="New Conatct").place(x=500,y=0)

l3=Label(root,text="First Name:").place(x=500,y=20)
l4=Label(root,text="Last Name:").place(x=500,y=40)
l5=Label(root,text="Phone#:").place(x=500,y=60)

e1=Entry(root).place(x=580,y=20)
e2=Entry(root).place(x=580,y=40)
e3=Entry(root).place(x=580,y=60)

def display():
    pass

var1=IntVar()

t1=Checkbutton(root,text="Friend",variable=var1,onvalue=1,offvalue=0,command=display).place(x=590,y=90)

l6=Label(root,text="Email:").place(x=500,y=113)
e4=Entry(root).place(x=580,y=113)
l7=Label(root,text="Birthday:").place(x=500,y=135)
e5=Entry(root).place(x=580,y=135)

def declare():
    pass


b2=Button(root,text="Add Contact",command=declare).place(x=650,y=160)

l6=Label(root,text="Last Name").place(x=0,y=300)
e6=Entry(root).place(x=80,y=300)

def search():
    pass

b3=Button(root,text="Search",command=search).place(x=150,y=400)
mainloop()