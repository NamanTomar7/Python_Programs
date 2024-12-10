import os
#Create and open a file
myname=open("Naman.txt","w")

#Write in the file
myname.write("My Name is Naman Tomar")

#To overwrite a text by user
#Method -1
# name1=input("Enter your name:")
# myname.write(name1)

# #Method 2
# myname.write(input("Enter your name:"))

#To read a file
myname=open("Naman.txt","r")
# print(myname.read())
mydata=myname.read()
if "Tomar" in mydata:
    print("yes")
else:
    print("no")    