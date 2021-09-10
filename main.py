#Phonebook directory

from tkinter import *
from tkinter import messagebox
from Add import add
from Search import search
from Update import update
from Delete import delete

import sqlite3
con=sqlite3.connect('phone.db')
cur=con.cursor()
root=Tk()
root.title('Phonebook application')
root.maxsize(1250,740)
root.minsize(1250,740)
root.configure(bg='black')
l1=Label(text='Phone Directory',bg='#242424',font=('corbel' ,20 ),fg='white',padx=100,pady=20)
l1.pack(fill=X)

l2=Label(root,text='What do you want to do? ',font='corbel, 15',fg='white',bg='#242424')
l2.place(x=450,y=150)
Button(root,text='Add',font='corbel 10',fg='white',bg='#242424',command=add).place(x=600,y=300)
Button(root,text='Search',font='corbel 10',fg='white',bg='#242424',command=search).place(x=590,y=400)
Button(root,text='Update',font='corbel 10',fg='white',bg='#242424',command=update).place(x=590,y=500)
Button(root,text='Delete',font='corbel 10',fg='white',bg='#242424',command=delete).place(x=590,y=600)
l3=Label(root,text=' All rights reserved',font='corbel 15', bg='#242424',fg='white').place(x=500,y=700)



root.mainloop()
