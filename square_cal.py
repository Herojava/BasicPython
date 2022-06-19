from tkinter import *
from tkinter import ttk, messagebox
import datetime

GUI = Tk()
GUI.title('Square Area Calculator')
GUI.geometry('600x600')

F1 = ttk.Frame(GUI)
F1.pack(pady=5)

L = ttk.Label(F1, text='Square Area Calculator', font=(None, 20)).pack()
img = PhotoImage(file='square.png')
IMG = Label(F1, image=img).pack()

F2 = ttk.Frame(GUI)
F2.pack(pady=5)

L1 = ttk.Label(F2, text='WIDE (meter) ::', font=(None, 20)).grid(row=0, column=0)
L2 = ttk.Label(F2, text='LONG (meter) ::', font=(None, 20)).grid(row=1, column=0)

v_wide = StringVar()
v_long = StringVar()

v_wide.set('0')
v_long.set('0')

E1 = ttk.Entry(F2, textvariable=v_wide, justify='right', font=(None, 20))
E1.grid(row=0, column=1)
E2 = ttk.Entry(F2, textvariable=v_long, justify='right', font=(None, 20))
E2.grid(row=1, column=1)

def Cal():
	try:
		if float(v_long.get()) and float(v_wide.get()) > 0:
			try:
				square_area = float(v_wide.get()) * float(v_long.get())
				messagebox.showinfo('Square Area', 'Wide : {} meter & Long : {} meter >>> Area : {} square meter'.format(v_wide.get(), v_long.get(), square_area))
				v_wide.set('0')
				v_long.set('0')
			except:
				messagebox.showwarning('Error', 'Please input only number!!!')
				v_wide.set('0')
				v_long.set('0')
		else:
			messagebox.showwarning('Zero', 'Please input the number of wide and long!!!')
	except:
		messagebox.showwarning('Error', 'Please input only number!!!')
		v_wide.set('0')
		v_long.set('0')

def Enter_Action_E1(event=None):
	try:
		if float(v_long.get()) and float(v_wide.get()) > 0:
			try:
				square_area = float(v_wide.get()) * float(v_long.get())
				messagebox.showinfo('Square Area', 'Wide : {} meter & Long : {} meter >>> Area : {} square meter'.format(v_wide.get(), v_long.get(), square_area))
				v_wide.set('0')
				v_long.set('0')
			except:
				messagebox.showwarning('Error', 'Please input only number!!!')
				v_wide.set('0')
				v_long.set('0')
		elif float(v_long.get()) == 0:
			E2.focus()
		# elif float(v_long.get()) == 0:
		# 	E1.focus()
		else:
			messagebox.showwarning('Error', 'Please input only number!!!')
			v_wide.set('0')
			v_long.set('0')
	except:
			messagebox.showwarning('Error', 'Please input only number!!!')
			v_wide.set('0')
			v_long.set('0')

def Enter_Action_E2(event=None):
	try:
		if float(v_long.get()) and float(v_wide.get()) > 0:
			try:
				square_area = float(v_wide.get()) * float(v_long.get())
				messagebox.showinfo('Square Area', 'Wide : {} meter & Long : {} meter >>> Area : {} square meter'.format(v_wide.get(), v_long.get(), square_area))
				v_wide.set('0')
				v_long.set('0')
			except:
				messagebox.showwarning('Error', 'Please input only number!!!')
				v_wide.set('0')
				v_long.set('0')
		# elif float(v_wide.get()) == 0:
		# 	E2.focus()
		elif float(v_wide.get()) == 0:
			E1.focus()
		else:
			messagebox.showwarning('Error', 'Please input only number!!!')
			v_wide.set('0')
			v_long.set('0')
	except:
		messagebox.showwarning('Error', 'Please input only number!!!')
		v_wide.set('0')
		v_long.set('0')


B = ttk.Button(GUI, text='Calculate', command=Cal)
B.pack(pady=10, ipady=20, ipadx=20)

E1.focus()
E1.bind('<Return>', Enter_Action_E1)
E2.bind('<Return>', Enter_Action_E2)



GUI.mainloop()