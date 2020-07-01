from tkinter import *

root = Tk()

e = Entry(root, width = 40, borderwidth = 4)
e.grid(row = 0, column = 4)
e.insert(0,'enter your name :')


def myclick():

	myLabel = Label(root, text ='hello' + e.get())
	myLabel.grid(row =0,column=3)

# creating a label widgit
myLabel1 = Label(root, text = 'Hello World')

myLabel2 = Label(root, text = 'my name is yogesh shahi')

myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=0)

MyButton = Button(root, text = 'click me', command = myclick)

MyButton.grid(row=0,column=1)

root.mainloop()