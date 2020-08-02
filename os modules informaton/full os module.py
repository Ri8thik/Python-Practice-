import os
import shutil
# 1) to print the path of witch the file is presen 

#print(os.getcwd())

# 2) to make the directery we use it but if the directry is already is presemt than it display error

#os.mkdir("rs")

#  3) to check whether the file is present or not

#print(os.path.exists("rs")) # to print the output we use the print method and it print the true or false value


#  4) if we want to check whether the file is present or not and if not present than make the file :----

"""
if os.path.exists("music"):
        print("file already present")
else:
        os.mkdir("music")


#  5) to open the file we use it 
open('file.txt','a').close()

 #  6) if we want to change the directery
 # one metthod
 
# os.mkdir(r"F:\rithik\work\jaadu")
# second method
# we can change the dirctery by using this method

os.chdir(r"F:\rithik\work")
os.mkdir("jaadu")




  #  7) if we want to check the list of the given folder than we use this method
  
print(os.listdir())


# supose if we want to find the list list of some different folder than we use the two method
# i) first we can chande the directery by this method


os.chdir(r"F:\rithik\work")

print(os.listdir())


 # ii) second we can define the path of the given file which we can find the the list
 
print(os.listdir(r"F:\rithik\work"))


 #  8) if we want to  find the list of element present in the file with there path also than we use this
for i in os.listdir():
        path = os.path.join(os.getcwd(),i)
        print(path)

# if we want to find the path of different folder than we give the path to listdir() and change os.getcwd to given path
for i in os.listdir(r"F:\rithik\work\python"):
        path =os.path.join(r"F:\rithik\work\python",i)
        print(i)





#  9) if we want to check the folders of the given folder in depth so we use this
# we can also check the folders of subfolder

os.chdir(r"F:\rithik\work") # here we change the dirctery to the specific one 

file= os.walk(r"F:\rithik\work") #here we use the wolk funtion to walk on the all folders it gives us three output s

for current_path, folder_names, file_name in file: # here we use the fore loop for the file 
        print(f"current path:{current_path}")
        print(f"folder_names:{folder_names}")
        print(f"file_names:{file_name}")





  # 10) to delete the file

os.rmdir("file name")

  # 11) to make the sub-folders
os.makedirs("new/new1")


# 12) to delete the folder when it is not empty we use shutil module to done this
shutil.rmtree('new')
# note it will does not send the file to recycle bin it permanently delete the file (shutil function)


# 13) to copy the one folder and paste to another folder

shutil.copytree("music",'rr/music33')

# 14) to copy the file and paste to another folder

shutil.copy("file.txt",'rr/file.txt')


# 15) to move the file and paste to another folder
shutil.move("file.txt",'rr/file22.txt')
"""
# 15) to move the file and paste to another folder


shutil.move("music",'rr/new2')















