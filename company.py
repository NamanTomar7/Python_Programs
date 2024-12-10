import numpy as np
import pandas as pd
import json

# employee=np.arange(1000000)
# employee=employee.reshape(100000,10)
# print(employee)
# highest=pd.DataFrame(employee)
# print("\nHighest Salary paying Employee's-\n", highest.tail(1))
# lowest=highest.head(1)
# lowest=lowest+500

# print("\nBonus to lowest paying Emloyees-\n",lowest)
# middle=pd.DataFrame(employee.reshape(10,100000))
# middleEle=middle[4:6]
# print("Accessing middle elements-\n",middleEle)

data=np.arange(0,12)
data=data.reshape(3,4)
# print(data)

data1=pd.DataFrame(data)
print("Raw data-\n",data1)
print("Displaying 6,7,10,11 using array slicing- \n",data1.iloc[1:3,2:4])  #Accessing 6,7,10,11

print("Displaying 5,6,9,10-\n",data1.iloc[1:3,1:3])

data1.to_json("sample.json")