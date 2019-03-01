#!/usr/bin/env python
# coding: utf-8

# ## MA(1) eksempel

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
from numpy import cos, sin, pi
from scipy import signal

sigma_w = 1
wn = np.random.normal(loc=0, scale=sigma_w, size=100)

# vanlig moving average 
a = np.array([1, 0.5])
filtered = signal.convolve(wn, a, mode='same')

# plott data
fig, ax = plt.subplots(figsize = [12,4])
ax.plot(wn,linewidth=2,color = "black");
ax.plot(filtered,linewidth=2, color = "red")
ax.grid()
ax.set_xlim(0,100)
ax.tick_params(axis='both',labelsize=18)


# ### Spekter:

# In[3]:


# plott data
omega = np.arange(-pi, pi, 0.01)
S_X = np.array([sigma_w**2*(1.25+cos(omega_i)) for omega_i in omega])

fig, ax = plt.subplots(figsize = [12,4])
ax.plot(omega, np.full(len(omega),sigma_w**2), linewidth=2, color = "black");
ax.plot(omega, S_X, linewidth=2, color = "red")
ax.grid()
ax.set_xlim(-pi,pi)
ax.tick_params(axis='both',labelsize=18)


# ## Estimering av spekter med periodogram:

# In[15]:


# genererer hvit støy, som i eksempel ovenfor
sigma_w = 1
N = 100
timestep = 1
wn = np.random.normal(loc=0, scale=sigma_w, size=N)

# beregn periodogrammet
dft_wn = timestep/N*np.abs(np.fft.fft(wn))**2

# beregn frekvenser
f = np.array([m/(N*timestep) for m in range(0,N)])

# plott
fig, ax = plt.subplots(figsize = [12,4])
ax.plot(f, np.full(len(f),sigma_w**2),'-.', linewidth=2, color = "gray");
ax.plot(f, dft_wn, linewidth=2, color = "black")
ax.grid()
ax.set_xlim(0,1/timestep)
ax.tick_params(axis='both',labelsize=18)


# In[16]:


# har også en funksjon som gir oss frekvensene:
freq = np.fft.fftfreq(N, d=timestep)
freq


# In[17]:


fig, ax = plt.subplots(figsize = [12,4])
ax.plot(freq, np.full(len(freq),sigma_w**2),'-.', linewidth=2, color = "gray");
ax.plot(freq, dft_wn, linewidth=2, color = "black")
ax.grid()
ax.set_xlim(-1/(2*timestep),1/(2*timestep))
ax.tick_params(axis='both',labelsize=18)

# ser at vi plotter først positive frekvenser, deretter begynner vi på de negative.
# punktet helt til venstre plottes dermed rett etter puntet helt til høyre,
# og de blir dermed forbundet med en rett linje.


# In[18]:


# flytter om på elementer i arrayene ved hjelp av fftshift-funksjonen:
S_fft = timestep/N*abs(np.fft.fft(wn))**2
freq = np.fft.fftfreq(N, d=timestep)
S_shift,f_shift = np.fft.fftshift([freq,S_fft])

# plott
fig, ax = plt.subplots(figsize = [12,4])
ax.plot(f_shift, np.full(len(f),sigma_w**2),'-.', linewidth=2, color = "gray");
ax.plot(f_shift, S_shift, linewidth=2, color = "black")
ax.grid()
ax.set_xlim(-1/(2*timestep),1/(2*timestep))
ax.tick_params(axis='both',labelsize=18)
ax.set_xlabel('$f$',fontsize = 18)
ax.set_ylabel('$\hat{S}^{(per)}(f)$',fontsize = 18);


# In[19]:


N=10
conv = signal.convolve(np.ones(N)/np.sqrt(N), np.ones(N)/np.sqrt(N), mode='full')
plt.stem(conv)


# In[20]:


# plot Dirichlet kernel and sinc together
f = np.arange(-1/2, 1/2, 0.001)
N = 50 # øk N, og se konvergens mot en delta-funksjon

fig, ax = plt.subplots(figsize = [10,7])
ax.plot(f,1/np.sqrt(N)*sin(N*pi*f)/(pi*f), linewidth=1, color = "black");
ax.plot(f,1/np.sqrt(N)*sin(N*pi*f)/sin(pi*f), linewidth=1, color = "red")
ax.grid()
ax.set_xlim(-1/2,1/2)
#ax.set_ylim(-1,1) # need to zoom in to see the differences
ax.tick_params(axis='both',labelsize=18)

# Liten forskjell på diskret tid og kontinuerlig fouriertransform her altså


# In[21]:


f = np.arange(-1/2, 1/2, 0.001)
N = 100 # øk N, og se konvergens mot en delta-funksjon

fig, ax = plt.subplots(figsize = [10,7])
ax.plot(f,1/N*sin(N*pi*f)**2/sin(pi*f)**2, linewidth=1, color = "red")
ax.grid()
ax.set_xlim(-1/2,1/2)
#ax.set_ylim(-1,1) # need to zoom in to see the differences
ax.tick_params(axis='both',labelsize=18)


# ## Eksempel

# In[22]:


A = 1; 
f0 = 0.2 + 0.5/100
#f0 = 0.2
dt = 1
t = np.arange(0,100,dt)
N = len(t)

theta = np.random.uniform(low=0, high=2*pi, size=1)
Xt = A*sin(2*pi*f0*t + theta)
#plt.plot(Xt)

# beregn periodogrammet
S_per = dt/N*abs(np.fft.fft(Xt))**2
freq = np.fft.fftfreq(N, d=dt)
S_shift,f_shift = np.fft.fftshift([freq,S_per])

fig, ax = plt.subplots(figsize = [10,7])
ax.stem(f_shift, S_shift)
ax.grid()
ax.set_xlim(-1/(2*dt),1/(2*dt))
#ax.set_ylim(0,0.2) # need to zoom in to see the differences
ax.tick_params(axis='both',labelsize=18)


# ## Eksempel

# In[23]:


A = 1; 
f0 = 0.2 +0.5/100
f1 = 0.3 +0.5/100
dt = 1
t = np.arange(0,100,dt)
N = len(t)

theta = np.random.uniform(low=0, high=2*pi, size=1)
Xt = sin(2*pi*f0*t) + sin(2*pi*f1*t)

# beregn periodogrammet
S_per = dt/N*abs(np.fft.fft(Xt))**2
freq = np.fft.fftfreq(N, d=dt)
S_shift,f_shift = np.fft.fftshift([freq,S_per])

fig, ax = plt.subplots(figsize = [10,7])
ax.stem(f_shift, S_shift)
ax.grid()
ax.set_xlim(-1/(2*dt),1/(2*dt))
#ax.set_ylim(0,0.2) 
ax.tick_params(axis='both',labelsize=18)


# ## Blackman-Tukey estimator

# In[26]:


# estimator av autokovarians (fra kap 1)
def sample_acvf(x,maxlag=None): #function consistent with Eq. (1.36) in textbook
    n = len(x)
    if maxlag==None:
        maxlag=n-1
    xmean = np.mean(x)
    gamma = np.zeros(maxlag+1)
    for h in range(0,maxlag+1):
        gamma[h] = 1/n*(x[h:]-xmean)@(x[:n-h]-xmean)
        #gamma[h] = 1/(n-h)*(x[h:]-xmean)@(x[:n-h]-xmean) # alternativ mindre brukt estimator
    return gamma

def S_BT(x,M): # Blackman-Tukey estimator for PSD. Must have M <= N - 1
    acvf_estimate = sample_acvf(x)
    acvf_fft = np.fft.fft(acvf_estimate)
    bt_estimator = acvf_fft[:M+1] + acvf_fft[:M+1].conjugate() - acvf_estimate[0]
    return bt_estimator

# beregn frekvenser
N = 100
f = np.array([m/(N*timestep) for m in range(0,N)])

# plott
fig, ax = plt.subplots(figsize = [12,4])
ax.plot(f, np.full(len(f),sigma_w**2),'-.', linewidth=2, color = "gray");
ax.plot(f, dft_wn, linewidth=2, color = "black")
ax.plot(f, S_BT(wn,N-1), linewidth=2, color = "red")
ax.grid()
ax.set_xlim(0,1/timestep)
ax.tick_params(axis='both',labelsize=18)

