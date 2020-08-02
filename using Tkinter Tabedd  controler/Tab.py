import tkinter as tk
from tkinter import ttk
root=tk.Tk()
root.title("TAB control")
# to create a TAb menu we wabt to create a notebook
# here we store the data in nb variable 
nb =ttk.Notebook(root)
# after that create how much tab you want to creat
#here we create a page1
page1=ttk.Frame(nb)
#here we create a page2 
page2=ttk.Frame(nb)
# now we add that pages to the notebook by adding in the variable "nb" , if we want to add some text on that tab we can add it
nb.add(page1,text="ONE")
nb.add(page2,text="TWO")
#here we do not use the grid method becouse it does not give us the hole page
# so we use pack method and expand=true and fill =both side virtical as well as horizontal
nb.pack(expand=True,fill="both")
#nb.grid(row=0,column=0)

# now add some labels to the page1
Label1=ttk.Label(page1,text="this is lagel")
Label1.grid(row=0,column=0)

# entry also
entry1= ttk.Entry(page1,width=16)
entry1.grid(row=0,column=1)

#here we create lables foe page 2
Label2=ttk.Label(page2,text="this is lagel 2")
Label2.grid(row=0,column=0)
entry2= ttk.Entry(page2,width=16)
entry2.grid(row=0,column=1)



root.mainloop()
