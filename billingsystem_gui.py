from tkinter import *
root = Tk()
root.title("Billing system")
root.geometry("1280x720")
bg_color='#209298'

title=Label(root,text="Billing system",bg=bg_color, fg='white',font=('times new roman',35,'bold'),relief=GROOVE,bd=12)
title.pack(fill=X)

#=================================product details==========================

F1=LabelFrame(root,text='product Details',font=('times new roman',18,'bold'),fg='green')
F1.place(x=5,y=90,width=800,height=500)

#==========================heading=============================

itm=Label(F1,text='Items',font=('Helvetic',25,'bold','underline'),fg='black')
itm.grid(row=0,column=0,padx=20,pady=15)

n=Label(F1,text='Number of Items',font=('Helvetic',25,'bold','underline'),fg='black')
n.grid(row=0,column=1,padx=20,pady=15)

cost=Label(F1,text='cost of Items',font=('Helvetic',25,'bold','underline'),fg='black')
cost.grid(row=0,column=2,padx=20,pady=15)

bread=Label(F1,text='Bread',font=('times new roman',20,'bold'),fg='lawngreen',bg='black')
bread.grid(row=1,column=0,padx=20,pady=15)

b_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7)
b_txt.grid(row=1,column=1,padx=20,pady=15)

cb_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7)
cb_txt.grid(row=1,column=2,padx=20,pady=15)

wine=Label(F1,text='wine',font=('times new roman',20,'bold'),fg='lawngreen',bg='black')
wine.grid(row=2,column=0,padx=20,pady=15)

w_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7)
w_txt.grid(row=2,column=1,padx=20,pady=15)

wb_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7)
wb_txt.grid(row=2,column=2,padx=20,pady=15)

Rice=Label(F1,text='Rice',font=('times new roman',20,'bold'),fg='lawngreen',bg='black')
Rice.grid(row=3,column=0,padx=20,pady=15)

a_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7)
a_txt.grid(row=3,column=1,padx=20,pady=15)

ab_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7)
ab_txt.grid(row=3,column=2,padx=20,pady=15)

Milk=Label(F1,text='Milk',font=('times new roman',20,'bold'),fg='lawngreen',bg='black')
Milk.grid(row=4,column=0,padx=20,pady=15)

c_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7)
c_txt.grid(row=4,column=1,padx=20,pady=15)

cb_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7)
cb_txt.grid(row=4,column=2,padx=20,pady=15)

Chips=Label(F1,text='Chips',font=('times new roman',20,'bold'),fg='lawngreen',bg='black')
Chips.grid(row=5,column=0,padx=20,pady=15)

d_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7)
d_txt.grid(row=5,column=1,padx=20,pady=15)

db_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7)
db_txt.grid(row=5,column=2,padx=20,pady=15)

T=Label(F1,text='Total Price',font=('times new roman',20,'bold'),fg='lawngreen',bg='black')
T.grid(row=6,column=0,padx=20,pady=15)

t_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7)
t_txt.grid(row=6,column=1,padx=20,pady=15)

ct_txt=Entry(F1,font='arial 15 bold',relief=SUNKEN,bd=7)
ct_txt.grid(row=6,column=2,padx=20,pady=15)

#========================================bill========================

F2=Frame(root,relief=GROOVE,bd=10)
F2.place(x=820,y=90,width=430,height=500)
bill_title=Label(F2,text='Receipt',font='arial 15 bold',bd=7,relief=GROOVE).pack(fill=X)
scrol=Scrollbar(F2,orient=VERTICAL)
scrol.pack(side=RIGHT,fill=Y)
textarea=Text(F2,font='arial 15 bold',yscrollcommand=scrol.set)
textarea.pack(fill=BOTH)
scrol.config(command=textarea.yview)

#================================button======================


F3=Frame(root,relief=GROOVE,bd=10)
F3.place(x=5,y=590,width=1270,height=120)

btn1=Button(F3,text='Total',font='arial 25 bold',bg='yellow',fg='crimson',padx=5,pady=5,width=10)
btn1.grid(row=0,column=0,padx=20,pady=10)

btn2=Button(F3,text='Receipt',font='arial 25 bold',bg='yellow',fg='crimson',padx=5,pady=5,width=10)
btn2.grid(row=0,column=1,padx=20,pady=10)

btn3=Button(F3,text='Print',font='arial 25 bold',bg='yellow',fg='crimson',padx=5,pady=5,width=10)
btn3.grid(row=0,column=2,padx=20,pady=10)

btn4=Button(F3,text='Reset',font='arial 25 bold',bg='yellow',fg='crimson',padx=5,pady=5,width=10)
btn4.grid(row=0,column=3,padx=20,pady=10)

btn5=Button(F3,text='Exit',font='arial 25 bold',bg='yellow',fg='crimson',padx=5,pady=5,width=10)
btn5.grid(row=0,column=4,padx=20,pady=10)

root.mainloop()

