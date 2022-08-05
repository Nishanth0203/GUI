from tkinter import *
import sqlite3

root=Tk()

l1=Label(root,text="Movie booking")
l2=Label(root,text="person name")
l3=Label(root,text="movie name")
l4=Label(root,text="class")
l5=Label(root,text="no.of tickets")

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

mainloop()