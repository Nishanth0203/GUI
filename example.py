from tkinter import *
import sqlite3
root=Tk()

l1=Label(root,text="custid")
l2=Label(root,text="customername")
l3=Label(root,text="branch")
l4=Label(root,text="accountype")
l5=Label(root,text="amount")

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
accounttype=""
def select():
    if radio.get()==1:
        accounttype="saving"
    else:
        accountytpe="not saving"
rb1=Radiobutton(root,text="saving",variable=radio,value=1)
rb2=Radiobutton(root,text="not saving",variable=radio,value=1)
rb1.grid(row=4,column=2)
rb2.grid(row=4,column=3)

slide=Scale(root,from_=0, to=200,orient=HORIZONTAL)
slide.grid(row=5,column=2)

spin=Spinbox(root,from_=1, to=200)
spin.grid(row=6,column=6)

def select():
    pass
def update():
    pass
def delete():
    pass
def insert():
    pass

b1=Button(root,text="delete",command=delete)
mainloop()