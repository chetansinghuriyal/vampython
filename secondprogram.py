   # -> # is used to comment the line
# -> it is also used to define the code meaning 
# -> it can also comment and uncomment mutliple lines using ctrl +/

# comment example 
# write a program to print your name 
print("my name is chetan singh uriyal") #print to display statement 

#variables can store the value and it can change it any time 
name= "chetan singh uriyal"
#pass the variable in the print function 
print("my name is "+ name )# + is used to concatenate the strings

#declare and initialize the multiple variable in print function
age=20
gender="male"
email = "demo@demo.com"
#pass the multiple variable in print function
# this line give the type error 
# reason for error str can't be concatenate with the integer
# problem  
#print ("my name is "+ name+  
#                  " my age is " +age +" and gender is "+gender")
# solution 1- int variable + replace by ,
print("my name is "+ name+ 
     " my age is",age ," and gender is "+gender )
#solution 2 -enclosed the variable inside string statement using f
# pass the variable in()
print(f"my name is {name} my age is {age} and gender is {gender} and mail is {email}")

# data types in pyhton 
print(type(name)) 
print(type(age))


#1 str-> it can store the string data e.g name="saksham joshi"
#2 int -> it can store the numeric data e.g name="33"
#3 float-> it can store the decimal no e.g pecentagee="75.45"

#Typecasting in python :-convert one datatype to another datatypes
#e.g sometime when we purchase item in float we paid in integer

purchaseitemprice=90.32
paiditemprice=int (purchaseitemprice)
print("paid amount is",paiditemprice)



#  it is not possible string to int
# name="pawan"
# fname=int(name)
# print("name is",fname)

#but int to  string is possible
ageinstring=str(age)

print("my age  is " + ageinstring + " and gender is "+gender)