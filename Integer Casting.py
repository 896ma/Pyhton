from curses import COLOR_BLACK
from distutils.command.install_lib import PYTHON_SOURCE_EXTENSION
from modulefinder import IMPORT_NAME


x=int(8.9)
y=int(7)
z= int("3")

print (x)
print (y)
print (z)


#creating,initializing and adding variables in python 
a=4
h=8
print (a+h)
#Getting a character at any position of a string

m="Fuck you"
print(m[2])
#Modulus operator

z=9
q=2
print(z%q)
#Assignment operator

x=5
print(x)
 
#The multiplication Operator
g=3
w=12*g
print(w)
  

#Creating list in python
Thislist =["Python","Java","VisualBasic","C++","Cobol"]
print(Thislist)
#Access particular items in a list
Thislist =["BigData","Machine learning","AI","CloudComputing"]
print(Thislist[0])
#Remove white space from a string
d="Chinja ua mortherfucker"
print(d.strip())
#changing  the value of an item in a list

myNewlist=["cs","IT","med","law","Journalism"]
myNewlist[3]=("Electrical Engineering")
print(myNewlist)

#Looping through a list
myLoopList=["Avocado","Mutura","Maembe","Mapera","Githeri"]
for x in myLoopList:
     print(x)
#Checking if a list item exists
myLoopList=["Avocado","Mutura","Maembe","Mapera","Githeri"]
if "Mutura" in myLoopList:
    print("Yes",'Mutura',"is in the Looplist")
else:
    print("You are wrong Motherfucker")

#Getting the length of a list of items
myLoopList=["Avocado","Mutura","Maembe","Mapera","Githeri"]
print(len(myLoopList))
#Add an item to the end of a list(.append)
myLoopList=["Avocado","Mutura","Maembe","Mapera","Githeri"]
myLoopList.append("Dhamogwaja")
print(myLoopList)

#add an item to a specific index in a list 
myLoopList=["Avocado","Mutura","Maembe","Mapera","Githeri","Dhamogwaja"]
myLoopList.insert(2,"Smocha")
print(myLoopList)

#Remove an item from a list
myLoopList=["Avocado","Mutura","Maembe","Mapera","Githeri","Dhamogwaja"]
myLoopList.remove("Dhamogwaja")
print(myLoopList)

#Remove the last item from the list
myLoopList=["Avocado","Mutura","Maembe","Mapera","Githeri","Dhamogwaja"]
myLoopList.pop()
print(myLoopList)

# Remove an item at a specified index
myLoopList=["Avocado","Mutura","Maembe","Mapera","Githeri","Dhamogwaja"]
del myLoopList[3]
print(myLoopList)

#Empty an entire list
myLoopList=["Avocado","Mutura","Maembe","Mapera","Githeri","Dhamogwaja"]
myLoopList.clear()
print(myLoopList)

#USing the list() constructor to create a list
myLoopList=list(("Avocado","Mutura","Maembe","Mapera","Githeri","Dhamogwaja"))
print(myLoopList) 

#LIST NAVIGATION COMPLETED
#Tuples and lists  are almost the same and minimum complexity exists between the two
#creating a tuple

DemoTuple=("vscode","netbeans","intellij","msword","msexcel","codeblocks")
print(DemoTuple)

#float casting
x=(float(6))
print(x)

# Creating a  Dictionary
myDictionary={
    "Name":"Engineer",
    "Language":"Java",
    "Specialty":"WebDevelopment"
}

print(myDictionary)
#Accessing items in the Dictionary
myDictionary={
    "Name":"Engineer",
    "Language":"Java",
    "Specialty":"WebDevelopment"
}
x =myDictionary["Language"]
print(x)
#Changing the value of an item in a dictionary
myDictionary={
    "Name":"Engineer",
    "Language":"Java",
    "Specialty":"WebDevelopment"
}
myDictionary["Language"]="python"
print(myDictionary)

#using the values() function to return the values of a dictionary
myDictionary={
    "Name":"Engineer",
    "Language":"Java",
    "Specialty":"WebDevelopment"
}
for x in myDictionary.values():
    print(x)
#Python loops(For loop)
Fruits=["Oranges","Pineapple","Avocado","Maembe","Bomba"]
for x in Fruits:
    print (x)
#Looping through a string
Cheo ="Managera"
for x in Cheo:
    print(x)
#Break statement in a for loop
Fruits=["Oranges","Pineapple","Avocado","Maembe","Bomba"]
for x  in Fruits:
    print(x)
    if x =="Avocado":
        break

# Continue statement in a for loop(Skips the item selected and proceeds to print out the rest)
Fruits=["Oranges","Pineapple","Avocado","Maembe","Bomba"]
for x in Fruits:
    print(Fruits)
    if Fruits==("Pineapple"):
        continue
   
   
   
#unfunctional code

#using the range() function in a  for loop
for x in range(10):
    print(x)

#Else in a for loop
for x in range(6):
    print(x)
else:
    print("Task completed")
#A nested for loop

Joiner=["Software","Big","Machine","Artificial"]
Disc=["Engineer","Data","Learning","Intelligence"]

for x in Joiner:
    for y in Disc:
     print(x,y)
#While loop
i =2
while i<7:
    print(i)
    i+=1
#Using the Break statement in a while loop
i=7
while i<15:
    print(i)
    if (i ==12):
        break
    i+=1
#Using the continue statement in a while loop
d=9
while d<17:
    d+=1
    if d ==14:
        continue
    print(d)
#The elif ,if and else statements
a=34
b=34
if a>b:
    print(a,"is greater than",b)
elif b>a:
    print(b,"is greater than ",a)
else:
    print("Nigga you are so wrong")
#Short hand if..else
a=356
b=987
print("A") if b>a else print("B")
#The "and " key word

a=278
b=567
c=984
if a<b and c>b:
    print("You are Gay") 

#SETS
#in sets ,the list is unordered and may appear in any random order
#Creating a set

mySet={"Django","Python","Sql","Vb.net"}
print(mySet)
#remove an item from a set

mySet={"Django","Python","Sql","Vb.net"}
mySet.remove("Python")
print(mySet)

#Python functions
#Create and  call a function
def Chinja_ua():
    print("Chinja ua Motherfucker")
Chinja_ua()

#Function Parameters
def Chinja_ua(fname):
    print(fname +"Oduor")

Chinja_ua("Marvine")
Chinja_ua("Johnston")
Chinja_ua("Wa kimani")

#Default Parameter Value(Outputs the default value of a function if a particular value was not specified)
def Chinja_ua(country="Kenya" ):
    print("Iam from" +country)
Chinja_ua("Uganda")
Chinja_ua("The United States")
Chinja_ua("Germany")
Chinja_ua("South Africa")
Chinja_ua()

#Let a function return a value
def Chinja_ua(x):
    return (5*x)
print(Chinja_ua(6))
print(Chinja_ua(8))
print(Chinja_ua(12))
print(Chinja_ua(9))
print(Chinja_ua(5))
#python arrays(A collection of ordered series of elements of the same type)
#Creating an array
import array
a=array.array('i',[1,2,3,4,5,6])
print(a)
#The first array stands for the name of the module,the second one for the array constructor and the i is the typecord
#in this case our array stores integer values

#Another way of creating an array
from array import *
a=array('i',[7,8,9,3,24,7])
print(a)
#Accessing Array Elements(Must be defined first)
from array import *
a=array('i',[7,8,9,3,24,7])
print(a[5])
#Accesing array values using negative indices
import array
a=array.array('i',[65,34,78,36,91,17,93])
print(a[-3])
#looping through an array
from array import *
a=array('i',[65,34,78,36,91,17,93])
for x in a:
    print(a)
#Finding the length of an array
import array
a=array.array('i',[65,34,78,36,91,17,93])
print(len(a))
#Adding elements to an array(using the extend() function to add more than one items to the end of an array)
from array import *
a=array('d',[65.4,34.5,78.6,36.7,91.3,17.9,93.1])
a.extend([67.5,34.6])
print(a)
#using inser() function to add an item to a specific index of an array
import array
b=array.array('d',[3.6,5.9,4.5,8.7,2.9,1.3])
b.insert(2,4.6)
print(b)
#The values of an array item at a  given index
from array import *
c=array('d',[3.6,5.9,4.5,8.7,2.9,1.3])
c[2]=9.4
print(c)
 #project development in python
 #project Developer levels (Beginner,Intermediate,Complex projects)
  
#simple project building..helps to  amiliarize with workflow and problem solving
#libraries and frameworks are not used in designing simple projects
from array import *
e=array('d',[43.3,56.3,78.9,9.1]) 
print(e)
#Mimial libraries and frameworks are used in designing intermediate projects








    
    

 
   
 



  

















 
