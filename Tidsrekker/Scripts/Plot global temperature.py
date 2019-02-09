#!/usr/bin/env python
# coding: utf-8

# # Plot global temperature data

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# load data
filename = '/Users/hege-beatefredriksen/OneDrive - UiT Office 365/Teaching/STA-2003spring2019/Data/hadcrut4.txt'

datatable = pd.read_table(filename,skipinitialspace=True, header=None,sep=" ")
years = datatable.iloc[::2,0].values # read every second element in column
annualmeans = datatable.iloc[::2,13].values # read every second element in column
monthlymeans = datatable.iloc[::2,1:13].values
months = np.arange(years[0],years[-1]+1,1/12)


# In[2]:


# plot data
fig, ax = plt.subplots(figsize = [8,5])
ax.plot(months, monthlymeans.flatten())
ax.plot(years,annualmeans,linewidth=2,color = "black")
ax.set_ylabel('T(t)',fontsize = 18)
ax.set_title('Global temperature',fontsize = 18)
ax.set_xlabel('Year',fontsize = 18)
ax.grid()
ax.set_xlim(min(years),max(years))
ax.tick_params(axis='both',labelsize=20)


# ## analyser inkrementer:

# In[3]:


n = len(np.diff(annualmeans))

# plot data
fig, ax = plt.subplots(nrows=2, ncols=1, figsize = [16,10])
ax[0].plot(years[1:],np.diff(annualmeans),linewidth=2,color = "black")
ax[0].set_ylabel('diff(Global temperature)',fontsize = 18)
ax[0].set_xlabel('Year',fontsize = 18)
ax[0].grid()
ax[0].set_xlim(min(years),max(years))
ax[0].tick_params(axis='both',labelsize=20)

from statsmodels.tsa.stattools import acf 

ax[1].stem(acf(np.diff(annualmeans),nlags=25))
ax[1].plot(np.full(26,2/np.sqrt(n)),'--',color='gray')
ax[1].plot(np.full(26,-2/np.sqrt(n)),'--',color='gray')
ax[1].set_ylabel('ACF',fontsize = 18)
ax[1].grid()
ax[1].tick_params(axis='both',labelsize=20)


# In[4]:


np.mean(np.diff(annualmeans))*160 # delta: stigningstallet for en lineær trend


# ## Trendmodell basert på info om strålingsubalanse på toppen av atmosfæren:

# In[5]:


# load data
filename = '/Users/hege-beatefredriksen/OneDrive - UiT Office 365/Teaching/STA-2003spring2019/Data/hansenforcing.txt'

datatable = pd.read_table(filename, skiprows=5, header=None, sep="\s+")
years2 = datatable.iloc[:,0]
net_forcing = datatable.iloc[:,9]

# plot 
fig, ax = plt.subplots(figsize = [8,5])
ax.plot(years2, net_forcing)
ax.set_xlabel('Year',fontsize = 18)
ax.set_ylabel('Forcing estimate (W/m$^2$)',fontsize = 18)
ax.grid()
ax.set_xlim(min(years),max(years))
ax.tick_params(axis='both',labelsize=20)


# In[6]:


# Modellerer tregheten til temperaturen ved å kjøre dette signalet gjennom et lineært filter.
# Dere trenger ikke sette dere inn i detaljene i dette.

#taulist = np.array([0.5, 5, 50])
taulist = np.array([1,10,100])
F = net_forcing

# compute components: exp(-t/tau_n)*F(t) (Here * is a convolution)
dim = len(taulist)
lf = len(F)
predictors = np.full((lf,dim),np.nan)   

# compute exact predictors by integrating greens function
for k in range(0,dim):
    intgreensti = np.full((lf,lf),0.)
    for t in range(0,lf):
        # compute one new contribution to the matrix:
        intgreensti[t,0] = taulist[k]*(np.exp(-t/taulist[k]) - np.exp(-(t+1)/taulist[k]))
        
        # take the rest from row above:
        if t > 0:
            intgreensti[t,1:(t+1)] = intgreensti[t-1,0:t]
    # compute discretized convolution integral by this matrix product:
    predictors[:,k] = intgreensti@np.array(F)
    
# utfør linear regresjon mellom X og Y
Y = annualmeans[0:(2016-1850)]
X = predictors
X = sm.add_constant(X)

model1 = sm.OLS(Y,X)
results1 = model1.fit()
b = results1.params

Tn = b[1:]*predictors

residual = Y - X@b


# In[7]:


# plot data
fig, ax = plt.subplots(ncols=2, nrows=1, figsize = [18,5])
ax[0].plot(years,annualmeans,linewidth=2,color = "black")
ax[0].plot(years2,X@b,linewidth=2,color = "blue")
ax[0].set_ylabel('T(t)',fontsize = 18)
ax[0].set_title('Global temperature',fontsize = 18)
ax[0].set_xlabel('Year',fontsize = 18)
ax[0].grid()
ax[0].set_xlim(min(years),max(years))
ax[0].tick_params(axis='both',labelsize=20)

ax[1].plot(years2,residual,linewidth=2,color = "black");
ax[1].set_ylabel('T(t)',fontsize = 18)
ax[1].set_title('Global temperature residual',fontsize = 18)
ax[1].set_xlabel('Year',fontsize = 18)
ax[1].grid()
ax[1].set_xlim(min(years),max(years))
ax[1].tick_params(axis='both',labelsize=20)


# In[8]:


# acf av residual
from statsmodels.tsa.stattools import acf 

fig, ax = plt.subplots(figsize = [16,5])
ax.stem(acf(residual,nlags=25))
ax.plot(np.full(26,2/np.sqrt(n)),'--',color='gray')
ax.plot(np.full(26,-2/np.sqrt(n)),'--',color='gray')
ax.grid()
ax.tick_params(axis='both',labelsize=20)


# In[ ]:




