#Function Declaring
def fullname(fname,lname):
    print(fname+" "+lname)  #Function Definition

first=input("Enter your first name: ")
last=input("Enter your last name: ")

fullname(first,last) #Passing variables to function and calling it.

def name(*kids):
        print("Smartest kid is: "+ kids[3])

kid1="Naman"
kid2="sonia"
kid3="Nikhil"
kid4="Isha"

name(kid1,kid2,kid3,kid4)