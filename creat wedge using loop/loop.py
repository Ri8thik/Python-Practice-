import tkinter as tk
from tkinter import ttk
root=tk.Tk()
# A) labels
#here we create a labels using loop method
# first we amke a list in which all the labels are present
labels=["user name :-","user email :-","age:-","gender:-",'state:-',"city:-"]
#start a for loop so that it print all the labels which are given in above list:-
for i in range(len(labels)):
        # this print the labe[0] which means a current label
        cur_label="label" +str(i)
        # here we start a simple method in which  we create a label
        cur_label=tk.Label(root,text=labels[i])
        # here we use the padding padx is use for left and right , pady is used for top and bottom 
        cur_label.grid(row=i,column=0,sticky=tk.W, padx=2, pady=2)

# B) Entry box
# to create a loop for entry bos so that it print many entry
#first we create a dictunary in which we store the variable ,and that variable will store the data of the current entry
user_info={
        'name': tk.StringVar(),
        "email" :tk.StringVar(),
        "age" :tk.StringVar(),
        "gender" : tk.StringVar(),
        "state" : tk.StringVar(),
        "city" : tk.StringVar()
        }
#here is the counter variable which increases the value of row as the loop start
counter =0
#here is the loop 
for i in user_info:
        #this print the first entry[i] or current entry[i]
        cur_entry='entry' + i
        # here is the simple methoid to create  a entry and in textvariable we create a dictonaray user_info
        cur_entry=tk.Entry(root,width=16,textvariable=user_info[i])
        # here we use the padding padx is use for left and right , pady is used for top and bottom 
        cur_entry.grid(row=counter,column=1,padx=2, pady=2)
        # here the counter increment the valuye 
        counter+=1


def submit():
        
        print("user_name is :- " +user_info['name'].get())
        print("user_email is :- " +user_info['email'].get())
        print("user_age is :- " +user_info['age'].get())
        print("gender :- " +user_info['gender'].get())
        print("state :- " +user_info['state'].get())
        print("city :- " +user_info['city'].get())
        
submit_btn =ttk.Button(root,text='submit',command=submit)
submit_btn.grid(row=6,columnspan=2)
        
root.mainloop()
