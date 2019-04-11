
# coding: utf-8

# # Nino 3.4 index

# In[1]:


import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels as sm
from statsmodels.tsa.stattools import acf, pacf


# In[2]:


file = 'nino3_4.txt'

# load data
datatable = pd.read_table(file,sep='\s',engine='python',skipfooter=3,header=None)
years=datatable.iloc[:,0].values
data = datatable.iloc[:,2::2].values.flatten() # les data fra annenhver kolonne
data = data[:-10] # mangler data for de siste 10 månedene i tabellen
months = np.arange(years[0],years[-1]+1,1/12)
months = months[:-10]


# ## Trekk fra sesongvariasjoner:

# In[3]:


# compute mean january value, mean february value, etc.
C = np.zeros(12)
for m in range(0,12):
    C[m] = np.mean(data[m::12])  # take out every 12th element, then compute mean

plt.plot(C);

# repeat C to create a periodic signal of equal length or longer than the dataset
repC = np.tile(C,int(np.ceil(len(data)/12)))
# compute residual (by subtracting periodic signal)
x = data - repC[:len(data)]

plt.plot(data)
plt.plot(x)
plt.show()


# In[4]:


months[-45] # bruker perioden fram til juni 2015 for å lage en prediksjon,
#  som vi deretter kan sammenligne med den faktiske utviklingen av tidsrekka.


# In[5]:


y = x[:-45]

fig, ax = plt.subplots(figsize = [12,6])
ax.plot(months[:-45],y)
ax.plot(months[-45:],x[-45:])


# In[6]:


plt.stem(pacf(y))


# In[7]:


model = sm.tsa.arima_model.ARIMA(y, order=(2, 0, 0))
model_fit = model.fit()

print(model_fit.summary())


# In[8]:


M = 36
forecast, stderr, conf_int = model_fit.forecast(steps=M)
# gir ut forecast, std, (1-alpha)% konfidensintervall. Default: 95% konfidensintervall


# In[9]:


fig, ax = plt.subplots(figsize = [12,6])
ax.plot(months[:-45],y)
ax.plot(months[-45:],x[-45:])
ax.plot(months[-45:-45+M],forecast)
ax.fill_between(months[-45:-45+M], conf_int[:,0], conf_int[:,1],alpha = 0.5)
plt.show()

# ## Finn residualene fra modellen

# In[10]:


res = model_fit.resid
plt.plot(res)

