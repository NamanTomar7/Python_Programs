import numpy as np
import pandas as pd

#Create an Array named user from 0 to 49 using numpy 
user=np.array([5,2,1,6,8,3,7])
sorted=np.sort(user)
print("Array-",user)
print("Sorted array-",sorted)          #arange creates an array with some range:- arange(start, stop, step)

# #Find mean , max and min using numpy
# #Method-1
# mean=np.mean(user)
# print("Mean:-",mean)

# #menthod-2
# print("Min-", user.min())
# print("Max-", user.max())

# print("Shape-",user.shape)  #It shows number of rows and columns of the array 

# # Reshape arranges the data according to user using rows and columns
# # mydata=user.reshape(5,10)   # 5 Represents rows and 10 represents columns
# # mydata=mydata+500
# # print("Reshaped-", mydata.shape)
# # print(mydata)
# # print(mydata>510)   #It will Display true or false above 510 in mydata

# #Array Slicing - It is used to access a small set of data from a larger array or data set. 
# print(user[:]) 
# print(user[5:20])   #It will Display 5-19 from the array named User

# emp=np.array([3,4,5,6,7,8,9,2,3,5])
# print(emp[ :-5])   # -5 means from last index to 5 before 

# #Pandas represend dataset in dataframe

# mydataframe=pd.DataFrame(data=np.arange(0,50).reshape(5,10))
# print(mydataframe)
# print("Mean-\n", mydataframe.mean())
# print("Mode-\n", mydataframe.mode())
# print("Median-\n", mydataframe.median())
# print(mydataframe.head(5))   #Represents top 5 row 
# print(mydataframe.loc[2,[6,]])