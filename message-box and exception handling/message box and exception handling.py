# in this we use the exception handling and make a message box
import tkinter as tk
from tkinter import ttk
#message box was present in tkinter so we import messagebox from it as a m_box
from tkinter import messagebox as m_box
root=tk.Tk()

#simply make a fram in which we make a label and entry box
label_frame=ttk.LabelFrame(root,text="Contact Detail")
label_frame.grid(row=0,column=0,padx=40,pady=10)

#now make a lable for name and for age

name_label=ttk.Label(label_frame,text="Enter your Name Please :- ")
age_label=ttk.Label(label_frame,text="Enter your age please :-")

#here we create a variable in which we store the data of entry box 
name_var= tk.StringVar()
age_var= tk.StringVar()

#here we create a entry box for name and age
name_entry= ttk.Entry(label_frame,width=36,textvariable=name_var)
age_entry= ttk.Entry(label_frame,width=36,textvariable=age_var)

# here we use the grid and padding also 
name_label.grid(row=0,column=0,padx=5,pady=5,sticky=tk.W)
age_label.grid(row=0,column=1,padx=5,pady=5,sticky=tk.W)
name_entry.grid(row=1,column=0,padx=5,pady=5,sticky=tk.W)
age_entry.grid(row=1,column=1,padx=5,pady=5,sticky=tk.W)

#now the funtion is called

def submit():
        # m_box.showinfo("title","content")
        # first we get the data of name and age 
        name=name_var.get()
        age=age_var.get()
        # now we start a loop in which is the user does not enter the name or the age than it show the error that pls enter both name and age
        if name=="" or age =="":
               m_box.showerror('error','please enter both name and age')
        #else condition run 
        else:
                # now if the user enter the value in both section buit does not put the int value in box than we display an error that pls enter valid age 
                try:
                        #here we check whether the value is int or not
                        age=int(age)
                        # it its int it display the value 
                #if it is not int than it start exception block
                except ValueError:
                        #here it display the error that pls enter valid age
                        m_box.showerror("error","pls enter valid age")
                # now if we want to know about if thew user is above the 18 or not  
                else:
                        #here is the condition
                        if age < 18:
                                m_box.showwarning('error','you are not 18+')
                        print(f'{name}:{age}')

# here we creat a button which call submit function
submit_btn=ttk.Button(root,text="submit",command = submit)
submit_btn.grid(row=1,columnspan=2,padx=40)

root.mainloop()


# MESSAGE BOX INFORMATION
# 1) there are three comman message box appear info, error and warning
# m_box.showerror("error","pls enter both name and age" )












































