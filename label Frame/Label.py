import tkinter as tk
from tkinter import ttk
root=tk.Tk()
root.title("LAbel_Frame")
label_frame=ttk.LabelFrame(root,text="enter your detail below")
label_frame.grid(row=0,column=0,padx=40)

labels=["user name :-","user email :-","age:-","gender:-",'state:-',"city:-"]

for i in range(len(labels)):
        cur_label="label" +str(i)
        cur_label=tk.Label(label_frame,text=labels[i])
        # here we use the padding padx is use for left and right , pady is used for top and bottom 
        cur_label.grid(row=i,column=0,sticky=tk.W)


user_info={
        'name': tk.StringVar(),
        "email" :tk.StringVar(),
        "age" :tk.StringVar(),
        "gender" : tk.StringVar(),
        "state" : tk.StringVar(),
        "city" : tk.StringVar()
        }

counter =0
 
for i in user_info:
        cur_entry='entry' + i
        cur_entry=tk.Entry(label_frame,width=16,textvariable=user_info[i])
        # here we use the padding padx is use for left and right , pady is used for top and bottom 
        cur_entry.grid(row=counter,column=1)
        counter+=1


def submit():
        
        print("user_name is :- " +user_info['name'].get())
        print("user_email is :- " +user_info['email'].get())
        print("user_age is :- " +user_info['age'].get())
        print("gender :- " +user_info['gender'].get())
        print("state :- " +user_info['state'].get())
        print("city :- " +user_info['city'].get())
        
submit_btn =ttk.Button(root,text='submit',command=submit)
submit_btn.grid(row=1,columnspan=2)
        
#this is a for loop which create the padding effect in the label_frame in this methiod we does not  define the padding in each lable and entrys
for child in label_frame.winfo_children():
        child.grid_configure(padx=4,pady=8)


        
root.mainloop()
