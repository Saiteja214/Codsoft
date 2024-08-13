"""Creating a Random Password Generator
    instead of using imported modules from string library, we use ascii values
    ascii(American Standard Code for INformation Interchange) values are from 0 - 127
    1. 0 - 32 : we have some characters which can't be used in generating a password 
    2. 33-126 : contains upper-case letters, lower-case letters, digits,special characters
    3.127: DEL character which we won't use in generating a password"""

# For a basic strong password the minimum required length is of 8 characters

from tkinter import *  #tkinter for basic GUI for taking input and generating password which allows users to copy it to clipboard
import tkinter as tk  # tk for positioning of widgets on the window
from tkinter import messagebox  #an alert box pops-up when user input for password length is lessthan 8
from random import randint   # for generating random integer form ascci range of 33 - 126

root=tk.Tk()
root.title('Password Generator') # title for th window 
root.geometry('450x300')  # basic size of window which can be resized while using


# for generating a random password
def rand_pass():
    pwd.delete(0,END)                   #clearing the password label for every user input for length 
    pass_length=int(pass_entry.get())   # input for password length
    if pass_length<8:                   # an alert box pops-up if length is less than 8
        messagebox.showerror("Password is too Short","should be minimum of 8 Characters") 
    else:                              
        my_pass=''
        for i in range(pass_length):
            my_pass+=chr(randint(33,126))  # else random ascii values are generated and are converted to characters 
m,dY7CJ#yw

    pwd.insert(0,my_pass)  #inserting the generated password

#for copying the password to the clipboard
def clip_brd():
    root.clipboard_clear()  # clearing the clipboard
    root.clipboard_append(pwd.get()) #appending the genertaed password to the clipboard

#label for frame for entering the length of password 
label_frame=LabelFrame(root,text='Length of Password')
label_frame.pack(pady=30) #label positioning 

#Entery label for password length
pass_entry=Entry(label_frame,font=('Times New Roman',18))
pass_entry.pack(pady=20,padx=20) # entry box positiong to the frame 

#for showing the generated password based on calculation from ascii values
pwd=Entry(root,font=("Times New Roman ",18))
pwd.pack(pady=20)  # positioning of password label


# for fixing buttons on the frame
frm=Frame(root)
frm.pack(pady=20)  # button positioning from labels

#button for Generating password , upon clicking generate password rand_pass wil be called
btn=Button(frm,text='Generate Password',command=rand_pass)
btn.grid(row=0,column=0,padx=10)  # positioning of button-Generate Password

#Button allows user to copy the generated password to the clipboard , upon clicking Copy To clipboard clip_brd will be called
clip=Button(frm,text='Copy To Clipboard',command=clip_brd)
clip.grid(row=0,column=1,padx=10)  # positioning of button-Copy To Clipboard

root.mainloop()