#!/usr/bin/env python
# coding: utf-8

# # Kap 3

# ## Eksempel fra tidligere:

# In[2]:


import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf 

filedir = '/Users/hege-beatefredriksen/OneDrive - UiT Office 365/Teaching/STA-2003spring2019/Data/saved_from_astsa'
filename = 'soi.txt'

file = os.path.join(filedir, filename)

# load data
datatable = pd.read_table(file,sep='\t',engine='python')
year=datatable.iloc[:,0].values
soi=datatable.iloc[:,1].values

n=len(soi)

fig, ax = plt.subplots(ncols=1,nrows=2,figsize = [16,10])
ax[0].plot(year,soi);
ax[0].set_xlabel('Year',fontsize = 18)
ax[0].set_title('Southern Oscillation index',fontsize = 18)
ax[0].grid()
ax[0].set_xlim(min(year),max(year))
ax[0].tick_params(axis='both',labelsize=18)

ax[1].stem(np.arange(49)/12,acf(soi,nlags=4*12))
#ax[1].plot(np.arange(49)/12,np.full(49,2/np.sqrt(n)),'--',color='gray')
#ax[1].plot(np.arange(49)/12,np.full(49,-2/np.sqrt(n)),'--',color='gray')
ax[1].grid()
ax[1].set_ylabel('ACF',fontsize = 18)
ax[1].set_xlabel('Time lag (years)',fontsize = 18)
ax[1].tick_params(axis='both',labelsize=18)


# In[3]:


# compute mean january value, mean february value, etc.
C = np.zeros(12)
for m in range(0,12):
    C[m] = np.mean(soi[m::12])  # take out every 12th element, then compute mean

plt.plot(C)


# In[4]:


# repeat C to create a periodic signal of equal length or longer than the dataset
repC = np.tile(C,int(np.ceil(len(soi)/12)))
# compute residual (by subtracting periodic signal)
residual = soi - repC[:len(soi)]

fig, ax = plt.subplots(ncols=1,nrows=2,figsize = [16,10])
ax[0].plot(year,residual);
ax[0].set_xlabel('Year',fontsize = 18)
ax[0].set_title('Deseasonalized Southern Oscillation index',fontsize = 18)
ax[0].grid()
ax[0].set_xlim(min(year),max(year))
ax[0].tick_params(axis='both',labelsize=18)

maxlag = 4*12
ax[1].stem(np.arange(49)/12,acf(residual,nlags=maxlag))
ax[1].plot(np.arange(0, maxlag+1)/12,np.full(maxlag+1,2/np.sqrt(n)),'--',color='gray')
ax[1].plot(np.arange(0, maxlag+1)/12,np.full(maxlag+1,-2/np.sqrt(n)),'--',color='gray')
ax[1].grid()
ax[1].set_ylabel('ACF',fontsize = 18)
ax[1].set_xlabel('Time lag (years)',fontsize = 18)
ax[1].tick_params(axis='both',labelsize=18)


# ## Simuler AR(1):

# In[5]:


import numpy as np
import matplotlib.pyplot as plt
import random
from statsmodels.tsa.stattools import acf 

N = 1000
phi = 0.9

w = [random.gauss(0, 1) for i in range(N)]
x = np.zeros(N)

# sett initialverdi
x[0] = random.gauss(0,1)

for i in range(1,N):
    x[i] = phi*x[i-1] + w[i]
    
# plott
fig, ax = plt.subplots(nrows = 2, ncols = 1, figsize = [15,10])
ax[0].plot(x,linewidth=2,color = "blue"); 
ax[0].set_title('Simulering av AR(1)-prosess med $\phi =$' + str(phi), fontsize = 18)
ax[0].grid()
ax[0].tick_params(axis='both',labelsize=18)

maxlag = 20
ax[1].stem(np.arange(maxlag+1),acf(x,nlags=maxlag))
ax[1].plot(np.arange(maxlag+1),np.full(maxlag+1,2/np.sqrt(N)),'--',color='gray')
ax[1].plot(np.arange(maxlag+1),np.full(maxlag+1,-2/np.sqrt(N)),'--',color='gray')
ax[1].grid()
ax[1].set_title('ACF av tidsrekka ovenfor',fontsize = 18)
ax[1].set_xlabel('h',fontsize = 18)
ax[1].tick_params(axis='both',labelsize=18)


# ## Simuler MA(1):

# In[6]:


import numpy as np
import matplotlib.pyplot as plt
import random
from statsmodels.tsa.stattools import acf 

N = 500
theta = 0.9

w = [random.gauss(0, 1) for i in range(N+1)] # trenger å inneholde 1 verdi mer enn x
x = np.zeros(N+1)

for i in range(1,N+1):
    x[i] = theta*w[i-1] + w[i]
    
# får ikke fylt inn noe på index 0, så fjerner denne:
x = x[1:]
    
# plott
fig, ax = plt.subplots(nrows = 2, ncols = 1, figsize = [15,10])
ax[0].plot(x,linewidth=2,color = "blue"); 
ax[0].set_title('Simulering av MA(1)-prosess med $\Theta =$' + str(theta), fontsize = 18)
ax[0].grid()
ax[0].tick_params(axis='both',labelsize=18)

maxlag = 20
ax[1].stem(np.arange(maxlag+1),acf(x,nlags=maxlag))
ax[1].plot(np.arange(maxlag+1),np.full(maxlag+1,2/np.sqrt(N)),'--',color='gray')
ax[1].plot(np.arange(maxlag+1),np.full(maxlag+1,-2/np.sqrt(N)),'--',color='gray')
ax[1].grid()
ax[1].set_title('ACF av tidsrekka ovenfor',fontsize = 18)
ax[1].set_xlabel('h',fontsize = 18)
ax[1].tick_params(axis='both',labelsize=18)

print(theta/(1+theta**2))


# ## Convert ARMA to AR or MA

# In[7]:


from statsmodels.tsa.arima_process import arma2ma
from statsmodels.tsa.arima_process import arma2ar

# Eksempel 3.8 i boka:
phi = [1, -0.9] # autoregressive parameters
theta = [1, 0.5] # moving average parameters
arma2ma(phi, theta, lags = 10) # tar også med psi_0 = 1.


# In[8]:


arma2ar(phi, theta, lags = 10) # tar også med pi_0 = 1.


# In[ ]:




