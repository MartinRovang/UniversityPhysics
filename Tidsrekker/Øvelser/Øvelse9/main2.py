#%%
import numpy as np
import matplotlib.pyplot as plt

sigma_w = 1
# genererer hvit støy, som i eksempel ovenfor
N = 100
timestep = 1
t = np.linspace(0, 10, N)
f0 = 0.2
A = 1
wn = A*np.sin(2*np.pi*f0*t) + np.random.normal(loc=0, scale=sigma_w, size=N)

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



#%%

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('ASETEK.OL.csv')
data = pd.DataFrame(data)

x = data['Adj Close'].values[1:]
x = np.array(x,float)

#%%
import numpy as np
import matplotlib.pyplot as plt
f = 2000
fs = 8000
N = 16000
n = np.arange(0,N,1)
x = np.cos(2*np.pi*f*n/fs)
X = np.fft.fft(x)
freq = np.fft.fftfreq(len(X), 1/fs)


plt.plot(freq, np.abs(X))
plt.show()

print(8000*2000/N)

