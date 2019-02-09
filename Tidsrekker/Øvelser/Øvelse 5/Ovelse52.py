#%%
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import datetime as dt
import random
import os
import statsmodels.api as sm




#%%

filedir = ''
filename2 = 'oslotemp_monthly.txt'
file = os.path.join(filedir, filename2)
# load data
datatable2 = pd.read_table(file,sep='\s+',skiprows=14, skipfooter=20,engine='python',converters={'Month': lambda x: str(x)})
# Months are converted to strings to keep the leading 0's.
month=datatable2.iloc[:,1].values
data=datatable2.iloc[:,2].values
startyear = int(month[0][3:7])
endyear = int(month[-1][3:7])
time1 = startyear + int(month[0][0:2])/12
time2 = endyear + int(month[-1][0:2])/12
timearray = np.arange(time1,time2,1/12)


filename = 'hadcrut4.txt'
datatable = pd.read_table(filename,skipinitialspace=True, header=None,sep=" ")
years = datatable.iloc[::2,0] # read every second element in column
annualmeans = datatable.iloc[::2,13] # read every second element in column
monthlymeans = datatable.iloc[::2,1:13]
months = np.arange(years.values[0],years.values[-1]+1,1/12)

# plot data
fig, ax = plt.subplots(figsize = [8,5])
ax.plot(timearray, data/np.max(data), color = 'white')
ax.plot(months, monthlymeans.values.flatten()/np.max(monthlymeans.values.flatten()), color = 'pink')
# ax.plot(years,annualmeans,linewidth=2,color = "black")
ax.set_xlabel('t',fontsize = 18)
ax.set_ylabel('T(t)',fontsize = 18)
ax.set_title('Global temperature',fontsize = 18)
plt.ylabel('T',fontdict=None)
plt.xlabel('Year')
ax.grid()
ax.set_xlim(min(years),max(years))
ax.tick_params(axis='both',labelsize=20)
plt.show()

# filedir = ''
# filename = 'oslotemp_monthly.txt'

# file = os.path.join(filedir, filename)

# # load data
# datatable = pd.read_table(file,sep='\s+',skiprows=14, skipfooter=20,engine='python',converters={'Month': lambda x: str(x)})
# # Months are converted to strings to keep the leading 0's.
# month=datatable.iloc[:,1].values
# data=datatable.iloc[:,2].values

# startyear = int(month[0][3:7])
# endyear = int(month[-1][3:7])
# time1 = startyear + int(month[0][0:2])/12
# time2 = endyear + int(month[-1][0:2])/12
# timearray = np.arange(time1,time2,1/12)

# fig, ax = plt.subplots(figsize = [9,5])
# #plt.plot(timearray,data,linewidth=2,color = "black")
# plt.plot(timearray,data,linewidth=2,color = "white") # siste 10 år
# ax.set_xlabel('Year',fontsize = 18)
# ax.set_title('Monthly temperature Oslo',fontsize = 18)
# ax.grid()
# #ax.set_xlim(min(timearray),max(timearray))
# #ax.set_ylim(-12,20)
# ax.tick_params(axis='both',labelsize=22)
# plt.show()

#%%

