#List can store multiple elements of different data types.
#It can also store the duplicate data.
#List is an ordered data set. --> Ascending,sorting,decending

#create list and store your friends name

friends=["Yash","Isha","Nikhil","Sonia"]
print(friends) #print array

#ADD ages of your friends in the list
friends.append(36)

#Insert adds new data anywhere in the list using index number.
friends.insert(3, "Naman")  
print(friends)

friends.remove("Yash")     #Remove element from the array. 
print(friends)

friends.pop(4)      #Remove elements using indexing
print(friends)

print(friends[3])           #Access single element using indexing.

for x in friends:
    print(x)            #Access elements using loop.

#ADD favt. city name in the list.
#Add kasol in the first index.
#Remove last city in the list.
#sorting the list data.
#print the list data.

cities=["Goa","Delhi","New york","Pune","Ghaziabad"]
print("Name of my favorite cities:- \n",cities,"\n")

cities.insert(0,"Kasol")
print("After Adding 1 more city in index 0:- \n",cities,"\n")

cities.pop(5)
print("After removing last index:- \n",cities,"\n")

cities.sort()
print("After Sorting:- \n",cities,"\n")
