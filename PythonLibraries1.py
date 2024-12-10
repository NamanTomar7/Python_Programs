import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# years=np.array([2005,2006,2007,2009,2011])
# grades=np.array([54.05,72,69,73,87])

# #Show data in graph- line(x,y),piegraph(x),bargraph(x,y),scatters(x,y)
# # Dataset must have sane size in these graphs 
# #plt.plot(years,grades)
# plt.plot(years,grades,marker="o")
# plt.title("Academic Growth")
# plt.xlabel("passing marks")
# plt.ylabel("student marks")
# plt.show()

# language=np.array(["python","java","javascript","c#"])
# trending=np.array([45,30,20,10])
# plt.title("Trending language marketplace")
# plt.pie(trending)
# plt.legend(language)
# plt.show()

#Jio 5 years sales growth rate

growth=np.array([2019,2020,2021,2022,2023])
revenue=np.array([29.6,57.1,125,155,226])
plt.title("Jio past 5 years growth")
plt.xlabel("Years")
plt.ylabel("Revenue(In Crores)")
plt.bar(growth,revenue)
plt.grid()
plt.show()