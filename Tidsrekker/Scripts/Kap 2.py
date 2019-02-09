#!/usr/bin/env python
# coding: utf-8

# # Kap 2

# In[4]:


import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

filedir = '/Users/hege-beatefredriksen/OneDrive - UiT Office 365/Teaching/STA-2003spring2019/Data/saved_from_astsa'

# load cmort data
filename = 'cmort.txt'
file = os.path.join(filedir, filename)
datatable = pd.read_table(file,sep='\t',engine='python')
year=datatable.iloc[:,0].values
cmort=datatable.iloc[:,1].values
n=len(cmort)
print(len(cmort))

# load part data
filename = 'tempr.txt'
file = os.path.join(filedir, filename)
datatable = pd.read_table(file,sep='\t',engine='python')
tempr=datatable.iloc[:,1].values
print(len(tempr))

# load part data
filename = 'part.txt'
file = os.path.join(filedir, filename)
datatable = pd.read_table(file,sep='\t',engine='python')
part=datatable.iloc[:,1].values
print(len(part))

# plot data
fig, ax = plt.subplots(ncols=1,nrows=3,figsize = [18,12])
ax[0].plot(year,cmort);
#ax[0].set_xlabel('Year',fontsize = 18)
ax[0].set_title('Cardiovascular mortality',fontsize = 18)
ax[0].grid()
ax[0].set_xlim(min(year),1980)
ax[0].tick_params(axis='both',labelsize=18)

ax[1].plot(year,tempr);
#ax[1].set_xlabel('Year',fontsize = 18)
ax[1].set_title('Temperature',fontsize = 18)
ax[1].grid()
ax[1].set_xlim(min(year),1980)
ax[1].tick_params(axis='both',labelsize=18)

ax[2].plot(year,part);
ax[2].set_xlabel('Year',fontsize = 18)
ax[2].set_title('Particulates',fontsize = 18)
ax[2].grid()
ax[2].set_xlim(min(year),1980)
ax[2].tick_params(axis='both',labelsize=18)


# In[5]:


# Det fins flere måter å estimere lineære trender på i Python,
# men vi skal bruke mest metoden i Statsmodels. Den ligner mest på R,
# og gir oss dermed mye statistikk på resultatet.


# In[6]:


# utfør linear regresjon mellom X og Y
Y = cmort
X = year - year[0]
X = sm.add_constant(X) # NB: må spesifiseres dersom vi skal ha konstantledd i modellen.

model1 = sm.OLS(Y,X)
results1 = model1.fit()
results1.params


# In[7]:


print(results1.summary())


# In[8]:


# Sjekk hva "results1" inneholder:
#dir(results1)


# In[9]:


# plot trend together with data
fig, ax = plt.subplots(figsize = [18,6])
ax.plot(year,cmort);
ax.plot(year,results1.fittedvalues)
ax.set_xlabel('Year',fontsize = 18)
ax.set_title('Cardiovascular mortality',fontsize = 18)
ax.grid()
ax.set_xlim(min(year),1980)
ax.tick_params(axis='both',labelsize=18)


# ## legg til flere prediktorer

# In[10]:


# Som i Eq. (2.19-2.21) i boka:

# prediktorer:
Z1 = year - year[0]
Z2 = tempr - tempr.mean()
Z3 = Z2**2
Z4 = part


# In[11]:


# utfør linear regresjon mellom X og Y
Y = cmort
X = np.column_stack((Z1, Z2))
X = sm.add_constant(X) # NB: må spesifiseres dersom vi skal ha konstantledd i modellen.

model2 = sm.OLS(Y,X)
results2 = model2.fit()
results2.params

# plot fit together with data
fig, ax = plt.subplots(figsize = [18,6])
ax.plot(year,cmort);
ax.plot(year,results2.fittedvalues)
ax.set_xlabel('Year',fontsize = 18)
ax.set_title('Cardiovascular mortality',fontsize = 18)
ax.grid()
ax.set_xlim(min(year),1980)
ax.tick_params(axis='both',labelsize=18)


# In[12]:


# utfør linear regresjon mellom X og Y
Y = cmort
X = np.column_stack((Z1, Z2, Z3))
X = sm.add_constant(X) # NB: må spesifiseres dersom vi skal ha konstantledd i modellen.

model3 = sm.OLS(Y,X)
results3 = model3.fit()
results3.params

# plot fit together with data
fig, ax = plt.subplots(figsize = [18,6])
ax.plot(year,cmort);
ax.plot(year,results3.fittedvalues)
ax.set_xlabel('Year',fontsize = 18)
ax.set_title('Cardiovascular mortality',fontsize = 18)
ax.grid()
ax.set_xlim(min(year),1980)
ax.tick_params(axis='both',labelsize=18)


# In[13]:


# utfør linear regresjon mellom X og Y
Y = cmort
X = np.column_stack((Z1, Z2, Z3, Z4))
X = sm.add_constant(X) # NB: må spesifiseres dersom vi skal ha konstantledd i modellen.

model4 = sm.OLS(Y,X)
results4 = model4.fit()
results4.params

# plot fit together with data
fig, ax = plt.subplots(figsize = [18,6])
ax.plot(year,cmort);
ax.plot(year,results4.fittedvalues)
ax.set_xlabel('Year',fontsize = 18)
ax.set_title('Cardiovascular mortality',fontsize = 18)
ax.grid()
ax.set_xlim(min(year),1980)
ax.tick_params(axis='both',labelsize=18)


# ## AIC og BIC

# In[14]:


# Funksjon som konverterer definisjonen av AIC og BIC i Python/R til definisjonen i læreboka:
# Input: AIC/BIC beregnet i python, og lengden på tidsrekka
def aic_textbook(aic_python,n):
    return aic_python/n - np.log(2*np.pi)


# In[15]:


aic_array = np.array([[results1.aic], [results2.aic], [results3.aic], [results4.aic]])
aic_array_textbook = aic_textbook(aic_array,n)
rsquared_array = np.array([[results1.rsquared], [results2.rsquared], [results3.rsquared], [results4.rsquared]])

bic_array = np.array([[results1.bic], [results2.bic], [results3.bic], [results4.bic]])
bic_array_textbook = aic_textbook(bic_array,n)

mse_array = np.array([[results1.mse_resid], [results2.mse_resid], [results3.mse_resid], [results4.mse_resid]])

datatable = np.concatenate((aic_array, bic_array, aic_array_textbook, bic_array_textbook, rsquared_array, mse_array),axis=1)
row_labels = ['model1 (2.18)','model2 (2.19)','model3 (2.20)','model4 (2.21)']

df = pd.DataFrame(datatable, columns=['AIC', 'BIC', 'AIC as in textbook', 'BIC as in textbook', 'R$^2$', 'MSE'], index=row_labels)
df


# ## Lineær regresjon for å estimere periodisiter (Ex. 2.10 i boka)

# In[36]:


from numpy import cos, sin, pi

w = np.array([random.gauss(0, 5) for i in range(500)])

t = np.arange(0,500)
s = np.array([2*cos(2*pi*(t+15)/50) for t in range(500)])
x = s + w

# plott
fig, ax = plt.subplots(figsize = [18,6])
ax.plot(t,x,linewidth=2,color = "black"); 
ax.plot(t,s,linewidth=2,color = "red")
ax.grid()
ax.set_ylim([-15,15])
ax.set_xlim([0,500])
ax.tick_params(axis='both',labelsize=18)


# In[38]:


# Hvis vi nå antar at vi ikke kjenner styrken på den periodiske komponenten, klarer vi å estimere det?

z1 = cos(2*pi*t/50)
z2 = sin(2*pi*t/50)

# utfør linear regresjon mellom X og Y
Y = x
X = np.column_stack((z1, z2))

model = sm.OLS(Y,X)
results = model.fit()
results.params

# plot fit together with data
fig, ax = plt.subplots(figsize = [18,6])
ax.plot(x, linewidth=2, color = "black");
ax.plot(results.fittedvalues,linewidth=3)
ax.grid()
ax.set_ylim([-15,15])
ax.set_xlim([0,500])
ax.tick_params(axis='both',labelsize=18)


# In[ ]:




