import matplotlib.pylab as plt
from scipy import stats as st
from sklearn.metrics import r2_score
import numpy as np

year=[2014,2015,2016,2017,2018,2019,2020,2021,2022,2023]
profit=[-0.2,0.6,2.4,3.0,10.1,11.6,21.3,33.4,-2.7,30.4]

# plt.scatter(age,salary)
# plt.show()

slope,intercept,r,p,std_err= st.linregress(year,profit)

print("slope-",slope,"\nIntercept-",intercept,"\nr-",r,"\np-",p,"\nstd_err-",std_err)
 
# If r is near to 1 -> Best Case , we apply linear expression
# If r is near to 0 -> Worst Case , we do not apply linear regression
# age1=int(input("\nEnter Age to predict salary: "))

def predict(year):
    return  slope*year+intercept

print("\nExpected Profit:- ",predict(2025))

# futureData=np.poly1d(np.polyfit(year,profit,3))
# print(futureData(2025))
# print("Expected profit in 2025- ",r2_score,profit,futureData(2025))