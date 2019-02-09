#!/usr/bin/env python
# coding: utf-8

# # Plot global temperature data

# In[38]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load data
filename = '/Users/hege-beatefredriksen/OneDrive - UiT Office 365/Teaching/STA-2003spring2019/Data/hadcrut4.txt'

datatable = pd.read_table(filename,skipinitialspace=True, header=None,sep=" ")
years = datatable.iloc[::2,0] # read every second element in column
annualmeans = datatable.iloc[::2,13] # read every second element in column
monthlymeans = datatable.iloc[::2,1:13]
months = np.arange(years.values[0],years.values[-1]+1,1/12)


# In[39]:


# plot data
fig, ax = plt.subplots(figsize = [8,5])
ax.plot(months, monthlymeans.values.flatten())
ax.plot(years,annualmeans,linewidth=2,color = "black")
ax.set_xlabel('t',fontsize = 18)
ax.set_ylabel('T(t)',fontsize = 18)
ax.set_title('Global temperature',fontsize = 18)
plt.ylabel('T',fontdict=None)
plt.xlabel('Year')
ax.grid()
ax.set_xlim(min(years),max(years))
ax.tick_params(axis='both',labelsize=20)


# In[ ]:




