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
    n = np.arange(0,M,1)
    window = (1/2)*(1 - np.cos(2*np.pi*n/(M-1)))
    U = (1/M)*np.sum(window**2)
    window_length = 2*int(round(len(x)/M, 1))
    spectrum = np.zeros(M)
    for i in range(0, window_length):
        spectrum_temp = np.fft.fft(window*x[(int(overlap*i)*M):(int(overlap*i)+1)*M])
        spectrum += (dt/(M*U))*np.abs(spectrum_temp)**2
    freq = np.fft.fftfreq(M, dt)
    print('Number of windows: %s'%window_length)
    return freq[0:int(M/2)], spectrum[0:int(M/2)]

t = np.arange(0,len(sunspots),1)
sunspots2 = 0.40*np.cos(2*np.pi*0.094*t) + np.random.uniform(0, 1, len(t))
sunspots2_padded = np.pad(sunspots2, (500,500), 'constant')

x_padded = np.pad(sunspots,(500, 500), 'constant')
M, M_pad = int(80*2), int(80*2)
freq, spectrum = WOSA(sunspots, M, 1/2)
freq_padded, spectrum_padded = WOSA(x_padded, M_pad, 1/2)
freq_padded2, spectrum_padded2 = WOSA(sunspots2, M_pad, 1/2)
freq_w, S_w = w_periodogram(sunspots, 1)

fig, ax = plt.subplots(2,2, figsize = (15,10))
ax[0,0].plot(time, sunspots, linewidth = '3', color = 'black')
ax[0,0].set_title('Sunspots plot', fontsize = '20')
ax[0,0].set_ylabel('Sunspots')
ax[0,0].set_xlabel('Time')
ax[1,0].plot(freq_padded, spectrum_padded/spectrum_padded[0], '-.', linewidth = '1', color = 'black')
ax[1,0].set_title('WOSA padded, M = %s'%M_pad, fontsize = '20')
ax[1,0].set_xlabel('Frequency')
ax[1,0].set_ylabel('dB power')
ax[0,1].plot(t, sunspots2, linewidth = '3', color = 'black')
ax[0,1].set_title('Sunspots simulated', fontsize = '20')
ax[0,1].set_ylabel('Sunspots simulated')
ax[0,1].set_xlabel('Time')
ax[1,1].plot(freq_padded2, spectrum_padded2/spectrum_padded2[0], '-.', linewidth = '1', color = 'black')
ax[1,1].set_title('WOSA padded simulated, M = %s'%M_pad, fontsize = '20')
ax[1,1].set_xlabel('Frequency')
ax[1,1].set_ylabel('dB power')
plt.tight_layout()
plt.show() 


