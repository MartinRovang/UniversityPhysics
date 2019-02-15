#!/usr/bin/env python
# coding: utf-8

# # Glatting av tidsrekker

# ## Eksempel: Southern Oscillation Index (SOI)

# In[24]:


import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

filedir = '/Users/hege-beatefredriksen/OneDrive - UiT Office 365/Teaching/STA-2003spring2019/Data/saved_from_astsa'
filename = 'soi.txt'
file = os.path.join(filedir, filename)

# load data
datatable = pd.read_table(file,sep='\t',engine='python')
year=datatable.iloc[:,0].values
soi=datatable.iloc[:,1].values
n=len(soi)

# plott data
fig, ax = plt.subplots(figsize = [15,5])
ax.plot(year,soi,linewidth=2,color = "black");
ax.set_xlabel('Year',fontsize = 18)
ax.set_title('Southern Oscillation Index',fontsize = 18)
ax.grid()
ax.set_xlim(min(year),max(year))
ax.tick_params(axis='both',labelsize=18)


# ### Glatting ved å bruke Moving average

# In[27]:


L = 25 # antall punkter vi midler over
k = int(np.floor(L/2)) # antall punkter på hver side av tidspunktet vi midler rundt

data_glattet = np.full(n, np.nan) # array som er like stort som soi, og inneholder kun nan.

for t in range(k, n - k):
    data_glattet[t] = np.mean(soi[(t-k):(t+k+1)]) # må la indeksen gå til 1 mer enn det den skal stoppe på

# plott data
fig, ax = plt.subplots(figsize = [15,5])
ax.plot(year,soi,linewidth=2,color = "black");
ax.plot(year,data_glattet,linewidth=2,color = "red")
ax.set_xlabel('Year',fontsize = 18)
ax.set_title('Southern Oscillation Index',fontsize = 18)
ax.grid()
ax.set_xlim(min(year),max(year))
ax.tick_params(axis='both',labelsize=18)


# ## Glatting ved å bruke et glidende vektet gjennomsnitt (Kernel)

# In[28]:


# Noen eksempler på Kernels først:

boxcar = np.full(L,1/L)
boxcar2 = np.concatenate([[1/24], np.repeat(1/12, 11), [1/24]])
boxcar_padded = np.pad(boxcar,(L,L),mode='constant')
boxcar2_padded = np.pad(boxcar2,(L,L),mode='constant')
# legger til nuller i begynnelsen og slutten av "boxcar" 
# for å gjøre det lettere å se at dette er en "box"

normal = signal.gaussian(L, std=3) / np.sum(signal.gaussian(L, std=3))

fig, ax = plt.subplots(ncols=3,nrows=1,figsize = [20,4])
ax[0].plot(boxcar_padded,linewidth=2,color = "black");
ax[0].plot(boxcar_padded,'o',color = "black");
ax[1].plot(boxcar2_padded,linewidth=2,color = "black");
ax[1].plot(boxcar2_padded,'o',color = "black");
ax[2].plot(normal,linewidth=2,color = "black");
ax[2].plot(normal,'o',color = "black");


# In[33]:


L = 25 # antall punkter vi tar et vektet middel over
k = int(np.floor(L/2)) # antall punkter på hver side av tidspunktet vi midler rundt

data_glattet = np.full(n, np.nan) # array som er like stort som soi, og inneholder kun nan.

bandwidth = 1*12 # ganger med 12 fordi det er 12 datapunkter per år
sigma = 0.25/0.6745*bandwidth 
normal = signal.gaussian(L, std=sigma) / np.sum(signal.gaussian(L, std=sigma))
boxcar2 = np.concatenate([[0.5], np.repeat(1, L-2), [0.5]])/L

for t in range(k, n - k):
    #data_glattet[t] = boxcar2@soi[(t-k):(t+k+1)] # må la indeksen gå til 1 mer enn det den skal stoppe på
    data_glattet[t] = normal@soi[(t-k):(t+k+1)]
    
# plott data
fig, ax = plt.subplots(figsize = [15,5])
ax.plot(year,soi,linewidth=2,color = "black");
ax.plot(year,data_glattet,linewidth=2,color = "red")
ax.set_xlabel('Year',fontsize = 18)
ax.set_title('Southern Oscillation Index',fontsize = 18)
ax.grid()
ax.set_xlim(min(year),max(year))
ax.tick_params(axis='both',labelsize=18)




# ## Lowess (Locally Weighted Scatterplot Smoothing)

# In[6]:


import statsmodels.api as sm
l = sm.nonparametric.lowess(soi,year,return_sorted = False, frac=2/3)
l2 = sm.nonparametric.lowess(soi,year,return_sorted = False, frac=0.05)

# plott data
fig, ax = plt.subplots(figsize = [15,5])
ax.plot(year,soi,linewidth=2,color = "black");
ax.plot(year,l,linewidth=2,color = "red")
ax.plot(year,l2,linewidth=2,color = "blue")
ax.set_xlabel('Year',fontsize = 18)
ax.set_title('Southern Oscillation Index',fontsize = 18)
ax.grid()
ax.set_xlim(min(year),max(year))
ax.tick_params(axis='both',labelsize=18)


# In[7]:


filename = 'rec.txt'
file = os.path.join(filedir, filename)

# load data
datatable = pd.read_table(file,sep='\t',engine='python')
year=datatable.iloc[:,0].values
rec=datatable.iloc[:,1].values

# merk at vi nå sorterer verdiene før vi plotter dem i et scatter plot
l = sm.nonparametric.lowess(soi[:-6],rec[6:],return_sorted = True, frac=2/3) 
l2 = sm.nonparametric.lowess(soi[:-6],rec[6:],return_sorted = True, frac=0.05)

fig, ax = plt.subplots(figsize = [6,6])
ax.scatter(rec[6:],soi[:-6],color="black"); # ved time lag 6
ax.plot(l[:,0],l[:,1],linewidth=2,color = "red")
ax.plot(l2[:,0],l2[:,1],linewidth=2,color = "blue")
ax.tick_params(axis='both',labelsize=18)
ax.set_ylabel('SOI',fontsize = 18)
ax.set_xlabel('Recruitment lagged with 6 months',fontsize = 18);


# ## Cubic Splines

# In[8]:


# Tilpasning av 3. ordens polynom for hvert tidspunkt gir en veldig god fit til tidsrekka selv.
# Mest nyttig dersom man ønsker data med høyere oppløsning enn det man egentlig har,
# eller for å approximere verdiene til manglende datapunter.


# In[9]:


from scipy.interpolate import interp1d
int_function = interp1d(year, soi, kind='cubic')

year_higherres = np.linspace(year[0],year[5*12],1000)

# plott data
fig, ax = plt.subplots(figsize = [15,5])
ax.plot(year[0:5*12],soi[0:5*12],linewidth=2,color = "black");
ax.plot(year[0:5*12],soi[0:5*12],'o',color = "black");
ax.plot(year_higherres,int_function(year_higherres),linewidth=2,color = "red")
ax.set_xlabel('Year',fontsize = 18)
ax.set_title('Southern Oscillation Index',fontsize = 18)
ax.grid()
ax.set_xlim(min(year),year[5*12])
ax.tick_params(axis='both',labelsize=18)


# ## Smoothing cubic splines (tilpasser polynom over lengre segmenter av data)

# In[10]:


from scipy.interpolate import UnivariateSpline

spl = UnivariateSpline(year, soi)

# plott data
fig, ax = plt.subplots(figsize = [15,5])
ax.plot(year,soi,linewidth=2,color = "black");
ax.plot(year, spl(year), 'g', lw=2)
print(spl.get_knots())

spl = UnivariateSpline(year, soi)
spl.set_smoothing_factor(20)
ax.plot(year, spl(year), 'b', lw=2)
print(len(spl.get_knots()))

spl = UnivariateSpline(year, soi)
spl.set_smoothing_factor(40)
ax.plot(year, spl(year), 'r', lw=2)
print(len(spl.get_knots()))

ax.set_xlabel('Year',fontsize = 18)
ax.set_title('Southern Oscillation Index',fontsize = 18)
ax.grid()
ax.set_xlim(min(year),max(year))
ax.tick_params(axis='both',labelsize=18)

#print(spl.get_knots())
#print(len(spl.get_knots()))
#print(len(year))


# # Lineære filter og konvolusjoner

# In[11]:


get_ipython().run_line_magic('matplotlib', 'inline')

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import animation, rc
from IPython.display import HTML

# NB: ffmpeg må installeres for å kunne kjøre den neste koden.
# Det kan gjøres ved å skrive inn følgende på kommandolinja:
# conda install -c conda-forge ffmpeg


# In[12]:


# First set up the figure, the axis, and the plot element we want to animate
fig, ax = plt.subplots(nrows = 3,ncols = 1, sharex=True, figsize = [15,7]);

L = 25
normal = signal.gaussian(L, std=3) / np.sum(signal.gaussian(L, std=3))
midpoint = int(np.floor(L/2))

for axes in [ax[0], ax[1], ax[2]]:
    axes.set_ylim(-0.2, 1.2)
    axes.set_xlim(0, 300)
    #axes.grid()

ax[1].set_ylim(0, 0.15)   
    
x0 = np.arange(0, 300)
y0 = np.repeat([0., 1., 0.], 100)
line0, = ax[0].plot([], [], lw=2)
line1, = ax[1].plot([], [], lw=2)
line2, = ax[2].plot([], [], lw=2)

line = [line0, line1, line2]

# initialization function: plot the background of each frame
def init():
    line[0].set_data(x0, y0)
    line[1].set_data([], [])
    line[2].set_data([], [])
    return line

# animation function. This is called sequentially
convolution = signal.convolve(y0, normal, mode='same')

def animate(i):
    x1 = np.arange(-midpoint+i, midpoint+1+i)
    y1 = normal
    
    x2 = np.arange(0,i)
    y2 = convolution[:i]
    line[1].set_data(x1, y1)
    line[2].set_data(x2, y2)

    return line

# call the animator.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=np.arange(0, 300), interval=100, blit=True)


# In[13]:


rc('animation', html='html5')
anim


# In[15]:


# Set up formatting for the movie files
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)

#anim.save('anim1.mp4', writer=writer)


# ## Tilbake til Moving average eksempel:

# In[16]:


wn = np.random.normal(loc=5, scale=10, size=100)

# vanlig moving average 
n=25
lin_filt = np.ones(n)
filtered = signal.convolve(wn, lin_filt, mode='valid') / sum(lin_filt)

# plott data
fig, ax = plt.subplots(figsize = [12,4])
ax.plot(wn,linewidth=2,color = "black");
ax.plot(filtered,linewidth=2, color = "red")
# samme plott av moving average, men forskjøvet i tid slik at det blir sentrert:
ax.plot(np.arange(np.floor(n/2),len(wn)-np.floor(n/2)), filtered, linewidth=2 ,color = "green")
ax.grid()
ax.set_xlim(0,100)
ax.tick_params(axis='both',labelsize=18)


# In[17]:


wn = np.random.normal(loc=5, scale=10, size=100)

# vanlig moving average 
n=25
lin_filt = np.ones(n)
filtered = signal.convolve(wn, lin_filt, mode='same') / sum(lin_filt)

# plott data
fig, ax = plt.subplots(figsize = [12,4])
ax.plot(wn,linewidth=2,color = "black");
ax.plot(filtered,linewidth=2, color = "red")
ax.grid()
ax.set_xlim(0,100)
ax.tick_params(axis='both',labelsize=18)


# In[18]:


# First set up the figure, the axis, and the plot element we want to animate
fig, ax = plt.subplots(nrows = 3,ncols = 1, sharex=True, figsize = [15,7]);

L = 25
normal = signal.gaussian(L, std=3) / np.sum(signal.gaussian(L, std=3))
midpoint = int(np.floor(L/2))

for axes in [ax[0], ax[1], ax[2]]:
    axes.set_ylim(-2, 2)
    axes.set_xlim(0, 300)
    #axes.grid()

ax[1].set_ylim(0, 0.15)

x0 = np.arange(0, 300)
y0 = np.random.normal(loc=0, scale=1, size=300)
line0, = ax[0].plot([], [], lw=2)
line1, = ax[1].plot([], [], lw=2)
line2, = ax[2].plot([], [], lw=1)
line3, = ax[2].plot([], [], lw=2)

line = [line0, line1, line2, line3]

# initialization function: plot the background of each frame
def init():
    line[0].set_data(x0, y0)
    line[1].set_data([], [])
    line[2].set_data(x0, y0)
    line[3].set_data([], [])
    return line

# animation function. This is called sequentially
convolution = signal.convolve(y0, normal, mode='same')

def animate(i):
    x1 = np.arange(-midpoint+i, midpoint+1+i)
    y1 = normal
    
    x2 = np.arange(0,i)
    y2 = convolution[:i]
    line[1].set_data(x1, y1)
    line[3].set_data(x2, y2)

    return line

# call the animator.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=np.arange(0, 300), interval=100, blit=True)


# In[19]:


rc('animation', html='html5')
anim


# In[ ]:


#anim.save('anim2.mp4', writer=writer)


# ## Eksempel med kausal prosess og ikke-symmetrisk filter:

# In[20]:


L = 25
lin_filter = np.array([np.exp(-0.4*t) for t in range(0,L)]) / np.sum(np.array([np.exp(-0.4*t) for t in range(0,L)]))

plt.plot(lin_filter);


# In[21]:


# First set up the figure, the axis, and the plot element we want to animate
fig, ax = plt.subplots(nrows = 3,ncols = 1, sharex=True, figsize = [15,7]);

L = 25
lin_filter = np.array([np.exp(-0.4*t) for t in range(0,L)]) / np.sum(np.array([np.exp(-0.4*t) for t in range(0,L)]))
midpoint = int(np.floor(L/2))

for axes in [ax[0], ax[1], ax[2]]:
    axes.set_ylim(-2, 2)
    axes.set_xlim(0, 300)
    #axes.grid()

ax[1].set_ylim(0, np.max(lin_filter))

x0 = np.arange(0, 300)
#y0 = np.random.normal(loc=0, scale=1, size=300)
y0 = np.repeat([0., 1., 0.], 100)
line0, = ax[0].plot([], [], lw=2)
line1, = ax[1].plot([], [], lw=2)
line2, = ax[2].plot([], [], lw=1)
line3, = ax[2].plot([], [], lw=2)

line = [line0, line1, line2, line3]

# initialization function: plot the background of each frame
def init():
    line[0].set_data(x0, y0)
    line[1].set_data([], [])
    line[2].set_data(x0, y0)
    line[3].set_data([], [])
    return line

# animation function. This is called sequentially
convolution = signal.convolve(y0, lin_filter, mode='same')
convolution = np.pad(convolution,(midpoint,0),mode='constant')

def animate(i):
    x1 = np.arange(i, L+i)
    #x1 = np.arange(i, L+i)
    y1 = lin_filter[::-1]
    
    x2 = np.arange(0, L+i)
    y2 = convolution[:L+i]
    line[1].set_data(x1, y1)
    line[3].set_data(x2, y2)

    return line

# call the animator.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=np.arange(0, 300-L), interval=100, blit=True)


# In[22]:


rc('animation', html='html5')
anim


# In[ ]:


#anim.save('anim3.mp4', writer=writer)

