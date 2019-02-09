#!/usr/bin/env python
# coding: utf-8

# # Plot Oslo temperature data

# In[1]:


import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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


# In[2]:


fig, ax = plt.subplots(figsize = [9,5])
#plt.plot(timearray,data,linewidth=2,color = "black")
plt.plot(timearray[-120:],data[-120:],linewidth=2,color = "white") # siste 10 år
ax.set_xlabel('Year',fontsize = 18)
ax.set_title('Monthly mean temperature Oslo',fontsize = 18)
ax.grid()
#ax.set_xlim(min(timearray),max(timearray))
#ax.set_ylim(-12,20)
ax.tick_params(axis='both',labelsize=22)


# In[3]:


def climatology(x,months,returnresidual=False,period='Normal'):
    # inputs: 
    # x: the dataset
    # months: strings on format mm.yyyy, e.g. 01.2019
    
    startyear = int(months[0][3:7])
    startmonth = int(months[0][0:2]) # 4 = april
    endyear = int(months[-1][3:7])
    endmonth = int(months[-1][0:2])

    # pad with NaN in beginning or end, such that element 0 corresponds to a january month,
    # and last element (-1) to a december month
    # This is just to make indexation easier
    n_pad_start = startmonth - 1 #number of months missing for time to start in january
    n_pad_end = 12 - endmonth #number of months missing for time to end in december
    x_pad = np.concatenate((np.full(n_pad_start, np.nan), x, np.full(n_pad_end, np.nan)))
    
    # compute climatology: mean january temp, mean february temp, etc.
    C = np.zeros(12)
    if period == 'All': # all values
        for m in range(0,12):
            C[m] = np.nanmean(x_pad[m::12])  # take out every 12th element, then compute mean (ignoring nan values)
    elif period == 'Normal':
        normalperiod_start = 1961; normalperiod_end = 1990
        startindex = (normalperiod_start - startyear - 1)*12 # starts in january
        endindex = (normalperiod_end - startyear)*12 - 1 # ends in december
        x_normalperiod = x_pad[startindex:endindex+1]
        for m in range(0,12):
            C[m] = np.nanmean(x_normalperiod[m::12]) # take out every 12th element, then compute mean
    
    if returnresidual == False:
        return C
    elif returnresidual == True:
        # repeat climatology to create a periodic signal of equal length as the dataset
        repC = np.tile(C,int(len(x_pad)/12))
        # compute residual (by subtracting periodic signal)
        residual = x_pad - repC
        # remove the padded nan-values again:
        if n_pad_end>0:
            residual = residual[n_pad_start:(-n_pad_end)]
        else:
            residual = residual[n_pad_start:]
        return [C,residual]


# In[4]:


fig, ax = plt.subplots(nrows=1,ncols=2,figsize = [15,5])
ax[0].plot(climatology(data,month,period = 'Normal'));
ax[1].plot(climatology(data,month,period = 'All'));
plt.show()

# In[5]:


clim, res = climatology(data,month,returnresidual=True)

fig, ax = plt.subplots(figsize = [9,5])
plt.plot(timearray,res,linewidth=2,color = "white")
#plt.plot(timearray[-120:],res[-120:],linewidth=2,color = "black") # siste 10 år
ax.set_xlabel('Year',fontsize = 18)
ax.set_title('Monthly temperature anomalies in Oslo',fontsize = 18)
ax.grid()
ax.set_xlim(min(timearray),max(timearray))
ax.tick_params(axis='both',labelsize=22)

plt.show()

# In[6]:


# compute annual mean values:

def annualmean(x):
    # input: data starting in january and ending in december 
    y = np.full(int(len(x)/12), np.nan)
    for t in range(0,int(len(x)/12)):
        y[t] = np.mean(x[t*12:((t+1)*12)])
    return y


# In[7]:


years = np.arange(startyear+1,endyear+1)
T = annualmean(res[9:])

fig, ax = plt.subplots(figsize = [9,5])
plt.plot(years,T,linewidth=2,color = "black")
ax.set_xlabel('Year',fontsize = 18)
ax.set_title('Annual mean temperature anomalies in Oslo',fontsize = 18)
ax.grid()
ax.set_xlim(min(years),max(years))
ax.tick_params(axis='both',labelsize=22)

plt.plot();


# In[8]:


import statsmodels.api as sm

fig, ax = plt.subplots(figsize = [8,8])
sm.graphics.qqplot(T, ax=ax,fit=True, line='45')
ax.tick_params(axis='both',labelsize=22)
ax.xaxis.label.set_size(20)
ax.yaxis.label.set_size(20)
plt.show()


# In[9]:


print(np.mean(T))
print(np.std(T))
print(2*np.std(T))


# In[10]:


from scipy.stats import norm
print('Sannsynlighet for å være innenfor ett standardavvik:', norm.cdf(1)-norm.cdf(-1))
print('Sannsynlighet for å være innenfor to standardavvik:', norm.cdf(2)-norm.cdf(-2))


# In[12]:


sample_kvantiler = (T-np.mean(T))/np.std(T)
sample_kvantiler


# In[ ]:




