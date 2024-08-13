from sqlite3 import OperationalError
import tkinter as tk
from tkinter import *

root=tk.Tk()
root.title('CALCULATOR')
root.geometry('550x375')

#for entering consecutively in the input tbox
def num_call(num):
    current=data.get()
    data.delete(0,END)
    data.insert(0,str(current)+str(num))

#for clearing contents from the text area
def button_clear():
    data.delete(0,END)

#for producing addition operation result
def button_add():
    num1=data.get()
    global first_number
    global operation
    operation="addition"
    first_number = int(num1)
    data.delete(0,END)

#for producing subtraction operation result
def button_sub():
    num1=data.get()
    global first_number
    global operation
    operation="subtraction"
    first_number = int(num1)
    data.delete(0,END)

#for producing multiplication operation result
def button_mul():
    num1=data.get()
    global first_number
    global operation
    operation="multiplication"
    first_number = int(num1)
    data.delete(0,END)

#for producing division operation result
def button_div():
    num1=data.get()
    global first_number
    global operation
    operation="division"
    first_number = int(num1)
    data.delete(0,END)

#for producing remainder operation result
def button_mod():
    num1=data.get()
    global first_number
    global operation
    operation="remainder"
    first_number = int(num1)
    data.delete(0,END)

#for performing specific operation based on operator
def button_equal():
    num2=data.get()
    data.delete(0,END)

    if operation=="addition":
        data.insert(0, first_number + int(num2))
    
    if operation=="subttraction":
        data.insert(0, first_number - int(num2))

    if operation=="multiplication":
        data.insert(0, first_number * int(num2))

    if operation=="division":
        data.insert(0, first_number / int(num2))
     
    if operation=="remainder":
        data.insert(0, first_number % int(num2))


#button Creation
data=tk.Entry(root,width=18,justify=RIGHT,font=('Times new roman',30))

b_0=tk.Button(root,text='0',padx=36,pady=10,command=lambda:num_call(0))
b_1=tk.Button(root,text='1',padx=36,pady=10,command=lambda:num_call(1))
b_2=tk.Button(root,text='2',padx=36,pady=10,command=lambda:num_call(2))
b_3=tk.Button(root,text='3',padx=36,pady=10,command=lambda:num_call(3))
b_4=tk.Button(root,text='4',padx=36,pady=10,command=lambda:num_call(4))
b_5=tk.Button(root,text='5',padx=36,pady=10,command=lambda:num_call(5))
b_6=tk.Button(root,text='6',padx=36,pady=10,command=lambda:num_call(6))
b_7=tk.Button(root,text='7',padx=36,pady=10,command=lambda:num_call(7))
b_8=tk.Button(root,text='8',padx=36,pady=10,command=lambda:num_call(8))
b_9=tk.Button(root,text='9',padx=36,pady=10,command=lambda:num_call(9))

b_clr=tk.Button(root,text='CLEAR',padx=25,pady=10,command=button_clear)
b_add=tk.Button(root,text='+',padx=36,pady=10,command=button_add)
b_eql=tk.Button(root,text='=',padx=36,pady=10,command=button_equal)
b_sub=tk.Button(root,text='-',padx=36,pady=10,command=button_sub)
b_mul=tk.Button(root,text='*',padx=36,pady=10,command=button_mul)
b_div=tk.Button(root,text='/',padx=36,pady=10,command=button_div)
b_mod=tk.Button(root,text='%',padx=36,pady=10,command=button_mod)


#Button displaying on the main window
data.grid(row=0,column=0,columnspan=3,padx=20,pady=20)
b_eql.grid(row=0,column=3)

b_7.grid(row=1,column=0,padx=10,pady=10)
b_8.grid(row=1,column=1,padx=10,pady=10)
b_9.grid(row=1,column=2,padx=10,pady=10)
b_add.grid(row=1,column=3,padx=10,pady=10)

b_4.grid(row=2,column=0,padx=10,pady=10)
b_5.grid(row=2,column=1,padx=10,pady=10)
b_6.grid(row=2,column=2,padx=10,pady=10)
b_sub.grid(row=2,column=3,padx=10,pady=10)

b_1.grid(row=3,column=0,padx=10,pady=10)
b_2.grid(row=3,column=1,padx=10,pady=10)
b_3.grid(row=3,column=2,padx=10,pady=10)
b_mul.grid(row=3,column=3,padx=10,pady=10)

b_mod.grid(row=4,column=0,padx=10,pady=10)
b_0.grid(row=4,column=1,padx=10,pady=10)
b_clr.grid(row=4,column=2,padx=10,pady=10)
b_div.grid(row=4,column=3,padx=10,pady=10)

#mainloop
root.mainloop()