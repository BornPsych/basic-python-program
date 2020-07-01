from tkinter import *

root = Tk()

root.title('Simple Calculator')

InputBox = Entry(root, width= 40 , borderwidth = 4)

InputBox.grid(row =0 , column= 0, columnspan = 3, padx = 10,pady=10)

def get_text(number):
	current = InputBox.get()

	InputBox.delete(0,END)
	InputBox.insert(0,str(current) + str(number))

def get_clear():

	InputBox.delete(0,END)

def get_add():
	
	global first_number

	global math

	math = "addition"

	first_number = int(InputBox.get())

	InputBox.delete(0,END)

def get_subtract():
	
	global first_number

	first_number = int(InputBox.get())


	global math
	math = " subtraction"

	InputBox.delete(0,END)

def get_multiply():
	
	global first_number

	first_number = int(InputBox.get())

	global math
	math = "multiplication"

	InputBox.delete(0,END)

def get_divide():
	
	global first_number

	global math
	math = "division"

	first_number = int(InputBox.get())

	InputBox.delete(0,END)

def get_equal():

	second_number = int(InputBox.get())

	InputBox.delete(0,END)

	if math == "addition":
		InputBox.insert(0,first_number+second_number)

	elif math== "subtraction":
		InputBox.insert(0,first_number-second_number)

	elif math== "multiplication":
		InputBox.insert(0,first_number*second_number)

	elif math== "division":
		InputBox.insert(0,first_number/second_number)

button_1 = Button(root, text = '1',padx = 20, pady = 20 , command = lambda: get_text(1))
button_2 = Button(root, text = '2',padx = 20, pady = 20 , command = lambda: get_text(2))
button_3 = Button(root, text = '3',padx = 20, pady = 20 , command = lambda: get_text(3))
button_4 = Button(root, text = '4',padx = 20, pady = 20 , command = lambda: get_text(4))
button_5 = Button(root, text = '5',padx = 20, pady = 20 , command = lambda: get_text(5))
button_6 = Button(root, text = '6',padx = 20, pady = 20 , command = lambda: get_text(6))
button_7 = Button(root, text = '7',padx = 20, pady = 20 , command = lambda: get_text(7))
button_8 = Button(root, text = '8',padx = 20, pady = 20 , command = lambda: get_text(8))
button_9 = Button(root, text = '9',padx = 20, pady = 20 , command = lambda: get_text(9))
button_0 = Button(root, text = '0',padx = 20, pady = 20 , command = lambda: get_text(0))

button_add = Button(root, text = '+',padx = 20, pady = 20 , command = get_add)
button_subrtact = Button(root, text = '-',padx = 20, pady = 20 , command = get_subtract)
button_multiply = Button(root, text = '*',padx = 20, pady = 20 , command = get_multiply)
button_divide = Button(root, text = '/',padx = 20, pady = 20 , command = get_divide)

button_equal = Button(root, text = '=',padx = 20, pady = 20 , command = get_equal)
button_clear = Button(root, text = 'clear',padx = 40, pady = 20 , command = get_clear)

button_quit = Button(root, text= " quit", padx=20, pady=20, command = root.quit)
button_1.grid(row =1,column=0)

button_2.grid(row =1,column=1)

button_3.grid(row =1,column=2)

button_4.grid(row =2,column=0)

button_5.grid(row =2,column=1)

button_6.grid(row =2,column=2)

button_7.grid(row =3,column=0)

button_8.grid(row =3,column=1)

button_9.grid(row =3,column=2)

button_0.grid(row =4,column=1)

button_add.grid(row =4,column=0)

button_subrtact.grid(row =6,column=0)

button_multiply.grid(row =6,column=1)

button_divide.grid(row =6,column=2)

button_equal.grid(row =4,column=2)

button_clear.grid(row =5,column=0)

button_quit.grid(row=5,column =2)


root.mainloop()