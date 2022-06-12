from tkinter import *
import sqlite3

root=Tk()

l1=Label(root,text="Annual Rate")
l2=Label(root,text="Number of Payments")
l3=Label(root,text="Loan Principle")
l4=Label(root,text="Monthly Payment")
l5=Label(root,text="Remaining Loan")

l1.grid(row=1,column=1,pady=10)
l2.grid(row=2,column=1,pady=10)
l3.grid(row=3,column=1,pady=10)
l4.grid(row=4,column=1,pady=10)
l5.grid(row=5,column=1,pady=10)

e1=Entry(root)
e2=Entry(root)
e3=Entry(root)
e4=Entry(root)
e5=Entry(root)

e1.grid(row=1,column=3,pady=10,padx=10)
e2.grid(row=2,column=3,pady=10,padx=10)
e3.grid(row=3,column=3,pady=10,padx=10)
e4.grid(row=4,column=3,pady=10,padx=10)
e5.grid(row=5,column=3,pady=10,padx=10)

def FinalBalance():
    strng="Insert into Loan values(?,?,?,?,?)"
    curs.execute(strng(e1.get(),e2.get(),e3.get(),e4.get(),e5.get()))
    conn.commit()
def MonthlyPayment():
    pass
def Quit():
    pass

b1=Button(root,text="Final Balance",command=FinalBalance)
b2=Button(root,text="Monthly Payment",command='MonthlyPayment')
b3=Button(root,text="Quit",command='Quit')

b1.grid(row=6,column=1)
b2.grid(row=6,column=2)
b3.grid(row=6,column=3)


conn=sqlite3.connect('ex6.db')
curs=conn.cursor()

strng='CREATE TABLE Loan(Annual Rate char(10),No of Payments char(10),Loan Principle char(10),Monthly Payment char(10),Remaining Loan char(10))'
curs.execute(strng)

mainloop()
