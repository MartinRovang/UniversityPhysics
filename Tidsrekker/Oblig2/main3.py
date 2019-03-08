import os
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

data = pd.read_csv('ASETEK.OL.csv')
data = pd.DataFrame(data)
x = data['Adj Close'].values[1:]

x = np.diff(x, 1)

def WOSA(x, M, overlap, dt = 1):
    x = np.append(x, 0)
    n = np.arange(0,M,1)
    window = (1/2)*(1 - np.cos(2*np.pi*n/(M-1)))
    U = (1/M)*np.sum(window**2)
    window_length = 2*int(round(len(x)/M, 1))
    print('Number of windows: %s'%window_length)
    spectrum = np.zeros(M)
    for i in range(0, window_length):
        spectrum_temp = np.fft.fft(window*x[(int(overlap*i)*M):(int(overlap*i)+1)*M])
        spectrum += (dt/(M*U))*np.abs(spectrum_temp)**2
    freq = np.fft.fftfreq(M, dt)
    return freq[0:int(M/2)], spectrum[0:int(M/2)]


freq, S = WOSA(x, 150, 1/2)

plt.plot(x)
plt.show()

plt.plot(freq, S)
plt.show()