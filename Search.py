from tkinter import *
import sqlite3


def search():
	top1=Toplevel()
	con=sqlite3.connect('phone.db')
	cur=con.cursor()
		
	top1.title('Search')
	top1.geometry('1250x720')
	top1.configure(bg='black')
	l4=Label(top1,text='Search data',bg='#242424',font=('corbel' ,20 ),fg='white',padx=100,pady=20)
	l4.pack(fill=X)
	l5=Label(top1,text='Enter mobile number',font='corbel 10', bg='#242424',fg='white')
	l5.place(x=350,y=200)
	e6=Entry(top1)
	e6.place(x=600,y=200)

	def search1():
		con=sqlite3.connect('phone.db')
		cur=con.cursor()
		
		s6=e6.get()
	
		sql="select* from 'phonebook' where Mobile =?;"
		result=cur.execute(sql,(s6,))
		for i in result:
			n1=i[0]
			n2=i[1]
			n3=i[2]
			n4=i[3]
			n5=i[4]
		if s6=='':
			messagebox.showerror('Error','Please enter the mobile number ')	
		else:
			try:
				
			
			
				Label(top1,text='First name',bg='#242424',fg='White',font='corbel 10').place(x=350,y=300)
				Label(top1,text='Last name',bg='#242424',fg='White',font='corbel 10').place(x=350,y=350)
				Label(top1,text='Address',bg='#242424',fg='White',font='corbel 10').place(x=350,y=400)
				Label(top1,text='Mobile',bg='#242424',fg='White',font='corbel 10').place(x=350,y=450)
				Label(top1,text='Pincode',bg='#242424',fg='White',font='corbel 10').place(x=350,y=500)
		
				Label(top1,text=n1,bg='#242424',fg='White',font='corbel 10').place(x=500,y=300)
				Label(top1,text=n2,bg='#242424',fg='White',font='corbel 10').place(x=500,y=350)
				Label(top1,text=n3,bg='#242424',fg='White',font='corbel 10').place(x=500,y=400)
				Label(top1,text=n4,bg='#242424',fg='White',font='corbel 10').place(x=500,y=450)
				Label(top1,text=n5,bg='#242424',fg='White',font='corbel 10').place(x=500,y=500)
			except UnboundLocalError as error:
				messagebox.showerror('Error','Data cannot be found on the database')
		
		
		
		
	Button(top1, text='Search',font='corbel 10', bg='#242424',fg='white',command=search1).place(x=900,y=200)
	con.close()
	