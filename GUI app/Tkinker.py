                               #THIS IS A STARTINTG CODE
                      # THIS THREE LINES ARE IMPORTANT AND USED IN ALL THE GUI APPLICATION

#import tkinter # this  module is used to make the GUI app
#ANOTHER METHOD IS ALSO USED TO IMPORT THE TKINTER MODEUL AND WE CAN PREFER IT AS A BEST
import tkinter as tk # NOW IN THIS WAY WE CAN USE THE "TK " INSTAD OF TKINTER
from tkinter import ttk #this ttk is the file in which all thge button switch are availabe 
from csv import DictWriter
import os
root =tk.Tk() #here root is the name of the variable 
root.title('GUI Application') #in this method we can change title


#ALL THE LABELS AND BUTTON , RADIOBUTTON -ARE AVAILABLE IN ---TK AS WELL AS TKK
#1) first lable now here we display this and to set the position we use two method
                        # I) pack() this methos id used and the text is in the  center
                        # 2) grid() this methiod is used and we can define the row nad column so that we can set the position of the lable
        # A)  here we can create a variable name "new_Label" and we can make the label abd store in it
name_label=ttk.Label(root, text="enter your name :-")
        # we can make this grid method in same line as well but to explain user we did it 
name_label.grid(row=0,column=0,sticky=tk.W)





        # B) here we craete a another lable to set the email

email_label=ttk.Label(root,text="enter your email :-")
email_label.grid(row=1,column=0,sticky=tk.W)


        # c) here we craete a another lable to set the age 
age_label=ttk.Label(root,text ="enter your age :-")
        #now we can notice that the age line is slightly forward so we use the stick.tk=W to stick that line 
age_label.grid(row=2,column=0,sticky=tk.W)



        # d) here we create a gender lable and for this we create a combobox
        
gender_label=ttk.Label(root,text ="select your gender :-")
        #now we can notice that the age line is slightly forward so we use the stick.tk=W to stick that line 
gender_label.grid(row=3,column=0,sticky=tk.W)



# NOW TO GET THE INPUT FROM THE USER WE WANT THE BOX
#2) CREATE A ENTRY BOX

        # a) so we have create a entry_box for the name
        # here we create the variable name_var to store the data give by the  user 
name_var =tk.StringVar()
        #here textvariable is used to store the  given data  which is given by the user to the name_var
name_entrybox=ttk.Entry(root,width=16 ,textvariable =name_var)
        # to set the loaction 
name_entrybox.grid(row=0,column=1)
        # to set the curser bydefalt in the name entrybox we use this 
name_entrybox.focus()





        #b) email
email_var =tk.StringVar()
email_entrybox=ttk.Entry(root,width=16 ,textvariable =email_var)
        # to set the loaction 
email_entrybox.grid(row=1,column=1)


        #c) age
age_var =tk.StringVar()
age_entrybox=ttk.Entry(root,width=16 ,textvariable =age_var)
        # to set the loaction 
age_entrybox.grid(row=2,column=1)



# 3) combobox create
        #here vwe create a gender_var to store the data 
gender_var=tk.StringVar()
        #here the gender_combobox is create , textvariable is used to store the data in gender_var variable and state ="readonly" means that the user could'nt type in it
gender_combobox=ttk.Combobox(root,width=16,textvariable=gender_var,state="readonly")
        # to set the values we use this so that user can set the one of the given value
gender_combobox['value']=('male','femail','other')
        # this tage is used to set the diffalt value as a male in the gender_combobox
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1)


# 4) radio button
        #a) first button
        #first make a variable which store the data given by the user 
user_type=tk.StringVar()
        #Radiobutton create a radio button and here we does not type variable here only variable becouse we want to selct the radio and store it in the user_type
radiobtn1=ttk.Radiobutton(root,text='student',value='student',variable=user_type)
radiobtn1.grid(row=4,column=0)
       
#here we make only one user_type variable so that user can select the data we gi9ve only one


        #b) second
radiobtn2=ttk.Radiobutton(root,text='teacher',value='teacher',variable=user_type)
radiobtn2.grid(row=4,column=1)


        #c) third
radiobtn3=ttk.Radiobutton(root,text='hod',value='hod',variable=user_type)
radiobtn3.grid(row=4,column=2)




# 5) check button
        # this is a check button which gives two value 1 or 0  , 1 means true and 0 means false
        # first create a variable "checkbtn_var" it store the int value so type "tk.Intvar()"
checkbtn_var= tk.IntVar()
        #here Checkbutton create a button and valiable is to store the data in checkbtn_var
checkbtn=ttk.Checkbutton(root,text="subscribe ower youtube channel" ,variable=checkbtn_var)
        # here column is used becouse if we does not use it it effect the above lines 
checkbtn.grid(row=5 ,columnspan=3,sticky=tk.W)



#6) create button
        # to craete a submit button we use the ttk.Button and to get that values to the user than use "command=action" and make the action name constructer and store the name,age,email values by usingname_var.get()
        #this is the action constructer
def action():
                #here we store the data in the username,userage,useremail variable  
        username=name_var.get()
        useremail=email_var.get()
        userage=age_var.get()
        #and print it 
        print(f'{username} is {userage} years old,email is {useremail}')
        #here we store the data more
        usergender=gender_var.get()
        usertype=user_type.get()
        # here if statement is run if 0 than no otherwise yes
        if checkbtn_var.get()==0:
                subscribed='NO'
        else:
                subscribed="yes"
                # print that all
        print(usergender,usertype,subscribed)
        # to store the data in the file we use the with open method and print data
        # 1) to store the data in text file 
        #  2) to store the data in csv file i write the data in at the last of the page 
        with open('file.txt','a') as f:
                f.write(f'{username},{useremail},{userage},{usergender},{usertype},{subscribed}\n')
                
        # if we want to set that is the user type the submit button than all the type data will errase from the app
        #use this|
        name_entrybox.delete(0, tk.END)
        email_entrybox.delete(0, tk.END)
        age_entrybox.delete(0, tk.END)
        # in this way we can change the colour of the button
        submit_button.configure(foreground='#b388ff')


        
        #this is actualy a submit buttion 
submit_button= tk.Button(root,text='Submit',command=action) # here we call the command =action and  the above constructe will call and store the usser data
submit_button.grid(row=6,column=0)

root.mainloop() # this is a main loop which run the program till the user dot cut that




"""
       with open('file.csv','a') as f:
                dict_writer=DictWriter(f,fieldnames=['username','useremail','userage','usergender','usertype','subscribed'])
                if os.stat('file.csv').st_size==0:
                        
                        dict_writer.writeheader()
                        
                dict_writer.writerow({
                        'username': username,
                        "useremail": useremail,
                        "userage": userage,
                        "usergender": usergender,
                        "usertype": usertype,
                        "subscribed": subscribed

                })


                """
