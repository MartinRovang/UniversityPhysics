
# coding: utf-8

# # Stokastiske prosesser

# ## Generer ett tilfeldig tall:

# In[6]:


import random
#random.seed(1)
random.gauss(0,1)
# trekker et tall fra en normalfordeling med gjennomsnitt: 0, og standardavvik: 1


# ## Generer en serie med tilfeldige tall:

# In[7]:


[random.gauss(0, 1) for i in range(10)]


# In[8]:


import matplotlib.pyplot as plt

w = [random.gauss(0, 1) for i in range(500)]

# plott
fig, ax = plt.subplots(figsize = [10,5])
plt.plot(w,linewidth=2,color = "black");

# Tilsvarer eksempel 1.8 i læreboka


# ## Moving average / glidende gjennomsnitt / rolling mean

# In[9]:


# Se eksempel 1.9 i læreboka

import pandas as pd
df = pd.DataFrame(w)
v = df.rolling(3,center=True).mean()
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rolling.html


# In[11]:


# plott
fig, ax = plt.subplots(figsize = [10,5])
ax.plot(w,linewidth=2,color = "black")
ax.plot(v,linewidth=2,color = "blue"); 
#ax.set_xlim(0,10)


# ## Autoregressive modell

# In[12]:


# Se eksempel 1.10 i læreboka
import numpy as np

x = np.zeros(len(w))
# sett initialverdier
x[0] = random.gauss(0,1)
x[1] = random.gauss(0,1)

for i in range(2,len(x)):
    x[i] = x[i-1] - 0.9*x[i-2] + w[i]


# In[13]:


# plott
fig, ax = plt.subplots(figsize = [10,5])
ax.plot(x,linewidth=2,color = "blue"); 


# ## Random walk

# In[14]:


# Se eksempel 1.11 i læreboka

# plott flere realisasjoner
fig, ax = plt.subplots(figsize = [10,5])

for i in range(10):
    wi = [random.gauss(0, 1) for i in range(500)]
    xi = np.cumsum(wi)
    ax.plot(xi,linewidth=2,color = "blue"); 


# ## Random walk med drift

# In[15]:


# Se eksempel 1.11 i læreboka

delta = 0.2

fig, ax = plt.subplots(figsize = [10,5])
t = np.arange(0,500)

for i in range(10):
    wi = [random.gauss(0, 1) for i in range(500)]
    xi = np.cumsum(wi) + delta*t
    ax.plot(xi,linewidth=2,color = "red"); 
    ax.plot(delta*t,linewidth=2,color = "black")


# ## Periodisk signal

# In[18]:


from numpy import cos, pi
#w = np.array([random.gauss(0, 1) for i in range(500)])
w = np.array([random.gauss(0, 25) for i in range(500)])

t = np.arange(0,500)
s = np.array([2*cos(2*pi*(t+15)/50) for t in range(500)])
x = s + w

# plott
fig, ax = plt.subplots(figsize = [10,5])
ax.plot(t,x,linewidth=2,color = "black"); 
ax.plot(t,s,linewidth=2,color = "red")

