from tkinter import *
import sqlite3
root=Tk()
  
l1=Label(root,text="Custid")
l2=Label(root,text="Customer Name")
l3=Label(root,text="Branch")
l4=Label(root,text="account type")
l5=Label(root,text="Amount")
  
  
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
        accounttype="Saving"
    else:
        accounttype="Non Saving"
rb1=Radiobutton(root,text="Saving",variable=radio,value=1,command=select)
rb2=Radiobutton(root,text="Non Saving",variable=radio,value=2,command=select)
rb1.grid(row=4,column=2)
rb2.grid(row=4,column=3)

slide=Scale(root,from_=0, to=200,orient=HORIZONTAL)
slide.grid(row=5,column=2)

def insert():
    strng="Insert into Banking values(?,?,?,?,?)"
    if radio.get()==1:
        accounttype="Saving"
    else:
        accounttype="Non Saving"
    curs.execute(strng,(e1.get(),e2.get(),e3.get(),accounttype,slide.get()))
    conn.commit()
def delete():
    strng1="delete from student where regno=?"
    curs.execute(strng1,(e1.get(),))
    conn.commit()
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

conn=sqlite3.connect('ex2.db')
curs = conn.cursor()

strng='CREATE TABLE Banking(Custid char(10),Customer Name varchar(40), Branch char(7),Amount char(7),Amountint)'
curs.execute(strng)
mainloop()

#RA2011050010048
#NISHANTH RAO DUGYALA
#RA2011050010001
#VAMSI