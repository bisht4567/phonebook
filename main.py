#Phonebook directory

from tkinter import *
from tkinter import messagebox
import sqlite3
con=sqlite3.connect('phone.db')
cur=con.cursor()
root=Tk()
root.configure(bg='black')
l1=Label(text='Phone Directory',bg='#242424',font=('corbel' ,20 ),fg='white',padx=100,pady=20)
l1.pack(fill=X)
#----------------------------------------Adding data to database-----------------------------

#Adding to directory
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
	
#===========================searching data from databse=================	

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
	
	
			
#==================================Update in database===========================		

def update():
	top2=Toplevel()
	top2.title('Update')
	top2.configure(bg='black')
	top2.geometry('1250x720')
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
		
		
		Button(top2,text='Update',font='corbel 10',bg='#242424',fg='white',command=update_record).place(x=550,y=550)
			
	
	Button(top2, text='Search',font='corbel 10', bg='#242424',fg='white',command=update1).place(x=900,y=200)

#=================Deleting record from database================
def delete():
	
	top3=Toplevel()
	con=sqlite3.connect('phone.db')
	cur=con.cursor()
		
	top3.title('Delete')
	top3.geometry('1250x720')
	top3.configure(bg='black')
	l4=Label(top3,text='Delete data',bg='#242424',font=('corbel' ,20 ),fg='white',padx=100,pady=20)
	l4.pack(fill=X)
	l5=Label(top3,text='Enter mobile number',font='corbel 10', bg='#242424',fg='white')
	l5.place(x=350,y=200)
	e6=Entry(top3)
	e6.place(x=600,y=200)
	def search2():
		
	
		s6=e6.get()
	
		sql="select* from 'phonebook' where Mobile =?;"
		result=cur.execute(sql,(s6,))
		for i in result:
			n1=i[0]
			n2=i[1]
			n3=i[2]
			n4=i[3]
			n5=i[4]
		def delete1():
			res=messagebox.askyesno('Delete', 'Do you want to delete')
			if res==1:
				sql='DELETE FROM phonebook where Mobile=?;'
				cur.execute(sql,(s6,))
				messagebox.showinfo('Deleted','Record deleted successfully')
				con.commit()
			else:
				messagebox.showinfo('Not deleted','Record not deleted')
		try:
			
			Label(top3,text='First name',bg='#242424',fg='White',font='corbel 10').place(x=350,y=300)
			Label(top3,text='Last name',bg='#242424',fg='White',font='corbel 10').place(x=350,y=350)
			Label(top3,text='Address',bg='#242424',fg='White',font='corbel 10').place(x=350,y=400)
			Label(top3,text='Mobile',bg='#242424',fg='White',font='corbel 10').place(x=350,y=450)
			Label(top3,text='Pincode',bg='#242424',fg='White',font='corbel 10').place(x=350,y=500)
		
			Label(top3,text=n1,bg='#242424',fg='White',font='corbel 10').place(x=500,y=300)
			Label(top3,text=n2,bg='#242424',fg='White',font='corbel 10').place(x=500,y=350)
			Label(top3,text=n3,bg='#242424',fg='White',font='corbel 10').place(x=500,y=400)
			Label(top3,text=n4,bg='#242424',fg='White',font='corbel 10').place(x=500,y=450)
			Label(top3,text=n5,bg='#242424',fg='White',font='corbel 10').place(x=500,y=500)
			Button(top3,text='Delete',font='corbel 10',bg='#242424',fg='white',command=delete1).place(x=550,y=550)
		except UnboundLocalError as error:
			messagebox.showerror('Error','Not available in database')	
			
		
		
	Button(top3, text='Search',font='corbel 10', bg='#242424',fg='white',command=search2).place(x=900,y=200)
	
	
		

	


l2=Label(root,text='What do you want to do? ',font='corbel, 15',fg='white',bg='#242424')
l2.place(x=450,y=150)
Button(root,text='Add',font='corbel 10',fg='white',bg='#242424',command=add).place(x=600,y=300)
Button(root,text='Search',font='corbel 10',fg='white',bg='#242424',command=search).place(x=590,y=400)
Button(root,text='Update',font='corbel 10',fg='white',bg='#242424',command=update).place(x=590,y=500)
Button(root,text='Delete',font='corbel 10',fg='white',bg='#242424',command=delete).place(x=590,y=600)
l3=Label(root,text=' All rights reserved',font='corbel 15', bg='#242424',fg='white').place(x=500,y=700)

con.commit()


root.mainloop()