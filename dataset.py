#Methods to store multiple Elements in python 
 
#Tuple - can store multiple elements of different datatypes like list.
#But there's a difference between tuple and list that tuple's are unchangeable.
#Set - set is same as list but Unordered, Unchangeable, no duplicate.
#Dictionary - Ordered , changeable , no duplicate

myList= ["Yash", "Naman","Nikhil"]
myTuple=( "Nikhil","Naman" ,"Yash")
mySet={"Nikhil","Naman","Yash"}
myDict={"Name":"Naman","Email":"namantomar776@gmail.com"}
#         #Note- Name in myDict is a key that is used to access any element from dictionary.
# #check Datatype of these data sets
# print(type(myList))
# print(type(myTuple))
# print(type(mySet))
# print(type(myDict))

#             #Identification of These Data Sets
# #List --> [], tuple --> (), set --> {}, dict --> {:}

# #Acess data from data types
# print("List:", myList[0])
# print("tuple:", myTuple[1], "dict:", myDict["Email"])

for a in myList:
    print("List:",a)
for b in myTuple:
    print("Tuple: ", b)
for c in mySet:
    print("Set: ",c)
for d in myDict.values():
    print("Dict:", d)

myList.insert(0,"Naman")   #List allows duplicate elements.
print(myList)               

# mySet.insert(0,"Naman")
# print(mySet)

# myDict.insert(0,"Naman")
# print(myDict)

#Tuple and set is unchangeable while list and dict. can be changed.
#List and tuple can store duplicate items while set and dict. cannot.

#Adding Elements in Data sets
mySet.add("Sonia")
myDict.update({"name":"Sonia"})
print(mySet)
print(myDict)

#You can add or change elements of tuple by typecasting it into list and assigning to different variable. 
y=list(myTuple)
y.insert(0,"Pawan")
myTuple=list(y)
print(myTuple)

#Removing Elements from data sets.
myDict.pop("Name")
myList.pop(0)
mySet.remove("Naman")
print(myDict,myList,mySet)