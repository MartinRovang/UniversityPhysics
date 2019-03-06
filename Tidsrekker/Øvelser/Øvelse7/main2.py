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

def periodogram(signal, f,dt):
    N = len(signal)
    n = np.arange(0,N,1)
    e = np.exp(-1j*2*np.pi*f*n*dt)
    S = (1/N)*np.abs(np.sum(signal*e))**2
    return S

def plot_per(N, dB = False):
    """dB gir mindre differanse mellom frekvensene"""
    real_spec = 1
    dt = 10/N
    t = np.linspace(0, 10, N)
    f0 = 10
    # gaussian_proc = np.random.normal(0,1,N)
    # gaussian_proc = np.random.normal(0,1,N) + 2*np.sin(2*np.pi*f0*t) # add signal
    data = pd.read_csv('ASETEK.OL.csv')
    data = pd.DataFrame(data)
    x = data['Adj Close'].values[1:]
    gaussian_proc = np.array(x,float)
    dt = len(gaussian_proc)/N
    
    S_list = []
    print('Lowest resolution you can see, %.3f'%(1/(N*dt)))
    print('Highest frequency to observe is, %.3f'%(1/(2*dt)))
    m = np.arange(0, N/2, 1) # fourier frequency n/(N*dt), n = 0,1,2,3,4... N/2
    f_list = m/(N*dt) # fourier frequency n/(N*dt), n = 0,1,2,3,4... N/2 Se kompendium s.32
    # f_list = np.arange(0, 100, 1)/N
    for f in f_list:
        S_list.append(periodogram(gaussian_proc, f, dt))
    fig, ax = plt.subplots(2,1)

    ax[0].plot(gaussian_proc)
    if dB == True:
        ax[1].plot(f_list, np.log10(S_list), color = 'black', linewidth = 2)
        ax[1].plot(f_list, np.log10(np.full(len(S_list), real_spec)), '-.')
        ax[1].set_title('Frequency')
    else:
        ax[1].plot(f_list, S_list, color = 'black', linewidth = 2)
        ax[1].plot(f_list, np.full(len(S_list), real_spec), '-.')
        ax[1].set_title('Frequency')
    #ax[1].set_ylim([0,10])
    plt.tight_layout()
    plt.show()
    
N = 50000
plot_per(N)

#%%
N = 10000
data = pd.read_csv('ASETEK.OL.csv')
data = pd.DataFrame(data)
x = data['Adj Close'].values[1:]
gaussian_proc = np.array(x,float)
dt = len(gaussian_proc)/N
print('Highest resolution: %.3f'%(1/(2*dt)))
spectrum = np.fft.fft(gaussian_proc, n =50000)
dt = len(gaussian_proc)/len(spectrum)
freq = np.fft.fftfreq(len(spectrum), dt)
s_shift, f_shift = np.fft.fftshift([freq, spectrum])

plt.plot(f_shift,np.log10( np.abs(s_shift)))
plt.show()


#%%
