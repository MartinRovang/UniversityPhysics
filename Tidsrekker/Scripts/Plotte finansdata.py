#!/usr/bin/env python
# coding: utf-8

# # Plotting av finansdata

# ## Dow Jones index

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt

# load data
filename = '/Users/hege-beatefredriksen/OneDrive - UiT Office 365/Teaching/STA-2003spring2019/Data/DJI.csv'

datatable = pd.read_csv(filename)
dates = datatable.iloc[:,0]
close = datatable.iloc[:,4]

print(dates.values)
x = [dt.datetime.strptime(d,'%Y-%m-%d').date() for d in dates.values] # convert dates to datetime.date format
#print(x)


# In[2]:


#plot data
fig, ax = plt.subplots(figsize=(20,7))
ax.plot(x, close.values)
fig.autofmt_xdate()

# Tick every year on Jan 1st
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

ax.set_xlabel('date',fontsize = 26)
ax.set_ylabel('DJI',fontsize = 26)
ax.grid()
ax.tick_params(axis='both',labelsize=14)
ax.set_title('Dow Jones Industrial Average',fontsize = 26)
ax.set_xlim(min(x),max(x));


# ## OSEBX (Oslo børs benchmark index)

# In[3]:


# load data
filename = '/Users/hege-beatefredriksen/OneDrive - UiT Office 365/Teaching/STA-2003spring2019/Data/osebx.csv'

datatable = pd.read_csv(filename)
dates = datatable.iloc[:,0]
Last = datatable.iloc[:,1]

print(dates.values)

# endre format på år, slik at det består av 4 siffer istedenfor 2. 
datoliste = dates.values; # sett datoene lik de gamle først, og bytt dem deretter ut i for-løkka:
for k in range(len(datoliste)):
    year = datoliste[k][6:8]
    if 30<= int(year) <= 99:
        year = '19' + year
    else:
        year = '20' + year
    datoliste[k] = datoliste[k][0:6] + year
print(datoliste)
    
x = [dt.datetime.strptime(d,'%d.%m.%Y').date() for d in datoliste] # convert dates to datetime.date format
#print(x)


# In[4]:


#plot data
fig, ax = plt.subplots(figsize=(20,7))
ax.plot(x, Last.values)
fig.autofmt_xdate()

# Tick every year on Jan 1st
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

ax.set_xlabel('date',fontsize = 26)
ax.set_ylabel('OSEBX',fontsize = 26)
ax.grid()
ax.tick_params(axis='both',labelsize=14)
ax.set_title('Oslo Børs Benchmark index',fontsize = 26)
ax.set_xlim(min(x),max(x))


# In[ ]:




