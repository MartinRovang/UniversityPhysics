#%%
import numpy as np
import matplotlib.pyplot as plt

sigma_w = 1
# genererer hvit støy, som i eksempel ovenfor
N = 100
timestep = 1
t = np.linspace(0, 10, N)
f0 = 20
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
