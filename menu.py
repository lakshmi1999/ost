from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
root=Tk()
l=Label(root,text="Press any button",font=("Arial Bold",50))
l.pack()

menu=Menu(root)
frame=Frame(root)
frame.pack()
root.config(menu=menu)
def openf():
        filedialog.askopenfilename()

def red():
	tkinter.messagebox.showinfo("RED BUTTON","Red button is clicked")
def blue():
	tkinter.messagebox.showinfo("Blue BUTTON","Blue button is clicked")
def black():
	tkinter.messagebox.showinfo("Black BUTTON","Black button is clicked")
def brown():
	tkinter.messagebox.showinfo("Brown BUTTON","Brown button is clicked")

filemenu=Menu(menu)
menu.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open',command=openf)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=root.quit)

helpmenu=Menu(menu)
menu.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About')

redbutton=Button(frame,text="RED",font=("Arial Bold",30),fg='red',command=red)
redbutton.pack(side=LEFT)
brownbutton=Button(frame,text="BROWN",font=("Arial Bold",30),fg='brown',command=brown)
brownbutton.pack(side=LEFT)
bluebutton=Button(frame,text="BLUE",font=("Arial Bold",30),fg='blue',command=blue)
bluebutton.pack(side=LEFT)
blackbutton=Button(frame,text="RED",font=("Arial Bold",30),fg='red',command=black)
blackbutton.pack(side=LEFT)

mainloop()



