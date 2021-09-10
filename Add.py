from tkinter import *
import sqlite3

def add():
	#creating new screen
	top=Toplevel()
	con=sqlite3.connect('phone.db')
	cur=con.cursor()
	top.title('Add')
	top.geometry('1250x720')
	top.configure(bg='black')
	#adding form
	l4=Label(top,text='Adding data',bg='#242424',font=('corbel' ,20 ),fg='white',padx=100,pady=20)
	l4.pack(fill=X)
	l5=Label(top,text='First name',font='corbel 10', bg='#242424',fg='white')
	l5.place(x=400,y=200)
	l5=Label(top,text='Last name',font='corbel 10', bg='#242424',fg='white')
	l5.place(x=400,y=250)
	l5=Label(top,text='Address ',font='corbel 10', bg='#242424',fg='white')
	l5.place(x=400,y=300)
	l5=Label(top,text='Mobile ',font='corbel 10', bg='#242424',fg='white')
	l5.place(x=400,y=350)	
	l5=Label(top,text='Pincode',font='corbel 10', bg='#242424',fg='white')

	
	l5.place(x=400,y=400)
	e1=Entry(top)
	e1.place(x=600,y=200)
	e2=Entry(top)
	e2.place(x=600,y=250)
	e3=Entry(top)
	e3.place(x=600,y=300)
	e4=Entry(top)
	e4.place(x=600,y=350)
	e5=Entry(top)
	e5.place(x=600,y=400)
	def add1():
		con=sqlite3.connect('phone.db')
		cur=con.cursor()
		s1=e1.get()
		s2=e2.get()
		s3=e3.get()
		s4=e4.get()
		s5=e5.get()
		try:
			
			sql='insert into phonebook values(?,?,?,?,?);'
			data=(s1,s2,s3,s4,s5)
			cur.execute(sql,data)
			messagebox.showinfo('Added', 'Data inserted successfully')
			con.commit()
		except sqlite3.Error as error:
			messagebox.showerror('Error','Data not inserted '+ str(error))
	Button(top,text='Add',font='corbel 10',fg='white',bg='#242424',command=add1).place(x=600,y=500)
	con.close()