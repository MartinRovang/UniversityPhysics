#!/usr/bin/env python
# coding: utf-8

# # Fourieranalyse

# ## - Tenker på signaler/tidsrekker som summer av periodiske funksjoner:

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
from numpy import cos, sin, pi

L = 500
timestep = 1
t = np.arange(0,L,timestep)
p1 = np.array([2*cos(2*pi*t/60) for t in range(L)])
p2 = np.array([2*cos(2*pi*t/30) for t in range(L)])
p3 = np.array([2*cos(2*pi*t/15-2) for t in range(L)])
p4 = np.array([2*cos(2*pi*t/3+10) for t in range(L)])
p5 = np.array([2*cos(2*pi*t/8) for t in range(L)])
p6 = np.array([3*cos(2*pi*t/10+5) for t in range(L)])
x = p1 + p2 + p3 + p4 + p5 + p6

# plott
fig, ax = plt.subplots(nrows=2,ncols=1,figsize = [18,6])
ax[0].plot(t,p1,linewidth=2); 
ax[0].plot(t,p2,linewidth=2); 
ax[0].plot(t,p3,linewidth=2); 
#ax[0].plot(t,p4,linewidth=2); 
#ax[0].plot(t,p5,linewidth=2); 
#ax[0].plot(t,p6,linewidth=2); 
ax[0].grid()
ax[0].set_ylim([-3,3])
ax[0].set_xlim([0,L])
ax[0].tick_params(axis='both',labelsize=18)

ax[1].plot(t,x,linewidth=2,color = "black"); 
ax[1].grid()
ax[1].set_ylim([-10,15])
ax[1].set_xlim([0,L])
ax[1].tick_params(axis='both',labelsize=18)


# ## FFT (Fast Fourier Transform)

# In[3]:


# FFT: En rask algoritme for å beregne den diskrete Fouriertransformen

x = p1 + p3 + p5
# numpy har en modul som heter fft, og den har igjen en funskjon fft:
dft = np.fft.fft(x)

freq = np.fft.fftfreq(L, d=timestep)
f = np.array([m/(L*timestep) for m in range(0,L)])

fig, ax = plt.subplots(figsize = [18,6])
ax.plot(freq, dft.real, label = "real")
ax.plot(freq, dft.imag, label = "im")
ax.set_xlabel('Frequency (f)',fontsize = 18)
ax.legend(fontsize = 18)
ax.tick_params(axis='both',labelsize=18)


# In[4]:


# Merk:
# Realdel symmetrisk om 0-frekvensen
# Imaginærdel: verdier på negative frekvenser har motsatt fortegn av positive frekvenser


# In[5]:


fig, ax = plt.subplots(figsize = [18,6])
ax.plot(f, dft.real, label = "real")
ax.plot(f, dft.imag, label = "im")
ax.set_xlabel('Frequency (f)',fontsize = 18)
ax.legend(fontsize = 18)
ax.tick_params(axis='both',labelsize=18)


# ## Rekonstruer signalet igjen med den inverse transformen:

# In[7]:


x_reconstructed = np.fft.ifft(dft)

fig, ax = plt.subplots(figsize = [18,6])
ax.plot(t,x_reconstructed, color = "black")
ax.plot(t,x) # ser at plottene overlapper helt
ax.set_xlabel('t',fontsize = 18)
ax.tick_params(axis='both',labelsize=18)


# In[ ]:




