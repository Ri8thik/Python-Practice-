"""
print("this is \\\\ double backslash")
print("this is /\\/\\/\\/\\/\\ mountain")
print("he is \t awesome (use escape of )")
print("\\\" \\n\\t \\'")
a=4
b=3
c=a*b
print("the total is " + str(c))

--------------------------------------------------------------------------------------------------
a=56
b=55

print(a+b) #addition
print(a-b) # subtration
print(a*b) # multiplication
print(a/b) #float division4
print(a//b) #int division5
print(a**b) #to find the power
print(a**.5) # to find the under root use .5
print(round(a**.5 ,4)) # to find the root upto the given digits
print(a%b) # to find the remainder
print((4*3+2)*4*(5+3*6)/4*3**2) # to solve this
-------------------------------------------------------------------------------------------


                                                                   CH ---2

# VARIABLES

name = "rithilk"
print(name)
age = 56
print(age)
name = "ankush" # python is a dynamic programing language becouse it can change its value 
print(name) # name variable can be use in many time .....
  # CONDITIONS  OF VARIABLES :-
  
  # variable can not be started from no  for ex (1num)
  #no special symbols are used in this language
  
print("hii")
--------------------------------------------------------------------------------------------

#STRING AND USER INPUT

name = input("enter your name ")
print("your name is " + name )
age= input("enter your age ")
print("your age is :-" +age )

# USER INPUT

a = int(input("enter your no "))
b= int(input("enter your 2 no:- "))
c= a+b
print("total is " + str(c))

# MULTIPLES VARIABLES IN  SAME LINE:-
name , age = input("enter your name "), int(input("your age :- "))
print("hello " + name +"  "+ "your age is :-" + str(age))

# MULTIPLE VARIABLES IN SINGLE INPUT

name ,age, standard , section, rollno = input("enter your details:-").split()
print("your name is :-"+name +"\n""your age is :-"+age +"\n""your standard is :-"+standard+"\n""your section is :-"+section+"\n""your roll no is :-"+rollno)


--------------------------------------------------------------------------------------------------------


# STRING FORMATING:-
name ="rithik"
rollno = 33
print("hello {} your rollno is {}".format(name , rollno)) # in this we do not have to mention the string type



# EXERCISE

no1 , no2 ,no3 =input("enter three no:-").split()
d= (int(no1)+int(no2)+int(no3))/3
print(d)

# another method

no1 ,no2,no3= input("enter three no:-").split()
print("your average is {}".format((int(no1)+int(no2)+int(no3))/3))




----------------------------------------------------------------------------------------------------------------------------------------------------

# STRING INDEXING
language = "python"


#position (index no )

# p = 0
# y=  1
# t=  2
# h=  3
# o=  4
# n=  5
print(language[5])


#STRING SLICING

language ="python"
# print(language[start agrument : stop argument-1])
print(language[0:6])



# STEP ARGUMENT
print("language"[0:6:2])# to skip the next element we have to add the step argument

# to reverse the string we use step argument:-

print("language"[::-1])



-------------------------------------------------------------------------------------------------
# to ask the user and print back user name in reverse order.



name = input("enter your name:-")
print("your name is {}".format(name[::-1]))


#ANOTHER METHOD

name = input("enter your name:-")
print(name[::-1])




-------------------------------------------------------------------------------------------------

# STRING METHOD 1

#1 len() funtion

print(len("rithik soun"))

#or
rs= "rithik soun"
print(len(rs))

#or
rs = "rithik soun"
rr = len(rs)
print(rr)


# 2 lower() method  (to change the all alphabets in lower order)

print("rIThIK SOUn".lower())



# 3  upper() method  (to change the all alphabets in upper order)

print("rIThIK SOUn".upper())

# 4 title() method

print("rIThIK SOUn".title())


# 5 count() method (to check the no of times the alphabets occur)

print("rIThIK SOUn".count("r"))


-----------------------------------------------------------------------------------

# print the name and character and count the no of alphabets :-


name , ch = input("enter your name and character :-").split(",")
print(len(name), name.count(ch))





# or 


name , ch = input("enter your name and character :-").split(",")
print("your length is:- {}".format((len(name))),"your character:- {}".format(name.count(ch)))
     

#or if the cases are sensative


name , ch = input("enter your name and character :-").split(",")

print("your length is:- {}".format((len(name))),"your character:- {}".format(name.lower().count(ch.lower()))     )





#STRIP METHOD  (TO REMOVE THE SPACES )

name = "         rithik soun         "
dots = "............................."

print(name.strip() + dots)  # it remove all the extra spaces

#lstrip() it remove all the left spaces
#rstrip() it remove all the right spaces
#note it does not remove the spaces b\w the variables
print(name.lstrip() + dots)
print(name.rstrip() + dots)
# replace("the variable that is remove ","the variable that can be replace")
print(name.replace("i","o") +dots.replace(".","'"))


# if you want to remove the space b\w the second ch then we have to add replace 

name , ch = input("enter your name and character :-").split(",")

print("your length is:- {}".format((len(name))),"your character:- {}".format(name.lower().count(ch.lower().replace(" ","")))     )


#REPLACE AND FIND METHOD

#replace(" " ," ",how many words do you change )
name ="helo i am a good boy and i can do any thing without any body"
print(name.replace("any ","no",1))



#find() methiod (to check the position of any character)

name ="helo i am a good boy and i can do any thing without any body"
print(name.find("any",2)) # if you want to check th another position of the variable than we can set the position of the previous one

#if you want to find the position of second any without findind the first position than 


name ="helo i am a good boy and i can do any thing without any body"
any_1 = name.find("any")
any_2 = name.find("any" ,any_1+1)
print(any_2)






# CENTER METHOD


name = "RITHIK SOUN"
print(name.center(21 ,"*"))


# QUESTION:-

name =input("enter your name :-")
a= len(name)
l=int(a+8)
print(name.center(l,"*"))

#or
name =input("enter your name :-")
print("{}".format(name.center(len(name)+8,"*")))

print("welcome to the calculator\nOPERATIONS ARE:0 \n1) SUM\n2) SUB\n3) MUL\n4) DIV ")
Z = input("enter your operation:-")

a , b =input("enter the value of A and B:-").split(",")
print("sum{}".format(int(a)+int(b)))
print("sub{}".format(int(a)-int(b)))
print("mul{}".format(int(a)*int(b)))
print("div{}".format(int(a)/int(b)))


---------------------------------------------------------------------------------------------------------------------------------------------------

                                                                   CH ---3
                                                                
# IF STATEMENT ANS ELSE STATEMENT:-----
age  = int(input("enter your age :-"))
if age >= 14:  # use this  (:) to run the program and in this language we does not have to use the currly bracces
    print("you are adult")
else:

    print("grow up dude")
    
# PASS STATEMENT(IF YOU WANT TO PASS ANY COMMAND SO YOU CAN USE THE PASS STATEMENT)
AGE = int(44)
if age >= 14: 
  pass

  
# questiuon

rnum = int(88)
num = int(input("enter your no :-"))
if num == rnum:
    print("YOU WIN !!!!!")
else:
        if num > rnum:
            print("too high")
        else:
          ma      print("too low")

# AND , OR OPERATER
gender = input("enter your gender:-")
age = int(input("enter your age :-"))
if gender== "male" and  age <= 18:   # using (and) condition all condition are compulsory and if we use (or) then only one condition should be true
    print("you are elligible  to vote")
else:
    print("you are a child bro")



#QUESTION


name = input("enter your name:-")
age = int(input("enter your age :-"))
if name[0] =='a' or name[0]=='A' and age>= 10:
    print("you can watch coco movie")
else:
    print("sorry, you can't watch the movie")


# IF_ELIF_ ELSE STATEMENT:-0

# use this command to set the various else condition using (elif)

age = int(input("enter your age :-"))
if 0<=age<=3:
    print("ticket prize is free()")
elif 3<age<=20:
    print("ticket prize is 200()")
elif 20<age<=60:
    print("ticket prize is 250()")
else:
    print("ticket prize is free()")
    
# in(keyword)  it is used to check the elphbets present in the given varaibles or not :-



name = input("enter your name :-")
if 'r[0]' in name :
    print("yes present")
else:
    print("not present")

# MINI CALCULATER:-----------------------------------------------------------------------------

print("welcome to the calculator\nOPERATIONS ARE:0 \n1) SUM\n2) SUB\n3) MUL\n4) DIV ")
z = int(input("enter your operation:-"))
a ,b =input("enter the value of A and B:-").split(",")
if z==1:
    print("sum:-{}".format(int(a)+int(b)))
elif z==2:
    print("sub:-{}".format(int(a)-int(b)))
elif z== 3:
    print("mul:-{}".format(int(a)*int(b)))
else:
    print("div:-{}".format(int(a)/int(b)))
    

# loops

#( while loop:-)   ---------------
i=1
while i<=100:
     print("hello")
     i= i+1
# 1question
#(ask the user to sum the all given no:0)

no1 , no2 = input("enter your starting and ending no:-").split(",")
total = 0
i= int(no1)
while i<= int(no2):
    total = total +i
    i=i+1
print(total)


# 2QUESTION
#(ASK THE USER TO TYPE THE NO AND ADD THAT NO EX:- 1234:____1+2+3+4)

no = input("enter your no:-")
l =len(no)
total = 0
i = 0
while i<l:
     total = total+ int(no[i])
     i=i+1
print(total)




#12345
#01234

# 3 QUESTION
# (ASK THE USER TO TYPE THE NAME AND PRINT THAT NAMER HOW MANY TIMES THE ALPHABETS COMES :-)



name = input("enter your name:-")
#var = ""
i = 0
while i< len(name):
     #if name[i] not in var:
       #  var=var+ name[i]
          print(name[i] ,name.count(name[i])
          i=i+1

# INFINITE LOOP


while True:
     print("hello world")



# for loop-----------------------------------------------------

for i in range(1,101):
     print("hello",i)

# 1 question (sum from 1 to 100) ( IN THIS I ADD THE N AND L VARIABLE SO THAT USER CAN ADD THE STARTING AND ENDING VALUE )
n,l = input("enter the starting and ending value :-").split(",")
total = 0
for i in range(int(n),int(l)):
     total = total + int(i)
print(total)     


 
# 2 QUESTION
#(ASK THE USER TO TYPE THE NO AND ADD THAT NO EX:- 1234:____1+2+3+4)
no = input("enter the no:-")
#1234
total = 0
for i in range(0,len(no)):
     total= total + int(no[i])
print(total)


# 3 QUESTION
#(ASK THE USER TO TYPE THE NAME AND PRINT THAT NAMER HOW MANY TIMES THE ALPHABETS COMES :-)
name = input("enter your name ")
for i in range(0,len(name)):
     print(name[i],name.count(name[i]))
  

# BREAK AND CONTINUE KEYWORDS:-


#BREAK:---
for i in range(0,10):
    if i == 5:
        break  # it break the line and exit the program
    else:
         print("hello")

    # CONTINUE:--------


for i in range(0,10):
    if i == 5:
        continue # it continue the program and does not print the given value 
    else:
         print(i)


# QUESTION :-
w_no = int(88)
game_over = False
guess = 1
u_no = int(input("guess a no b/w 0 to 100:--"))
while not game_over:
    if u_no == w_no:
     print("you win","and you guessed this no in",guess)
     game_over = True
    elif u_no > w_no:
     print("too high")
     guess += 1
     u_no = int(input("guess  again"))
     
    else:
     print("too low")
     guess += 1
     u_no = int(input("guess  again"))
     
     


# loop

# to add the random no we use :-
import random
winning_no = random.randint(1,100)



# or
import random
w_no = random.randint(1,100)
game_over = False
guess = 1
u_no = int(input("guess a no b/w 0 to 100:--"))
while not game_over:
    if u_no == w_no:
     print("you win","and you guessed this no in",guess)
     game_over = True
    elif u_no > w_no:
     print("too high")
     guess += 1
     u_no = int(input("guess  again"))
     
    else:
     print("too low")
     guess += 1
     u_no = int(input("guess  again"))
    

# STEP ARGUMENT IN FOR LOOP:---------


for i in range(10,1,-1):
    print(i)
    



# STRING FORMATING IN FOR LOOP::----

name =input("name is:-")
for i in range(0,len(name)):
    print(name[i])

#OR WE CAN USE THE STRING METHOD TO DECREASE THE LEANGTH:----

name ="rithik"
for i in name:
    print(i)

no = input("enter your no:-")
#1234
total = 0
for i in no:  # in this we does not want to add tye range so we just simply  type the variable so tht it help us 
    total += int(i)
print(total)






                                                                                    CH 4
                                                                     _____________FUNCTION_________________
# FUNTIONS:       
def funtion name (no1,no2):(_this is also known as a parameter__ and when the user add that is known as argument)# in this we does not have to add the parameter      
    return no1+no2                             #  print(no1+no2)    (IN THIS WE CAN ALSO USE THE PRINT FUNTION SO THAT THE FUNTION WILL AUTOMATICALLY PRINT THE FUNTION WITHIOUT THE RETURN TYPE  )

# make a funtion
def call(no,no2):
    return(no+no2)
 total= call(22,22)
print(total)
# for thr user input :----


def call (no1,no2):
    return(no1+no2)
a= int(input("enter your first no-"))
b= int(input("enter your second no-"))
print(call(a,b))


# PRACISE OF FUNCTION:_____

# to askt he user to type the name and print that last no:-------

name = input("enter your name pls:-")
def nam(a):
    return name[-1]
print(nam(name))


# to check the no odd or even:-
def new(a):
    return(a%2)
no = int(input("enter your no:-"))
if new(no)==0:
    print("no is even")
else:
    print("no is odd")

# another method:-----

# in this we add the if statemnet in the funtion 
def no(a):
    if a%2 == 0:
        return "even"
    return"odd"
new_no = int(input("enter your no"))
print(no(new_no))


# another method
def no(a):
    return a%2 ==0
n= int(input("enter your no"))
print(no(n))

#EXERCISE
# TO CHECK THE  GREATEST OF TWO NO
def new(a,b):
    if a>b:
        return a
    else:    
        return b 
no1 ,no2 =input("entre two no:- ").split(",")
print(new(no1,no2),"is greater")



#EXERCISE
#GREATEST OF THREE NO:-------------
def greater(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c
no1,no2,no3 = input("enter the three no:-").split(",")
print(greater(no1,no2,no3),"is greater")
        

#FUNTION INSIDE THE FUNTION":-------------
def greater(a,b):
    if a>b:
        return a
    else:
        return b  # first we have to make trhe greteast of two no and aftre that call thet funtion in greatest
def greatest(a,b,c):
    bigger = greater(a,b)
    return greater(bigger,c)  # in this greater and c value again goes to greater funtion and calculate that value 
no1,no2,no3 = input("enter the three no:-").split(",")
print(greatest(no1,no2,no3),"is greater")  # we have to call the greatest funtion




#palandrom no:-------------
name = input("enter your name")
def rev(a):
    reverse = a[::-1]
    if a == reverse:
        return True
    else:
        return False
print(rev(name))


# fibonacci series

 # 0 , 1 ,1 ,2 ,3 ,5 ,8 ,13 ,
def feb(n):
    a = 0
    b= 1
    if n == 1:
        print(a)
    elif n == 2:
        print(a ,b)
    else:
        print(a ,b ,end=" ")
        for i in range(n-2):
            c= a+b
            a=b
            b=c
            print(c ,end=" ")
feb(25)




# SCOPE:----------------
# IN THIS IF WE WANT TO CALL THE VARIABLE THAN WE HAVE TO USE THE FUNTION ONLY
#FOR EX
a=7
def var():  # if we want to print the a variable than we have to call the var()
    global a # if we want to use the outside variable than we have to add global 
    a=5
    return a
print(a)
print(var())
print(a)





                                                                           ________________________CH -5______________________________________
                                                                                             INTRO TO LIST



 # list of no 
# to store the data we use the data 
no = 1,2,3,4,5
print(no)


# we can also store the all caracters also :-----
min = 1,2,"rithik", 2.3,None
print(min[::+2]) # we also add the slicing also to print the specific one using indexing

# to change the variable in the list
min = [1,2,"rithik", 2.3,None]
min[2] ='two'
print(min)

# to add data in the list we use append method :----
min = [1,2,"rithik", 2.3,None]
min.append('ankush')
print(min)


# ANOTHER METHOD TO STORE DATA
# insert method
min = [1,2,"rithik", 2.3,None]
min.insert(1,"ankush")
print(min)


#to add two list :-----
min1 = [1,2,"rithik", 2.3,None]
min2 = [3,4,"ankush", 2,None]
total = min1+min2
print(total)

# to add the one list in another one  
# use extend method
min1 = [1,2,"rithik", 2.3,None]
min2 = [3,4,"ankush", 2,None]
min1.extend(min2)
print(min1)
print(min2)

# to delete the data in the list :------
# use pop method:0
min1 = [1,2,"rithik", 2.3,None]
min1.pop(1)# if you does not pass the argument than it delete the last item in the list
print(min1)
# del operater
del min1[2]
print(min1)

# remove method:--
min1 = [1,2,"rithik", 2.3,None]
min1.remove(2.3)
print(min1)

# to arrange the list in sort order:
# use sort method:-

min1 = [1,2,1,8,3,5,6,3,2.3]
min1.sort()# use sort() method
print(min1)

min1 = ['a','g','b','x','f','v','n','u','u']
min1.sort()# use sort() method
print(min1)

# sorted funtion
#it print the sorted list but does not sort the array:-----
min1 = [1,2,1,8,3,5,6,3,2.3]
print(sorted (min1))
print(min1)

# clear to clear the list  
# copy to copy the no
min1 = [1,2,1,8,3,5,6,3,2.3]
min1.clear()
print(min1)
# copy

min1 = [1,2,1,8,3,5,6,3,2.3]
min2 = min1.copy()
print(min2)

# join method
 #convert list to string:-
user= ['rithik','33']
print(','.join(user))
  
#using list in for loop
fruits =  ['apple', 'mango','grapes','bannana']
for i in fruits:
    print(i , end = ", ")
 # list inside list:---


# EXERCISE
# TO ADD THE LIST AND MAKE THE SQUARE OF EACH ELEMENT IN THE LIST:-
num = list(range(1,12))
def sqr(n):
    square =[]
    for i in n:
        square.append(i**2)
    return square
print(sqr(num))

#EXERCISE
# to reverse the given list without using slicing or reverse method:--
ls = [1,2,3,4,5,6,7]
def rev(n):
    emp =[]
    for i in range(len(n)):
       epe =  ls.pop()
       emp.append(epe)
    return emp
       # emp.append(print(ls.pop))
print(rev(ls))


#EXERCISE:-----
ls = ['abc','huv','jkl']
def ver(a):
    emp =[]
    for i in a:
        emp.append(i[::-1])
    return emp
print(ver(ls))

# EXRECISE
# [1,2,3,4,5,6] ::: INPUT
#[[1,3,5],[2,4,6]]
ls = [1,2,3,4,5,6,7,8,9]
def lp(n):
    emp =[]
    evenl=[]
    oddl=[]
    for i in n:
        if i%2==0:
            evenl.append(i)
        else:
            oddl.append(i)
    emp.append(evenl)
    emp.append(oddl)
    return emp
print(lp(ls))
            

# eXERCISE:-
#[1,2,3,4,5],[7,2,5,6,1]  INPUT
#[1,2,5] OUTPUT
l1 = [1,2,3,7,6,9,18,4,5]
l2 = [18,7,2,5,6,1,]
def com(n):
    emp =[]
    for i in l1:
        for j in l2:
            if j==i:
                emp.append(i)
            else:
                j+=1
    return emp
print(com(l1))

# min and max funtion:---
no = [1,3,2,44,22,99]
print(max(no))
print(min(no))

no = [1,3,2,44,22,99]
# now suntract bigger from smaller no:-

def su(l):
    a = max(l)
    b = min(l)
    return a-b
print(su(no))

# exercise:-
ls = [1,2,[3,4,2,1],[1,6,5,7,5],[7,8,6,5]]
def le(l):
    count = 0
    for i in l:
        if type(i)==list:
            count+=1
    return count

print(le(ls))


                                                                                           CH ---6
                                                                                           TUPLES
                                                                                 ----------------------

# it is immutable , it is represent bo simple() parantheses . 
namere= (1,2,3,4,5,6,7,8,9) # this is tuple
print(namere)


CH - 7
DICTIONARIES:---

user = {'name' : 'rithik' , 'age': '33'}
print(user)
#or another method:-

user =dict(name = 'rithik', age = 33)
# it can be represent by the dict 
print(user)
# to add the data in the dictionaries:-

user =dict()
user['name'] = 'rithik'
print(user)


# in keywords and looping:-
user = dict(name = 'rithik',
            rollno = 1816864,
            subject = 'maths')
if 'names' in user:
    print("present")
else:
    print("not present")

# to check the inner values use (.values())

user = dict(name = 'rithik',
            rollno = 1816864,
            subject = 'maths')
if 'rithik' in user.values():
    print("present")
else:
    print("not present")

# looping in dictonaries:-__________

user = dict(name = 'rithik',
            rollno = 1816864,
            subject = 'maths')
for i in user.values():
    print(i)
# keys method(.keys())
# to print the keys

# item method:------------
# to print all the items in the dict:--------
user = dict(name = 'rithik',
            rollno = 1816864,
            subject = 'maths')
user_j= user.items()
print(user_j)

#ADD DATA IN THE LIST
user = dict(name = 'rithik',
            rollno = 1816864,
            subject = 'maths')
user['class']='12th'
print(user)

# TO DEL THE DATA
user = dict(name = 'rithik',
            rollno = 1816864,
            subject = 'maths',
            cls1= '12th')
userpoped=user.pop('cls1')
print(user)
print("the poped item is", userpoped)

# TO RaNDOM DEL ITEM
user = dict(name = 'rithik',
            rollno = 1816864,
            subject = 'maths')
print(user)
popeditem = user.popitem()
print(user)
print('poped item is', popeditem)

# UPDATE METHOD
user = dict(name = 'rithik',
            rollno = 1816864,
            subject = 'maths')
updateuser = dict(friend = 'ankush',
            rollno2 = 18168645678,
            subjects = 'mathss')
user.update(updateuser)
print(user)

# FROMKEYS METHODS :---
user = dict.fromkeys(range(1,1100),'i_love_u')
print(user)


# GET METHOD

# it dose not end the program it display none
user = dict(name = 'rithik',
            rollno = 1816864,
            subject = 'maths')
print(user.get('names'))
# to clear the directory:------


user = dict(name = 'rithik',
            rollno = 1816864,
            subject = 'maths')
user.clear()
print(user)

# TO COPY THE DICNORY:::---
user = dict(name = 'rithik',
            rollno = 1816864,
            subject = 'maths')
user_1= user.copy()
print(user_1.popitem())
print(user)

# TO MORE ABOUT THE GET METHOD:::::::::::::-------------
user = dict(name = 'rithik',
            rollno = 1816864,
            subject = 'maths')
print(user.get('namse','not found'))# it is used to display the not found
# it does not get the two same values so the last one will over write the key!!!!!!
# EXERCISE
def cub(a):
    user = dict()
    for i in range(1,a+1):
        user[i]= i**3
    return user
print(cub(10))
# to count the no of alphbets:____________

def con(s):
    count ={}
    for i in s:
        count[i]=s.count(i)
    return count
print(con('rithik'))


  # sets :________________
s = {1,2,3,4,3,24,2}
print(s)# it does not print dublicate items

s =[1,2,4,3,2,1,34,1]
print(list(set(s)))# it help to discart the dublicate items from the list
# methods
#  1 add method
#  2 remove method
#  3 discard method
#  4 copy method
#  5 union method    |
#  6 intersection method     &
a = {1,2,3,4,3,24,2}
a.add(99)
print(a)
b = {1,2,3,4,3,24,2}
b.remove(24)
print(b)
c = {1,2,3,4,3,24,2}
c.discard(99) # it print the set if the item is not present on the list
print(c)
d = {1,2,3,4,3,24,2}
s1 = d.copy()
print(s1)
a = {1,2,3,4,3,24,2}
b = {1,33,2,55,78}
print(a | b) # unoin
a = {1,2,3,4,3,24,2}
b = {1,33,2,55,78}
print(a&b) # intersection

                                                                                     # LIST COMPRIHENSION:---------------------
# IT DECTRESE THE LINES
# FOR EX
s = []
for i in range(1,11):
    s.append(i**2)
print(s)
# if we want to use the list comp:0-
s=[i**2 for i in range(1,11)]
print(s)
# it we want to display the negative list than:-

s =[-i for i in range(1,11)]
print(s)

#if you want to display the first letter of name present in the list than :----
name =['rithik','ankush','rahul']
s= [i[0] for i in name]
print(s)

# to use the funtion and print the reverse string:---
s = ['abc','def','ghi']
new=[i[::-1] for i in s]
print(new)
# when we use the funtion:--
def rev(l):
    return[i[::-1] for i in l]
print(rev(['rithik','ankush','rahul']))
print(rev(s))

# list comp using if statement:---
no=[1,2,3,4,5,6,7,8,9,10,11]
new =[i for i in no if i%2==0 ]
print(new)
# exercise:---
def inp(l):
    return[str(i) for i in l if type(i)==float or  type(i)==int ]
print(inp([True,False ,[1,2,3],1,1.0,3]))

# using if _ else statement:----------------------
s=[1,2,3,4,5,6,7,8,9,10]
new=[i*2 if i%2==0 else -i for i in s ]
print(new)

# nested list in list comp:-----------
s=[[i for i in range(1,100)] for j in range(1,10)]
print(s)


                                                                                            # DICTIONARY COMP

# to print 1 to 10 squares
s= {"square of{}".format(i):i**2 for i in range(1,11)}
for a,b in s.items():
    print(a,":",b)
# to count the no of alphabets on the name :-----
s="rithik"
r={i:s.count(i) for iin s}
print(r)
# IF_ELSE STATEMENT
s={1,2,3,4,5,6,7,8,9,10,11}
n={i:'even' if i%2==0 else'odd' for i in s}
print(n)



                                                                                        # set COMP
                                                                                        
r={'rithik','ankush','mohit'}
s={i[0] for i in r}
print(s)

                                                                                    # MAKE FLEXIBLE FUNC
# *OPERATER
# *ARGS
# it is use to give the more than two variables in the single funtion:-0
def fe(*args):
    total =0
    for i in args:
        total =  total+i
    return(total)
print(fe(1,2,3))

# ARGS WITH NORMAL PARAMETER:-------------
# if we use the normal parameter also than

def me(num,*args):# in this num is the normal parameter and *args is the flexible funtion
    total = 1
    for i in args:
        total*= i
    return(total)
print(me(2,3,4))

# ARGS WITH ARGUMENT:-------------------

def me(*args):
    total = 1
    for i in args:
        total*= i
    return(total)
n=[1,2,3,4]
print(me(*n))

# EXERCISE:---------------------------
n=[1,2,3,4,5,6]
def pe(num ,*args):
    if args:
        return[i**num for i in args]
    else:
        return"yore list is empty"
print(pe(2,*n))


                                                                         #KWARGS
#kwargs (keyword aarguments)
def me(name,**kwargs):
    return(name,kwargs)
d=dict( f_name = 'rithik' , l_name='soun')
print(me('rithik',**d))


                                                                        #LAMBDA EXPRESSION  (ANONYMOUS FUNCTION)
def add(a,b):
    return a+b

# it can be represented by:-----
add2 =lambda a,b : a+b
print(add2(100,2))

# multiply function
l=lambda a,b : a*b
print(l(3,4))

# practice :::::::::::::_----------------------
d= lambda a: a%2==0
print(d(3))

# using if else statemnet using lambda
def fun(s):
    if len(s)> 5:
        return true
    return false
#if wev use the lambda expresion 
a= lambda s: True if len(s)>5 else False
print(a('rithik'))

# when we reduse the code

a= lambda s:len(s)>5
print(a('rithik'))


                                                                     # ENUMERATE FUNTION:_____________________
s =(1,2,3,4,5,6,7)
pos = 0
for i in s:
    print(pos,'=',i)
    pos= pos+1
# with the help of enumerate------------
s =(1,2,3,4,5,6,7)
for pos,i in enumerate(s):
    print(pos,'=',i)
    
# practice:--------
l=['rithik','ankush','rahul']
def o(d,f):
    for pos,i in enumerate(l):
        if i == f:
            return pos
    return -1
print(o(l,'rahul'))


# map funtion
n=[1,2,3,4]
s= list(map(lambda a: a**2,n))
print(s)

# FILTER FUNTION()

# without loop it run the whole funtion
def a(b):
    return b%2==0
l=[1,2,3,4,5,6,7,8,9]
rs = list(filter(a,l)) # it filter the list or tuple where a is the funtion and l is given list in which we can filter , it is apply only on list and tuple 
print(rs)


# when we use lambda funtion:----
l=[1,2,3,4,5,6,7,8,9]
rs = list(filter(lambda a:a%2==0 ,l)) 
print(rs)

# when we use the list comp

l=[1,2,3,4,5,6,7,8,9]
def even(a):
    emp=[i for i in a if i%2==0]
    return(emp)
print(even(l))


#ZIP FUNCTION :------------
u1 =['rithik','ankush','rahul']
u2=['user1','user2','user3']
print(list(zip(u2,u1)))# it combine the value u1 and u2 and if the no are 3 then it add all three no 

#ADVANCE FUNTION
def avg (*args):
    average=[]
    for pair in zip(*args):
        average.append(sum(pair)/len(pair))
    return average
p=([1,2,3],[1,2,3],[1,2,3])
print(avg(*p))


avg =lambda *args:[sum(pair)/len(pair) for pair in zip(*args)]
print(avg([1,2,3],[1,2,3],[1,2,3]))

# ALL AND ANY FUNTION
# IF ONE OPTION IS TRUE THAN WHOLE STATEMENT IS TRUE :--------- ANY
# IF ALL THE OPTIONS ARE TRUE THAN ONLY THE STATEMENT IS TRUE:--------ALL
# for any
no1 =[1,2,3,4,5,6,7,8,9]
n=any([i%2==0 for i in no1])
print(n)
# for all
no1 =[1,2,3,4,5,6,7,8,9]
n=all([i%2==0 for i in no1])
print(n)

#ADVANCE MIN AND MAX FUNTION:
l=['rithik','ankushe','rahul']
print(max(l,key = lambda a: len(a)))
# max funtion caltulate the max value appear in the funtion
# if we want to add the condition that we want to calculate the highest no of alphabets than we use the key funtion and in that funtion we add the condition using lambda funtion
# question:
l=[{'name': 'rithik','age':33,'score':99},
   {'name': 'rohit','age':31,'score':1},
   {'name': 'ankush','age':3,'score':9}
 ]
print(max(l,key= lambda a:a.get('age'))['name'])

l={'rithik':{'age':33,'score':99},
   'rohit':{'age':31,'score':1},
   'ankush':{'age':3,'score':9}
 }
print(max(l,key= lambda a:l[a]['score']))

# SORTED FUNTION:-----------
l=['adfbsdaxa','wfsvSW','qdfqwsdswss']
print(sorted(l))

l=[{'name': 'rithik','age':33,'score':99},
   {'name': 'rohit','age':31,'score':1},
   {'name': 'ankush','age':3,'score':9}
 ]
print(sorted(l,key = lambda a:a['score'],reverse=True))

#DOC STRING:------------
# IT IS THE MESSSAGE WHICH IS WRITTEN BY THE USER IN FUNTION
def a(a,b):
        '''here is the message:--'''
        return a+b
print(a.__doc__)
print(len.__doc__)

print(help(print)) # in this way we can help 

                                                                               ch 14
                                                                               #DECORATORS

# in decorator we can assine the funtion to another varaible and after that we can print that varaible
def a(b):
        return b**2
s=a
print(s(7))


# pass funtion as a argument
l=[1,2,3,4,5,6,7,8,9]
def a(b):
        return b**2
print(list(map(a,l)))

l=[1,2,3,4,5,6,7,8,9]
def a(b):
        return b**2
def new(func,l):
        new_list=[]
        for i in l:
                new_list.append(func(i))
        return(new_list)
print(new(a,l))

# when we use the list and lambda comprehention
l=[1,2,3,4,5,6,7,8,9]
a= lambda func,l:[func(i) for i in l]
print(a(lambda a:a**2,l))

# when we return funtion from funtion:-----
def of():
        def iif():
                print('inside inner func')
        return iif # if we does not use the parantheses than we can use in the lower part
c= of()
c()

# example:-
def of(msg):
        def iif():
                print("message is ",msg)
        return iif
c=of("hii")
c()

# first class funtion or closure funtion:--------------
# make a funtion to return square or cube or power four
# MADE BY MEE
def of(a,b):
        def iff():
                print(a**b)
        return iff
c= of(4,3) 
c()

# MADE BY GURUJII
def of(a):
        def iff(b):
                return a**b
        return iff
c= of(4) 
print(c(3))


#DECORATORS:-----------
#ENHANCE THE FUNTIONALITY OF OTHER FUNTION:-
def decorator_funtion(any_function):
        def wrapper_funtion():
                print("this is decorator funtion")
                any_function()
        return wrapper_funtion
def func1():
        print("funtion 1")
def func2():
        print("funtion 2")

c=decorator_funtion(func1)
c()

# when we use the syntactic sugar
def decorator_funtion(any_function):
        def wrapper_funtion():
                print("this is decorator funtion")
                any_function()
        return wrapper_funtion
@decorator_funtion# this is syntactic sugar
def func1():
        print("funtion 1")
func1()
@decorator_funtion # this is syntactic sugar
def func2():
        print("funtion 2")
func2()

# when WE USE THE ARGUMENT IN THE FUNTICOIN WE USE THE ARGS AND KWARGS 
def decorator_funtion(any_function):
        def wrapper_funtion(*args,**kwargs):
                print("this is decorator funtion")
                return any_function(*args,**kwargs) # if we want to do some operator work than we have to return the funtion other wise it will only run the funtion and  only print funtion will run 
        return wrapper_funtion
@decorator_funtion# this is syntactic sugar
def func1(a):
        print("funtion with argument",a)
func1(7)
@decorator_funtion
def add(a,b):
        return a+b
print(add(2,3))

# problem when we use the doc sring in the decoraters
from functools import wraps # use this line to import the wraps
def decorator_funtion(any_function):
        @wraps(any_function) # here we use the  syntactic suger 
        def wrapper_funtion(*args,**kwargs):
                print("this is decorator funtion")
                return any_function(*args,**kwargs) 
        return wrapper_funtion
@decorator_funtion# this is syntactic sugar
def func1(a):
        ''' hii this is func1 doc'''
        print("funtion with argument",a)
func1(7)
print(func1.__doc__)
@decorator_funtion
def add(a,b):
        return a+b
print(add(2,3))

#PRACTICE::::::::::::::::::-
from functools import wraps
def decoractor_funtion(any):
        @wraps(any)
        def wrap(*args,**kwargs):
                print("you are calling",any.__name__,"funtion")
                print(addition.__doc__)
                return any(*args,**kwargs)
        return wrap
@decoractor_funtion
def addition(a,b):
       
        return a+b
print(addition(2,3))

import time
from functools import wraps
def c_l(var):
        @wraps(var)
        def wr(*args,**kwargs):
                print("the funtion is ",var.__name__)
                t1=time.time()
                r=var(*args,**kwargs)
                t2= time.time()
                total_time= t2-t1
                print("this funtion took ",total_time,"seconds")
                return r
        return wr
@c_l
def cube(n):
        return[i**3 for i in range(1,n+1)]
print(cube(1000))


                                                                                 CH - 15
                                                                              GENERATORS
                                                                              
# IT IS ITERATER
# generator
# 1) generator funtion
# 2) generator comprehention
# to make generator

def a(b):
        for i in range(1,b+1):
                yield(i)# to make a generator we use the yield 
for j in a(10): # to print the yield funtion we use the for loop 
        print(j)

# EXAMPLE TO DEFINE A GENERATOR AND PRINT ONLY EVEN NO 
def a(b):
        for i in range(1,b+1):
                if i%2==0:
                        yield(i)
rs = a(199) # if we use this than only it will print one time 
for j in rs:
        print(j)
for k in rs:
        print(k)
        

# generator comprehention::::::::::::::::::::::
r=(i**2 for i in range(1,11))
for i in r:
        print(i)
for i in r: # it only print one time becouse it is a generator 
        print(i)
        
# diff b/w list and generator
#1) memory useage, time
#2) when we use list , when we use generator
# ans
# 1) generator is best in time , and in memory also
#2) when we does not use the data in many time than we use the generator

                                                                                        CH - 16
                                                                                        OBJECT ORIENTED PROGRAMING
                                                                                        class , objets(instance),methods


# MAKING OWER FIRST CLASS
#__init__ is the constructer
 
class person:
        def __init__(self,first_name,last_name,age):
                self.first_name=first_name
                self.last_name=last_name
                self.age=age
p1=person('rithik','soun',33)
p2=person('ankush','soun',330)
print(p1)


# EXERCISE
class Laptop:
        def __init__(s,brand,model,price):
                s.brand=brand
                s.model=model
                s.price=price
                s.total=brand +" "+ model
p1=Laptop('LG','KD83',330000)
p2=Laptop('HP','AK47',33000000)
print(p1.total)
print(p1.brand)


# INSTANCE OR OBJECT
class person:
        def __init__(s,f,l,age):
                s.f=f
                s.l=l
                s.age=age
        def full_name(s):
                return s.f ,s.l
p1=person('rithik','soun',33)
print(p1.full_name())
print(person.full_name(p1))                

# example:::::::
class Laptop:
        def __init__(s,brand,model,price):
                s.brand=brand
                s.model=model
                s.price=price
                s.total=brand +" "+ model
        def a_d(s,ds):
                ds= s.price*ds/100
                return s.price-ds

r=Laptop('hp','model',39000)
p1=Laptop('LG','KD83',330000)
print(r.a_d(10))

# class_variable:______________
# example
# class variable help the program to not write the varable in many time it help to write only in one time
class circle:
        pi= 3.14 # this is class variable 
        def __init__(self,r):
                self.r=r
        def cal(self):
                return 2*circle.pi*self.r
c=circle(3)
print(c.cal())

# example:-----
# using the class variable  to discount all the laptop 10 %
class Laptop:
        ds= 10
        def __init__(s,brand,model,price):
                s.brand=brand
                s.model=model
                s.price=price
                s.total=brand +" "+ model
        def a_d(s):
                dp= s.price*s.ds/100
                return s.price-dp
Laptop.ds= 0
r=Laptop('hp','model',39000)
p1=Laptop('LG','KD83',330000)
print(p1.a_d())
# problem when the discont is only for some laptop:-----
# to print object eliment :
# print(p1.__dict__)
p2=Laptop('LG','KD83',330000)
p2.ds=90
print(p2.a_d())

# exercise
class Person:
        total=0
        def __init__(s,f,l):
                Person.total+=1
                s.f=f
                s.l=l
r=Person('rithik','soun')
r2=Person('ankush','soun')
print(Person.total)


#TO MAKE A CLASS METHOD 
class Person:
        total=0
        def __init__(s,f,l):
                Person.total+=1
                s.f=f
                s.l=l
        @classmethod
        def counts(cls):
                return "you have created",cls.total,'instance of cls',cls.__name__


r=Person('rithik','soun')
r2=Person('ankush','soun')
print(Person.total)
print(Person.counts())

# example
class PubG:
        royal_pass= 700
        def __init__(s,f,l):
                s.f=f
                s.l=l
                k=int(input("enter your amount"))
                if k>PubG.royal_pass:
                        print("yoiu can by the royal_pass ")
                else:
                        print("sorry you can not afford!!!!!!!")
r=PubG("rithik","soun")
print(r.f)
      

# to make a class method as a  constructer:-------
class Person:
        total=0
        def __init__(s,f,l):
                Person.total+=1
                s.f=f
                s.l=l
        @classmethod
        def from_string(cls,string):
                f,l=string.split(',')
                return cls(f,l)
        @classmethod
        def counts(cls):
                return "you have created",cls.total,'instance of cls',cls.__name__


r=Person('rithik','soun')
r2=Person('ankush','soun')
print(Person.total)
print(Person.counts())
r3=Person.from_string('rithik ,soun')
















                       #REVESION OF CLASS CHAPTER ::::--------



# my first class
class Person:
        def __init__(self,fn,ln,age):
                print('hey') # it explain that ower program will run two time p1 , and p2 
                self.fn=fn
                self.ln=ln
                self.age=age

p1=Person('rithik','soun',33)
p2=Person('ankush','soun',30)
print(p1.fn)
print(p2.fn)

# EXAMPLES
class Laptop:
        def __init__(self,name,model_name,prize):
                self.name=name
                self.model_name=model_name
                self.prize=prize

p1=Laptop('hp','123qaz',220000)
p2=Laptop('dell','123wsx',330000)
print(p1.name)
print(p2.name)



# INSTANCE METHOD:-------
class Person:
        def __init__(self,fn,ln,age):
                self.fn=fn
                self.ln=ln
                self.age=age
                self.full= fn,ln
        def Full_name(self):
                return self.fn, self.ln

p1=Person('rithik','soun',33)
print(p1.full)
print(p1.Full_name())  
print(Person.Full_name(p1))

# exercise
class Laptop:
        def __init__(self,n,b,p):
                self.n=n
                self.b=b
                self.p=p
        def applydiscount(self,a):
                dd = self.p*(a/100)
                return self.p-dd
p1=Laptop('hp','dinfn33',10000)
print(p1.applydiscount(10))


# class variables or class at tibutes::::::::::
class Circle:
        pi= 3.14
        def __init__(self,r):
                self.r=r
        def cir(self):
                return 2*Circle.pi*self.r
p1=Circle(2)
p2=Circle(4)
print(p1.cir())
print(p2.cir())

class Laptop:
       
        def __init__(s,f,m,p):
                s.f=f
                s.m=m
                s.p=p

        d= 20
        def dis(s):
                d= (s.p*Laptop.d)/100
                return s.p-d
p1= Laptop('hp','kufufyjf123e4',10000)
print(p1.dis())

class Laptop:
       
        def __init__(s,f,m,p):
                s.f=f
                s.m=m
                s.p=p

        d= 20
        def dis(s):
                d= (s.p*s.d)/100
                return s.p-d
p1= Laptop('hp','kufufyjf123e4',10000)
p2= Laptop('hero','kufufyjyfyjfkufy',220000)
p2.d=50

print(p1.dis())
print(p2.dis())


class Person:
        count_instance = 0
        def __init__(s,f,l):
                s.f=f
                s.l=l
                Person.count_instance +=1
p1=Person('rithik','soun')
p2=Person('swde','qfgwe')

print(Person.count_instance)


# class method
class Person:
        count_instance = 0
        def __init__(s,f,l):
                s.f=f
                s.l=l
                Person.count_instance +=1
        @classmethod
        def class_instance(cls):
                return  cls.count_instance
p1=Person('rithik','soun')
p2=Person('swde','qfgwe')

print(Person.class_instance())
 
#practice:____________
class Person:
        count=0
        def __init__(self,f,l,a):
                Person.count+=1
                self.f=f
                self.l=l
                self.a=a
        @classmethod
        def count_instance(cls):
                return cls.count
        def full_name(self):
                return self.f,self.l
        def age(self):
                return self.a >18
p1=Person('rithik','soun',38)
p2=Person('ankush','soun',32)
print(p1.age())
print(p1.count_instance())


#to make ower own constructer----
class Person:
        count=0
        def __init__(self,f,l):
                Person.count+=1
                self.f=f
                self.l=l
        @classmethod
        def const(cls,string):
                f,l= string.split(',')
                return cls(f,l)
                
        @classmethod
        def count_instance(cls):
                return cls.count
        def full_name(self):
                return self.f,self.l
        def age(self):
                return self.a >18
p1=Person('rithik','soun')
p2=Person('ankush','soun')
ps=Person.const('rithik,soun')
print(p1.count_instance())
print(ps.full_name())

# static method:-----------
class Person:
        count=0
        def __init__(self,f,l):
                Person.count+=1
                self.f=f
                self.l=l
        @staticmethod
        def hello():
                print("hii static method calls")
        @classmethod
        def const(cls,string):
                f,l= string.split(',')
                return cls(f,l)
                
        @classmethod
        def count_instance(cls):
                return cls.count
        def full_name(self):
                return self.f,self.l
        def age(self):
                return self.a >18
p1=Person('rithik','soun')
p2=Person('ankush','soun')
ps=Person.const('rithik,soun')
print(p1.count_instance())
print(ps.full_name())
Person.hello()

# encapsulation
# it means put the usefull date in same place
# ebstaction
#to hide the complexity of the program to the user
class Phone:
        def __init__(self,name brand,prize):
                self.name=name
                self.brand=brand
                self.prize=prize
        def call(self,phone_no):
                print("calling ......" phone_no)
        def full_name(self):
                return self.name,self.brand

# naming convention
 1)# if we use the underscore than it means that this is a private property so pls do not change that instance variables
   # for ex _name
 2)# if we use the double underscore than it is known as dunder/megic method
   # for ex __name__
# name mangling
# if we use the __name than python change that name to _(class name)__name by default





                                                    # three problems in class that we can handle it

                                                    
# 1) when we put the -ve value in the price section so that it print the -ve value so we have to prevent it
# 2)if we cange the value of price by using  p1.price=200 thaen it only display in the print(p1.price )
# 3) use @property and @setter decoratter
class Phone:
        def __init__(self,name,brand,prize):
                self.name=name
                self.brand=brand
                self.prize=max(prize,0) # max take the greater value so if we put the -ve value it take 0
                #if prize >0:
                #       self.prize=prize
                #else:
                #       self.prize=0
                #self.complete_specification = self.name,self.brand,"and prize is" ,self.prize
        @property
        def complete_specification(self):
                return  self.name,self.brand,"and prize is" ,self.prize
        @property
        def price(self):
                return self.prize
        @price.setter
        def price(self,new_price):
                self.prize =max(new_price,0)

        def call(self,phone_no):
                print("calling ......",phone_no)
        def full_name(self):
                return self.name,self.brand
p1=Phone('nokia','1234',230000)
print(p1.name)
print(p1.brand)
p1.price=-23300
print(p1.price)
print(p1.complete_specification)
# another again

class Phone:
        def __init__(self,name,brand,_price):
                self.name=name
                self.brand=brand
                self._price=max(_price,0)
        @property
        def complete_name(self):
                return self.name,self.brand,'price is ',self._price
        @property
        def price(self):
                return self._price
        @price.setter
        def price(self,new_price):
                self._price=max(new_price,0)

p1=Phone('nokia','1234fghj',-232000)
p1.price=-200
print(p1.price)
print(p1.complete_name)

  
                                                              #INHERITANCE


class Phone:
        def __init__(self,name,brand,price):
                self.name=name
                self.brand=brand
                self.price=price
                self.all=self.name,self.brand,self.price
                
class smart_phone(Phone):
        def __init__(self,name,brand,price,space,battery):
                super().__init__(name,brand,price)
                self.space=space
                self.battery=battery
                self.all=self.name,self.brand,self.price
p0=Phone('nokia','123qw123',8800)
p1=smart_phone('oneplus','123qwer12','33000','124gb','66000mh')
print(p0.all)
print(p1.all)
 
# we can derive more than one class form one bass class :
class Phone:
        def __init__(self,name,brand,price):
                self.name=name
                self.brand=brand
                self.price=price
                self.all=self.name,self.brand,self.price
                
class smart_phone1(Phone):
        def __init__(self,name,brand,price,space,battery):
                super().__init__(name,brand,price)
                self.space=space
                self.battery=battery
                self.all=self.name,self.brand,self.price
class smart_phone2(Phone):
        def __init__(self,name,brand,price,space,battery):
                super().__init__(name,brand,price)
                self.space=space
                self.battery=battery
                self.all=self.name,self.brand,self.price
p1=smart_phone2('vivo','123ert','111222','128gb','55000mh')
print(p1.all)

#1) multilevel inheritance
class Phone:
        def __init__(self,name,brand,price):
                self.name=name
                self.brand=brand
                self.price=price
                self.all=self.name,self.brand,self.price
                
                
class smart_phone(Phone):
        def __init__(self,name,brand,price,space,battery):
                super().__init__(name,brand,price)
                self.space=space
                self.battery=battery
class super_phone(smart_phone):
        def __init__(self,name,brand,price,space,battery,camera):
                super().__init__(name,brand,price,space,battery)
                self.camera=camera
p0=smart_phone('vivo','123ert','111222','128gb','55000mh')
p1=super_phone('vivo','123ert','111222','128gb','55000mh','48mp')
#print(p1.all)
#print(help(super_phone))
print(isinstance(p1,super_phone))
print(issubclass(super_phone,Phone))


#2) multiple inheritance:_::::::::::::::::
class a:
        def class_a(self):
                return 'class_A'
        def hello(self):
                return 'hello class_A'
class b:
        def class_b(self):
                return 'class_B'
        def hello(self):
                return 'hello class_B'
class c(b,a):
        pass
fn=c()
print(fn.class_a())
print(fn.class_b())
print(fn.hello())

                  #special magic method/dunder methods
# dunder method are thos methods in which double underscore are present in both side for ex :- __init__ is the dunder method
#there are many more dunder methods like:-
#__str__ # it is used by the users 
#__repr__ # it is mostly used by the developer to get the object value as it is  
#they both is used to print ower object
# __len__ it is used to calculate the length of the object
                #OPPERATER OVERLOADING
#__add__ to add the two no
# there are many another also methods

class a:
        def __init__(self,n,b,p):
                self.n=n
                self.b=b
                self.p=p
        def phone_name(self):
                return "{},{}".format(self.n,self.b)
        def __str__(self):
                return "{},{},{}".format(self.n,self.b,self.p)
        def __repr__(self):
                return "a('{}','{}','{}')".format(self.n,self.b,self.p)
        def __len__(self):
                return len(self.phone_name())
        def __add__(self,other):
                return self.p + other.p
        
ob=a("nokia","123qwe",2200000)
obe=a("nokia","123qwe",1100000)
print(len(ob))
print(ob +obe) # to calculate the sum of the price of two no
  

                                                             # POLYMORFISUM
                                                        #WHICH HAVE MANY FORMS
# FOR EX add
# in this 



                                                                          CH - 17
                                                                           ERROR



#ERROR RAISE
#to print the error
def add(a,b):
        if (type(a) is int) and (type(b) is int):
                return a+b
        # raise is used and we can used any type erreo in this ::_______
        raise TypeError( "oops you return wrong input")

print(add(5,'6'))


# exercise  1
#nonImplemented error

class animal():
        def __init__(self,name):
                self.name= name

        def sound(self):
                raise NotImplementedError("you have to define the method in sub-class")


        
class dog(animal):
        def __init(self,breed):
                super().__init__(name)
                self.breed=breed
        def sound(self):
                return "bhoww...bhowww"
        
        
class cat(animal):
        def __init(self,breed):
                super().__init__(name)
                self.breed=breed
        def sound(self):
                return "meaoww....meaowww"

#d= dog('catty')
#print(c.sound())

#print(d.sound())

c = cat("jarry")
print(c.sound())

#example 2

class mobile:
        def __init__(self,name):
                self.name=name

class mobilestore:
        def __init__(self):
                self.mobiles = []

        def add_mobile(self,new_mobile):
                if isinstance(new_mobile,mobile):
                        self.mobiles.append(new_mobile)
                else:
                        raise TypeError('new mobile should be an object of mobile class')

                        
m =mobile('nokia')
st='oneplus'
p= mobilestore()
#print(p.mobiles)
p.add_mobile(m)
rs=p.mobiles
print(rs[0].name)



#EXCEPTION handling :-------
# THOS ERREOS WHICH ARE COME IN EXECUTION
# WE DONT WANT THAT WITH SONE EXCETION OWER WHOLE CODE WILL DISTROY
# SO WE USE TRY AND EXCEPT
# TRY
while True:
        try:
                age = int(input("enter your age"))# user input:- seven so
                break
        except ValueError:
                print('invalid input...')
        except:
                print('unexcepted error.......')
      
if age>18:
        print("you can play the game ")
else:
        print("you can't play this game")


# excaption in else and finaly block:___
#else is used to make the command when there is no exception 
#else is used to make the try block more eassly readable 
# finally block it will run all time if the condition is satisfy or not it will run all time
# benefits of finally block

while True:
        try:
                age = int(input("enter your age :-"))# user input:- seven so
                
        
        except ValueError:
                print('invalid input...')
        except:
                print('unexcepted error.......')
        else:
                print(f"user input = {age}")
                break
        finally:
                print("finally block.............")
                


#question:-----
def divide(a,b):
        try:
                return a/b
        except ZeroDivisionError as ree:
                #print("you can not devide the no by zero")
                print(ree)
        except TypeError:
                print("no must be int or float")
        except:
                print("unexpected error.. ")

        
print(divide(4,2))



#CUSTOM EXCEPTION:
class nameerror(ValueError):
        pass 
def valid(name):
        if len(name)< 8:
                raise nameerror('name is too short')
username= input("enter your name:-")
valid(username)
print(f"hello {username}")



#modules

import pdb

# debugging
#L -- TO CHECK THE LIST WHERE THE COMMAND IS STOP
#Q --- TO QUIT
#N --- TO NEXT THE DEBUGGING
#C -- TO RUN THE PROGRAM ASUSUAL
pdb.set_trace()

name = input("enter your name :-")
age = int(input("enter your age :---"))
print(f"your name is {name} and ur age is {age}")
age2 = age +5
print(f"{name} and you will be {age2} in next five year")


                                                                 #ch -18
#1 readfile (we use open to read the file and bydefalt read is given)
#2 open funtion (it open the file)
#3 read method   (we use print(f.read()) to read this file and print it )
#4 seek ethod  (to change the position of cursor position)
#5 tell method
#6 readline method
#7 readlines method
#8 close method

# 1 read file

f= open('file1.txt')
print(f.read())
f.close()




#4 seek method


f= open('file1.txt')
#print(f"cursor position {f.tell()}")

print(f.read())
print(f"cursor position {f.tell()}")
print('before seek method')

f.seek(0)
print("after seek method")
print(f"cursor position {f.tell()}")
print(f.read())
f.close()




#WITH BLOCK
#CONTEXT MANAGER

with open("file1.txt") as f:
        data=f.read()
        print(data)

# to write the content in the file

#use this three method to write    "w,a,r+"
#w command owerwright the content and deletthe previous one and if the file is not present by the given name than it will create the file

with open("file2.txt",'w') as f:
        f.write('hello')

#a it means append mode that also create the new file is the given file is not present in the folder and it dose not owerwrite the content it add the line

with open("file1.txt",'a') as f:
        f.write('\npls do it')

#r+  it dose not create the file so we want to create it
# when we write some content than it owerwrite it so we want to move that curse by using seek method



with open("file.txt",'r+') as f:
        f.seek(len(f.read())) # here we use the seek method and cont the no of length 
        f.write('\npls do it')


# copy the data from one file and paste it in the another file 

with open("file.txt",'r') as rf: # here we create a file file.txt and we read it with the help of read funtion 
        with open('file1.txt','w') as wf: # here we create the file1.txt so that we can paste the date in it
                wf.write(rf.read())# here we paste the data which was plesent in the file.txt


with open("rs.txt",'a') as f:
        data=f.write("rithik , 22\nankush ,33\nrahul,44")
        print(data)     


#exercise 1

with open("rs.txt",'r') as rf:
        with open('rss.txt','a') as wf:
                for line in rf.readlines():
                        name,salary=line.split(",")
                        wf.write(f"{name} salary is {salary}")
                        

#exercise

with open ('rithik.html',"r") as rf:
        with open('output.txt',"a") as wf:
                for line in rf.readlines():
                        if "<a href=" in line:
                                pos = line.find("<a href=")
                                first_quote = line.find('\"',pos)
                                second_quote = line.find('\"',first_quote+1)
                                url= line[first_quote+1:second_quote]
                                wf.write(url +'\n')
        


#better method
with open ('rithik.html',"r") as rf:
        with open('output.txt',"a") as wf:
                page = rf.read()
                link_exist = True
                while link_exist:
                        pos = page.find("<a href=")
                        if pos == -1:
                                link_exist = False
                        else:
                                first_quote = page.find('\"',pos)
                                second_quote = page.find('\"',first_quote+1)
                                url= page[first_quote+1:second_quote]
                                wf.write(url +'\n')
                                page =page[second_quote:]




# how to read the file when it has a emmoji in it :---
with open('hii.txt','r' ) as f:
        print(f.encoding)
        data = f.read()
        print(data)



# csv file
# using reader method we import reader

from csv import reader

with open("New.csv",'r') as f:
        csv_reader= reader(f)
        #itirater so we want to start the loop
        next(csv_reader)
        for row in csv_reader:
                print(row)



#using DictReader method:

from csv import DictReader
#ordered dict
with open("New.csv",'r') as f:
        csv_reader= DictReader(f,delimiter=',')
        for row in csv_reader:
                print(row['email'])


#write to csv files
#writer
#dictwriter
# 1)
#to write in csv file we use write module
from csv import writer
with open("csvs.csv",'w',newline='') as f:
        csv_writter=writer(f)
        #methods -writerow , writerows
        #writerow method
        #it take only one row
        #csv_writter.writerow(['name','country'])
        #csv_writter.writerow(['rithik','INDIA'])
        #csv_writter.writerow(['harshit','CHINA'])
        #csv_writter.writerow(['ankush','INDIA'])
        #csv_writter.writerow(['rahul','INDIA'])
        #writerows method
        #it take all the rows in single line
        csv_writter.writerows([['name','country'],['rithik','INDIA'],['harshit','CHINA'],['ankush','INDIA'],['rahul','INDIA']])


# 2)
# to write in csv file using DictWriter

from csv import DictWriter
with open("csvs.csv",'w',newline='') as f:
        csv_writter=DictWriter(f,fieldnames=['first_name','last_name','age'])
        csv_writter.writeheader()
        #writerow , writerows
        #writerow
        # it take row one by one
        #csv_writter.writerow({
         #       'first_name':'rithik',
         #       'last_name':'soun',
          #      'age':'22'

           #     })
        #csv_writter.writerow({
         #       'first_name':'ankush',
          #      'last_name':'soun',
           #     'age':'10'

            #    })
        #writerows
        csv_writter.5writerows(
                [
                        {'first_name':'rithik','last_name':'soun','age':'44'},
                        {'first_name':'rahul','last_name':'soun','age':'55'},
                        {'first_name':'ankush','last_name':'soun','age':'33'}

                        ])

"""


#copy one csv file data and past it in another csvfile
from csv import DictReader,DictWriter

with open('csvs.csv','r') as rf:
        with open('file2.csv','w',newline='') as wf:
                csv_reader=DictReader(rf)
                csv_writter=DictWriter(wf,fieldnames=['first_name','last_name','age'])
                csv_writter.writeheader()
                for row in csv_reader:
                        fname,lname,age=row['first_name'],row['last_name'],row['age']
                        csv_writter.writerow(
                                {
                                        'first_name':fname,
                                        'last_name':lname,
                                        'age':age
                                        }
                                )


























































