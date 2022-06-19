from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk()
GUI.title('โปรแกรมคำนวณราคาปลา')
GUI.geometry('700x600')

L = ttk.Label(GUI, text='กรุณากรอกจำนวนปลา', font=(None, 20)).pack()

bg = PhotoImage(file='car1.png')
BG = Label(GUI, image=bg).pack()

v_quantity = StringVar()
v_quantity.set('1')
E1 = ttk.Entry(GUI, textvariable=v_quantity, font=(None, 30), justify='right')
E1.pack(pady=10)
E1.focus()

def Cal(event=None):
	try:
		quan = float(v_quantity.get())
		fish_price = 39
		calc = quan*fish_price
		messagebox.showinfo('ราคาท้้งหมด', 'ราคาปลาทั้งหมด {} บาท'.format(calc))
		v_quantity.set('1')
		E1.focus()
	except:
		messagebox.showwarning('กรอกผิด', 'กรุณากรอกเฉพาะตัวเลขเท่านั้น')
		v_quantity.set('1')
		E1.focus()

B = ttk.Button(GUI, text='Calculate', command=Cal)
B.pack(ipadx=30, ipady=20, pady=10)

E1.bind('<Return>', Cal)

GUI.mainloop()