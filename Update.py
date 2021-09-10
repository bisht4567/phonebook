from tkinter import *
import sqlite3


def update():
	top2=Toplevel()
	top2.title('Update')
	top2.configure(bg='black')
	top2.geometry('1250x740')
	top.maxsize(1250,720)
	top.minsize(1250,720)
	l4=Label(top2,text='Update data',bg='#242424',font=('corbel' ,20 ),fg='white',padx=100,pady=20)
	l4.pack(fill=X)
	l5=Label(top2,text='Enter mobile number',font='corbel 10', bg='#242424',fg='white')
	l5.place(x=350,y=200)
	e6=Entry(top2)
	e6.place(x=600,y=200)
	
	def update1():
		
		con=sqlite3.connect('phone.db')
		cur=con.cursor()
		
		s6=e6.get()
		if s6=='':
			messagebox.showerror('Error','Mobile no must be inputed')
		else:
			
	
			sql="select* from 'phonebook' where Mobile =?;"
			result=cur.execute(sql,(s6,))
			for i in result:
				n1=i[0]
				n2=i[1]
				n3=i[2]
				n4=i[3]
				n5=i[4]
			try:
			
				Label(top2,text='First name',bg='#242424',fg='White',font='corbel 10').place(x=350,y=300)
				Label(top2,text='Last name',bg='#242424',fg='White',font='corbel 10').place(x=350,y=350)
				Label(top2,text='Address',bg='#242424',fg='White',font='corbel 10').place(x=350,y=400)
				Label(top2,text='Mobile',bg='#242424',fg='White',font='corbel 10').place(x=350,y=450)
				Label(top2,text='Pincode',bg='#242424',fg='White',font='corbel 10').place(x=350,y=500)
				e1=Entry(top2)
				e1.place(x=500,y=300)
				e1.insert(0,str(n1))
		
				e2=Entry(top2)
				e2.place(x=500,y=350)
				e2.insert(0,str(n2))
		
				e3=Entry(top2)
				e3.place(x=500,y=400)
				e3.insert(0,str(n3))
		
				e4=Entry(top2)
				e4.place(x=500,y=450)
				e4.insert(0,str(n4))
		
		
		
		
				e5=Entry(top2)
				e5.place(x=500,y=500)
				e5.insert(0,str(n5))
			except UnboundLocalError as error:
				messagebox.showerror('Error','Data cannot be found on the database')	
		
		def update_record():
			s1=e1.get()
			s2=e2.get()
			s3=e3.get()
			s4=e4.get()
			s5=e5.get()
			sql='UPDATE phonebook set First_name=?,Last_name=?,Address=?,Mobile=?,Pincode=? where Mobile=?'
			data=(s1,s2,s3,s4,s5,s4)
			cur.execute(sql,data)
			messagebox.showinfo('Updated','Updated successfully')
			con.commit()
			con.close()
		
		
		Button(top2,text='Update',font='corbel 10',bg='#242424',fg='white',command=update_record).place(x=550,y=550)
			
	
	Button(top2, text='Search',font='corbel 10', bg='#242424',fg='white',command=update1).place(x=900,y=200)
	
