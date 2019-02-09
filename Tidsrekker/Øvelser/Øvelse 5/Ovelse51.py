
#%%
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import datetime as dt
import random
import os
import statsmodels.api as sm

filedir = ''
filename = 'oslotemp_monthly.txt'

file = os.path.join(filedir, filename)

# load data
datatable = pd.read_table(file,sep='\s+',skiprows=14, skipfooter=20,engine='python',converters={'Month': lambda x: str(x)})
# Months are converted to strings to keep the leading 0's.
month=datatable.iloc[:,1].values
data=datatable.iloc[:,2].values

startyear = int(month[0][3:7])
endyear = int(month[-1][3:7])
time1 = startyear + int(month[0][0:2])/12
time2 = endyear + int(month[-1][0:2])/12
timearray = np.arange(time1,time2,1/12)

fig, ax = plt.subplots(figsize = [9,5])
#plt.plot(timearray,data,linewidth=2,color = "black")
plt.plot(timearray,data,linewidth=2,color = "white") # siste 10 år
ax.set_xlabel('Year',fontsize = 18)
ax.set_title('Monthly temperature Oslo',fontsize = 18)
ax.grid()
#ax.set_xlim(min(timearray),max(timearray))
#ax.set_ylim(-12,20)
ax.tick_params(axis='both',labelsize=22)
plt.show()


Y = data
X = timearray - timearray[0]

X = sm.add_constant(X)
model1 = sm.OLS(Y,X)
results1 = model1.fit()
resid1 = model1.fit().resid
results1.params
print(results1.summary())

# plot trend together with data
fig, ax = plt.subplots(figsize = [20,10])
ax.plot(timearray,data);
ax.plot(timearray,results1.fittedvalues, label = 'Linear fit')
ax.set_xlabel('Year',fontsize = 18)
ax.set_title('Monthly mean temperature Oslo',fontsize = 18)
ax.grid()
ax.tick_params(axis='both',labelsize=18)
ax.legend(loc = 'best')
plt.show()


plt.plot(resid1)
plt.show()



# Residualene for lineær regresjon ser ut til å være normalfordelt støy
# Dette kan bety at modellen ikke gjør økende "feil" over tid.

#%%


#Som i Eq. (2.19-2.21) i boka:
# prediktorer:
Y = data
Z1 = timearray - timearray[0]  #Sånn at x-aksen start på 0 og oppover.
Z2 = Z1**2

X = np.column_stack((Z1, Z2))
X = sm.add_constant(X)

model2 = sm.OLS(Y,X)
results2 = model2.fit()
resid2 = model2.fit().resid
results2.params
print(results2.summary())

# plot trend together with data
fig, ax = plt.subplots(figsize = [20,10])
ax.plot(timearray,data);
ax.plot(timearray,results2.fittedvalues, label = 'Linear fit')
ax.set_xlabel('Year',fontsize = 18)
ax.set_title('Monthly mean temperature Oslo',fontsize = 18)
ax.grid()
ax.tick_params(axis='both',labelsize=18)
ax.legend(loc = 'best')
plt.show()

plt.plot(resid1)
plt.show()

# Dette er en litt bedre modell

#%%
