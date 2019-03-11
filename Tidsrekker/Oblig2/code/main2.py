#%%
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


def w_periodogram(x, dt):
    N = len(x)
    n = np.arange(0,N,1)
    # Hann window
    window = (1/2)*(1 - np.cos(2*np.pi*n/(N-1)))
    U = (1/N)*np.sum(window**2)
    df = 1/(N*dt)
    f_list = np.arange(0,1/(2*dt), df)
    S = []
    for f in f_list:
        e = np.exp(-1j*2*np.pi*f*n*dt)
        S.append((dt/(N*U))*np.abs(np.sum(window*x*e))**2)

    return f_list, S


def WOSA(x, M, overlap, dt = 1):
    x = np.append(x, 0)
    n = np.arange(0, M, 1)
    window = (1/2)*(1 - np.cos(2*np.pi*n/(M-1)))
    U = (1/M)*np.sum(window**2)
    n_windows = int(round(len(x)/M, 1)/2)
    spectrum = np.zeros(M)
    for i in range(0, n_windows):
        spectrum_temp = np.fft.fft(window*x[(i*M):(i+1)*M])
        spectrum += (dt/(M*U))*np.abs(spectrum_temp)**2
    spectrum /= n_windows
    freq = np.fft.fftfreq(M, dt)
    print('Number of windows: %s'%n_windows)
    return freq[0:int(M/2)], spectrum[0:int(M/2)]

t = np.arange(0,len(sunspots),1)
sunspots2 = 0.40*np.cos(2*np.pi*0.094*t) + np.random.uniform(0, 1, len(t))
M = 40
freq, spectrum = WOSA(sunspots, M, 1/2)
freq_padded, spectrum_padded = WOSA(sunspots2, M, 1/2)
freq_padded2, spectrum_padded2 = WOSA(sunspots, M, 1/2)
freq_w, S_w = w_periodogram(sunspots, 1)

fig, ax = plt.subplots(2,1)
ax[0].plot(time, sunspots, linewidth = '3', color = 'black')
ax[0].set_title('Sunspots plot', fontsize = '20')
ax[0].set_ylabel('Sunspots')
ax[0].set_xlabel('Time')
ax[1].plot(freq, 10*np.log10(spectrum_padded/spectrum_padded[0]), '-.', linewidth = '1', color = 'black')
ax[1].set_title('WOSA padded, M = %s'%M, fontsize = '20')
ax[1].set_xlabel('Frequency')
ax[1].set_ylabel('dB power')
# ax[0,1].plot(t, sunspots2, linewidth = '3', color = 'black')
# ax[0,1].set_title('Sunspots simulated', fontsize = '20')
# ax[0,1].set_ylabel('Sunspots simulated')
# ax[0,1].set_xlabel('Time')
# ax[1,1].plot(freq_padded2, spectrum_padded2/spectrum_padded2[0], '-.', linewidth = '1', color = 'black')
# ax[1,1].set_title('WOSA padded simulated, M = %s'%M_pad, fontsize = '20')
# ax[1,1].set_xlabel('Frequency')
# ax[1,1].set_ylabel('dB power')
plt.tight_layout()
plt.show() 


