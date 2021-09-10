from tkinter import *
import sqlite3

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
				con.close()
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
	