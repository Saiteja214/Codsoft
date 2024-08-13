"""     To-Do List is used add tasks which has to be completed 
        A simple and friendly TO-DO list interface iis developed using tkinter
        Here we can add,delete, cross,uncross tasks and crossed tasks can also be deleted       """


from tkinter import *           # tkinter for basic GUI 
from tkinter.font import Font   # for creating separate font for tasks to be added

root=Tk()
root.title('To Do List ')
root.geometry('450x450')

#defining font for tasks
my_font=Font(
    family="Imprint MT shadow",
    size=25,
    weight="bold")

#creating frame
my_frame=Frame(root)  
my_frame.pack(pady=15)

#creating List box for positioning tasks
my_list=Listbox(my_frame,font=my_font,width=25,height=5,bg="SystemButtonFace",bd=0,fg="Black",highlightthickness=0,selectbackground="blue",activestyle="dotbox")
my_list.pack(side=LEFT,fill=BOTH)

#adding scrollbar for adding multiple items
my_scrollbar=Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT,fill=BOTH)

my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

#entry box adding tasks to the to-do list
my_entry=Entry(root,font=("Georgia",25))
my_entry.pack(pady=20)

# creating functions 

def delete_item():          # used to delete selected item
    my_list.delete(ANCHOR)  # ANCHOR -  item is selected by mouse click

def add_item():             # for adding new tasks to the list   
    my_list.insert(END,my_entry.get())
    my_entry.delete(0,END)

def cross_off_item():       # cross the tasks in the list if accomplished
    my_list.itemconfig(my_list.curselection(),fg="red")
    my_list.selection_clear(0,END)

def uncross_item():         # Uncross the tasks if they crossed by-mistake or if they are not yet accomplished
    my_list.itemconfig(my_list.curselection(),fg="green")
    my_list.selection_clear(0,END)

def delete_cross():         # remove the crossed tasks if they are accomplished and no longer wanted to see in the To-Do list
    count=0
    while count<my_list.size():
        if my_list.itemcget(count,"fg")=="red":
            my_list.delete(my_list.index(count))
        count+=1

def clear_list():           # Clear the whole task-list 
    my_list.delete(0,END)


#button frames 
button_frame=Frame(root)
button_frame.pack(pady=20)

#Buttons and their functioning
delete_button=Button(button_frame,text="DELETE",command=delete_item)
add_button=Button(button_frame,text="ADD",command=add_item)
crossoff_button=Button(button_frame,text="CROSS OFF",fg="red",command=cross_off_item)
uncross_button=Button(button_frame,text="UNCROSS ",fg="green",command=uncross_item)
delete_cross_item=Button(button_frame,text="Delete Cross Item",command=delete_cross)
clear_item_button=Button(button_frame,text="Clear List",command=clear_list)

#Positioning buttons on the frame
delete_button.grid(row=0,column=0)
add_button.grid(row=0,column=1,padx=25)
crossoff_button.grid(row=0,column=2,padx=25)
uncross_button.grid(row=0,column=3)
delete_cross_item.grid(row=2,column=0,columnspan=2,pady=15,padx=20)
clear_item_button.grid(row=2 ,column=2,columnspan=2,padx=50)

#start the mainloop
root.mainloop()