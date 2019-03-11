import os
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

filedir = os.path.dirname(__file__)
filename = 'SN_y_tot_V2.0.txt'

file = os.path.join(filedir, filename)

# load file
datatable = pd.read_csv(file,sep='\t',header=None,engine='python')
time = np.zeros(len(datatable))
sunspots = np.zeros(len(datatable))

for i in range(len(datatable)):
     time[i] = datatable.values[i,0][0:6]
     sunspots[i] = datatable.values[i,0][8:13]


def WOSA(x, M, dt = 1):
    n = np.arange(0, M, 1)
    window = (1/2)*(1 - np.cos(2*np.pi*n/(M-1)))
    U = (1/M)*np.sum(window**2)
    spectrum = np.zeros(M)
    # zero pad to avoid out of bound error
    x = np.pad(x, (0, int(M + M/2)), 'constant')
    n_windows = int(len(x)/(M-1))
    for i in range(n_windows):
        if i == 0:
            spectrum_temp = np.fft.fftshift(np.fft.fft(window*x[0:40]))
        else:
            spectrum_temp = np.fft.fftshift(np.fft.fft(window*x[(i*int(M/2)):(i+2)*int(M/2)]))
        spectrum += (dt/(M*U))*np.abs(spectrum_temp)**2        
    spectrum /= n_windows
    freq = np.fft.fftshift(np.fft.fftfreq(M, dt))
    print('Number of windows: %s'%n_windows)
    return freq, spectrum


# f1, f2 = 0.2, 0.4
# N = 100
# dt = 1
# n = np.arange(0,N,dt)
# data = np.cos(2*np.pi*f1*n) + np.cos(2*np.pi*f2*n)


M = 40
dt = 1
freq, spectrum = WOSA(sunspots, M)
idx = np.where(freq == 0)


fig, ax = plt.subplots(2,1)
ax[0].plot(sunspots, linewidth = '3', color = 'black')
ax[0].set_title('Sunspots plot', fontsize = '20')
ax[0].set_ylabel('Sunspots')
ax[0].set_xlabel('Year')
#ax[1].plot(freq, 10*np.log10(spectrum/spectrum[idx]), '-.', linewidth = '1', color = 'black')
ax[1].set_title('WOSA, M = %s'%M, fontsize = '20')
ax[1].set_xlabel('Frequency')
ax[1].set_ylabel('dB power')
ax[1].set_xlim([0,1/(2*dt)])
plt.tight_layout()
plt.show() 