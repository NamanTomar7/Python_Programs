#Errors in program

#Error-1
# print(x)

try:
    print(x)
except NameError:
    print("x is not defined")

#Error-2
x="Naman"
y=5

try:
    c=x+y
except TypeError:
    print("You can not concatenate String with Integer")    

#Error-3
# y=1/0
try:
    y=1/0
except ZeroDivisionError:
    print("Numbers can not be divided by zero")

#Error-4
name="pawan"
# no=int(name)

try:
    no=int(name)
except ValueError:
    print("Can not typecast string into integer")

#Error-5
friend={"Naman","Nikhil","yash"}
#friend[4]
try:
    friend[4]
except TypeError:
    print("There is no element at index 4")    
