import tkinter as tk
from tkinter import ttk
root=tk.Tk()
root.title("menubar")

def func():

        print("funtion called")

# now we create a menu bar ok
#use the class Menu and add that to the variable main_menu
main_menu =tk.Menu(root)
#bow creat a sub menu of the following menu
# here i make a file menu
#create a variable file_menu and add menu(main_manu)
# to remove the line which cut the box use tearoff =0 
file_menu=tk.Menu(main_menu, tearoff=0)
# now add the lables to the file  menu and for action use command and we make a funtion (func) above it 
file_menu.add_command(label="New file",command=func)
file_menu.add_command(label="new window",command=func)
# to create a line in the submenu
file_menu.add_separator()
file_menu.add_command(label="save file",command=func)

# here we create a edit_ menu in main menu

edit_menu=tk.Menu(main_menu,tearoff=0)
edit_menu.add_command(label="undo",command=func)
edit_menu.add_command(label="edit",command=func)
# now cascade the both file and edit menu in the main_menu
main_menu.add_cascade(label="file",menu=file_menu)
main_menu.add_cascade(label="edit",menu=edit_menu)

root.config(menu=main_menu)
root.mainloop()
