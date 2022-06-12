from tkinter import *
import sqlite3
root=Tk()

root.title("Phone list")

l1=Label(root,text="Name")
l1.grid(row=1,column=1)
e1=Entry(root)
e1.grid(row=1,column=2)
l2=Label(root,text="Phone")
l2.grid(row=2,column=1)
e2=Entry(root)
e2.grid(row=2,column=2)

rb1=Button(root,text="Add")
rb2=Button(root,text="Update")
rb3=Button(root,text="Delete")
rb1.grid(row=3,column=1)
rb2.grid(row=3,column=2)
rb3.grid(row=3,column=3)

listbox=Listbox(root,width=60)
listbox.grid(row=4,column=2)
listbox.insert(END,"{0} {1}".format("Name","Phone"))
mainloop()