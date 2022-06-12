from tkinter import *
import sqlite3

root=Tk()
root.title("registration form")
root.configure(bg='#90EE90')

l1=Label(root,text="Name",bg='#90EE90')
l1.grid(row=2,column=1)
l2=Label(root,text="Course",bg='#90EE90')
l2.grid(row=3,column=1)
l3=Label(root,text="Semester",bg='#90EE90')
l3.grid(row=4,column=1)
l4=Label(root,text="Form no",bg='#90EE90')
l4.grid(row=5,column=1)
l5=Label(root,text="Contact no:",bg='#90EE90')
l5.grid(row=6,column=1)
l6=Label(root,text="Email Id",bg='#90EE90')
l6.grid(row=7,column=1)
l7=Label(root,text="Address",bg='#90EE90')
l7.grid(row=8,column=1)
l8=Label(root,text="Form",bg='#90EE90')
l8.grid(row=1,column=4)

e1=Entry(root,)
e2=Entry(root)
e3=Entry(root)
e4=Entry(root)
e5=Entry(root)
e6=Entry(root)
e7=Entry(root)
e1.grid(row=2,column=2)
e2.grid(row=3,column=2)
e3.grid(row=4,column=2)
e4.grid(row=5,column=2)
e5.grid(row=6,column=2)
e6.grid(row=7,column=2)
e7.grid(row=8,column=2)

def submit():
    pass

b1=Button(root,text="Submit",command=submit,bg='red')
b1.grid(row=8,column=4)
mainloop()