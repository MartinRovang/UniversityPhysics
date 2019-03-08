#!/usr/bin/env python
# coding: utf-8

# ## MA(1) eksempel

# In[3]:


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

# In[4]:


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

# In[5]:


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


# In[6]:


# har også en funksjon som gir oss frekvensene:
freq = np.fft.fftfreq(N, d=timestep)
freq


# In[7]:


fig, ax = plt.subplots(figsize = [12,4])
ax.plot(freq, np.full(len(freq),sigma_w**2),'-.', linewidth=2, color = "gray");
ax.plot(freq, dft_wn, linewidth=2, color = "black")
ax.grid()
ax.set_xlim(-1/(2*timestep),1/(2*timestep))
ax.tick_params(axis='both',labelsize=18)

# ser at vi plotter først positive frekvenser, deretter begynner vi på de negative.
# punktet helt til venstre plottes dermed rett etter puntet helt til høyre,
# og de blir dermed forbundet med en rett linje.


# In[8]:


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


# In[9]:


N=10
conv = signal.convolve(np.ones(N)/np.sqrt(N), np.ones(N)/np.sqrt(N), mode='full')
plt.stem(conv)


# In[10]:


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


# In[11]:


f = np.arange(-1/2, 1/2, 0.001)
N = 100 # øk N, og se konvergens mot en delta-funksjon

fig, ax = plt.subplots(figsize = [10,7])
ax.plot(f,1/N*sin(N*pi*f)**2/sin(pi*f)**2, linewidth=1, color = "red")
ax.grid()
ax.set_xlim(-1/2,1/2)
#ax.set_ylim(-1,1) # need to zoom in to see the differences
ax.tick_params(axis='both',labelsize=18)


# ## Eksempel

# In[12]:


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

# In[13]:


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

# In[14]:


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


# ## Windows / tapers (beregnet for delta_t = 1)

# In[16]:


import numpy as np
import matplotlib.pyplot as plt
from numpy import cos, sin, pi, exp

N = 30;

# rektangulært vindu:
w = np.ones(30)
U = 1/N*sum(w**2)

fig, ax = plt.subplots(figsize = [8,5])
ax.stem(w)
ax.grid()
ax.tick_params(axis='both',labelsize=18)


# In[17]:


f_fourier = np.fft.fftfreq(N)
Q = 1/(N*U)*abs(np.fft.fft(w))**2

f_highres = np.linspace(0,1/2,N*100)
N_f = len(f_highres)
t = np.arange(0,N);
i = 1j;

w_dtft = np.full(N_f,np.nan)

for k in range(0,N_f):
    w_dtft[k] = 1/N*abs(sum(w*exp(-i*2*pi*f_highres[k]*t)))**2

fig, ax = plt.subplots(figsize = [8,5])
ax.stem(f_fourier[f_fourier>=0],Q[f_fourier>=0]) # plott punkter på fourierfrekvensene
ax.plot(f_highres,w_dtft) # plott en kurve som ser glatt ut ved å beregne DTFT for flere frekvenser
ax.grid()
ax.tick_params(axis='both',labelsize=18)


# In[18]:


def dB(x):
    return 10*np.log10(x/x[0])

fig, ax = plt.subplots(nrows=1,ncols=2,figsize = [16,5])
ax[0].stem(w)
ax[0].grid()
ax[0].tick_params(axis='both',labelsize=18)
ax[0].set_title('Window',fontsize = 18)

ax[1].plot(f_highres,dB(w_dtft)) # plott en kurve som ser glatt ut ved å beregne DTFT for flere frekvenser
ax[1].grid()
ax[1].set_xlim(0,1/2)
ax[1].set_ylim(-60,0) 
ax[1].tick_params(axis='both',labelsize=18)
ax[1].set_ylabel('dB',fontsize = 18);
ax[1].set_xlabel('f',fontsize = 18);
ax[1].set_title('Q(f)',fontsize = 18)


# In[19]:


# Triangular
#w = np.array([(N/2-abs(k))*2/N for k in range(-int(N/2), int(N/2))]) # with sharp top
w1 = np.array([(abs(k))*2/N for k in range(0, int(N/2))])
w = np.concatenate([w1, np.flip(w1)])
U = 1/N*sum(w**2)

w_dtft = np.full(N_f,np.nan)

for k in range(0,N_f):
    w_dtft[k] = 1/N*abs(sum(w*exp(-i*2*pi*f_highres[k]*t)))**2

fig, ax = plt.subplots(nrows=1,ncols=2,figsize = [16,5])
ax[0].stem(w)
ax[0].grid()
ax[0].set_ylim(0,1) 
ax[0].tick_params(axis='both',labelsize=18)
ax[0].set_title('Window',fontsize = 18)

ax[1].plot(f_highres,dB(w_dtft)) # plott en kurve som ser glatt ut ved å beregne DTFT for flere frekvenser
ax[1].grid()
ax[1].set_xlim(0,1/2)
ax[1].set_ylim(-60,0) 
ax[1].tick_params(axis='both',labelsize=18)
ax[1].set_ylabel('dB',fontsize = 18);
ax[1].set_xlabel('f',fontsize = 18);
ax[1].set_title('Q(f)',fontsize = 18);


# In[20]:


# Hann
w = np.array([1/2*(1 - cos(2*pi*k/(N-1))) for k in range(0, N)])
U = 1/N*sum(w**2)

w_dtft = np.full(N_f,np.nan)

for k in range(0,N_f):
    w_dtft[k] = 1/N*abs(sum(w*exp(-i*2*pi*f_highres[k]*t)))**2

fig, ax = plt.subplots(nrows=1,ncols=2,figsize = [16,5])
ax[0].stem(w)
ax[0].grid()
ax[0].tick_params(axis='both',labelsize=18)
ax[0].set_title('Hann window',fontsize = 18)

ax[1].plot(f_highres,dB(w_dtft)) # plott en kurve som ser glatt ut ved å beregne DTFT for flere frekvenser
# oppgave øving 8: Beregn analytisk uttrykk for den glatte kurven
ax[1].grid()
ax[1].set_xlim(0,1/2)
ax[1].set_ylim(-60,0) 
ax[1].tick_params(axis='both',labelsize=18)
ax[1].set_ylabel('dB',fontsize = 18);
ax[1].set_xlabel('f',fontsize = 18);
ax[1].set_title('Q(f)',fontsize = 18);


# In[21]:


# Hamming
w = np.array([0.54-0.46*cos(2*pi*k/(N-1)) for k in range(0, N)])
U = 1/N*sum(w**2)

w_dtft = np.full(N_f,np.nan)

for k in range(0,N_f):
    w_dtft[k] = 1/N*abs(sum(w*exp(-i*2*pi*f_highres[k]*t)))**2

fig, ax = plt.subplots(nrows=1,ncols=2,figsize = [16,5])
ax[0].stem(w)
ax[0].grid()
ax[0].tick_params(axis='both',labelsize=18)
ax[0].set_title('Hamming window',fontsize = 18)

ax[1].plot(f_highres,dB(w_dtft)) # plott en kurve som ser glatt ut ved å beregne DTFT for flere frekvenser
# oppgave øving 8: Beregn analytisk uttrykk for den glatte kurven
ax[1].grid()
ax[1].set_xlim(0,1/2)
ax[1].set_ylim(-60,0) 
ax[1].tick_params(axis='both',labelsize=18)
ax[1].set_ylabel('dB',fontsize = 18);
ax[1].set_xlabel('f',fontsize = 18);
ax[1].set_title('Q(f)',fontsize = 18);


# ## plott alle i samme figur, slik som Fig. 7.1 i kompendiet

# In[22]:



fig, ax = plt.subplots(nrows=4,ncols=2,figsize = [16,20])

N = 30

# rektangulært vindu:
w = np.ones(30)
U = 1/N*sum(w**2)
f_fourier = np.fft.fftfreq(N)
Q = 1/(N*U)*abs(np.fft.fft(w))**2
f_highres = np.linspace(0,1/2,N*100)
N_f = len(f_highres)
t = np.arange(0,N);
i = 1j;
w_dtft = np.full(N_f,np.nan)
for k in range(0,N_f):
    w_dtft[k] = 1/N*abs(sum(w*exp(-i*2*pi*f_highres[k]*t)))**2

ax[0,0].stem(w)
ax[0,0].grid()
ax[0,0].tick_params(axis='both',labelsize=18)
ax[0,0].set_title('Rectangular',fontsize = 18)

ax[0,1].plot(f_highres,dB(w_dtft)) # plott en kurve som ser glatt ut ved å beregne DTFT for flere frekvenser
ax[0,1].grid()
ax[0,1].set_xlim(0,1/2)
ax[0,1].set_ylim(-60,0) 
ax[0,1].tick_params(axis='both',labelsize=18)
ax[0,1].set_ylabel('dB',fontsize = 18);
#ax[0,1].set_xlabel('f',fontsize = 18);
ax[0,1].set_title('Q(f)',fontsize = 18)

# Triangular
#w = np.array([(N/2-abs(k))*2/N for k in range(-int(N/2), int(N/2))]) # with sharp top
w1 = np.array([(abs(k))*2/N for k in range(0, int(N/2))])
w = np.concatenate([w1, np.flip(w1)])
U = 1/N*sum(w**2)
w_dtft = np.full(N_f,np.nan)
for k in range(0,N_f):
    w_dtft[k] = 1/N*abs(sum(w*exp(-i*2*pi*f_highres[k]*t)))**2

ax[1,0].stem(w)
ax[1,0].grid()
ax[1,0].set_ylim(0,1) 
ax[1,0].tick_params(axis='both',labelsize=18)
ax[1,0].set_title('Triangular',fontsize = 18)

ax[1,1].plot(f_highres,dB(w_dtft)) # plott en kurve som ser glatt ut ved å beregne DTFT for flere frekvenser
ax[1,1].grid()
ax[1,1].set_xlim(0,1/2)
ax[1,1].set_ylim(-60,0) 
ax[1,1].tick_params(axis='both',labelsize=18)
ax[1,1].set_ylabel('dB',fontsize = 18);
#ax[1,1].set_xlabel('f',fontsize = 18);
ax[1,1].set_title('Q(f)',fontsize = 18);

# Hann
w = np.array([1/2*(1 - cos(2*pi*k/(N-1))) for k in range(0, N)])
U = 1/N*sum(w**2)
w_dtft = np.full(N_f,np.nan)
for k in range(0,N_f):
    w_dtft[k] = 1/N*abs(sum(w*exp(-i*2*pi*f_highres[k]*t)))**2

ax[2,0].stem(w)
ax[2,0].grid()
ax[2,0].tick_params(axis='both',labelsize=18)
ax[2,0].set_title('Hann window',fontsize = 18)

ax[2,1].plot(f_highres,dB(w_dtft)) # plott en kurve som ser glatt ut ved å beregne DTFT for flere frekvenser
# oppgave øving 8: Beregn analytisk uttrykk for den glatte kurven
ax[2,1].grid()
ax[2,1].set_xlim(0,1/2)
ax[2,1].set_ylim(-60,0) 
ax[2,1].tick_params(axis='both',labelsize=18)
ax[2,1].set_ylabel('dB',fontsize = 18);
#ax[2,1].set_xlabel('f',fontsize = 18);
ax[2,1].set_title('Q(f)',fontsize = 18);


# Hamming
w = np.array([0.54-0.46*cos(2*pi*k/(N-1)) for k in range(0, N)])
U = 1/N*sum(w**2)
w_dtft = np.full(N_f,np.nan)
for k in range(0,N_f):
    w_dtft[k] = 1/N*abs(sum(w*exp(-i*2*pi*f_highres[k]*t)))**2
    
ax[3,0].stem(w)
ax[3,0].grid()
ax[3,0].tick_params(axis='both',labelsize=18)
ax[3,0].set_title('Hamming window',fontsize = 18)

ax[3,1].plot(f_highres,dB(w_dtft)) # plott en kurve som ser glatt ut ved å beregne DTFT for flere frekvenser
# oppgave øving 8: Beregn analytisk uttrykk for den glatte kurven
ax[3,1].grid()
ax[3,1].set_xlim(0,1/2)
ax[3,1].set_ylim(-60,0) 
ax[3,1].tick_params(axis='both',labelsize=18)
ax[3,1].set_ylabel('dB',fontsize = 18);
ax[3,1].set_xlabel('f',fontsize = 18);
ax[3,1].set_title('Q(f)',fontsize = 18);


# In[ ]:




