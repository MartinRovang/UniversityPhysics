import matplotlib.pyplot as plt 
import numpy as np 


data = np.genfromtxt('tidsrekke_oblig2_oppg1.txt')

# f1, f2 = 0.2, 0.4
# N = 100
# dt = 1
# n = np.arange(0,N,dt)
# data = np.cos(2*np.pi*f1*n) + np.cos(2*np.pi*f2*n)


def WOSA(x, M, dt = 1):
    n = np.arange(0, M, 1)
    window = (1/2)*(1 - np.cos(2*np.pi*n/(M-1)))
    U = (1/M)*np.sum(window**2)
    spectrum = np.zeros(M)
    n_windows = 2*int(len(x)/(M-1))
    for i in range(n_windows):
        if i == 0:
            spectrum_temp = np.fft.fftshift(np.fft.fft(window*x[0:40]))
            plt.plot(x[0:40])
            t = np.arange(0, 40, 1)
            plt.plot(t, window)
        else:
            spectrum_temp = np.fft.fftshift(np.fft.fft(window*x[(i*int(M/2)):(i+2)*int(M/2)]))
            plt.plot(x[0:(i+2)*int(M/2)])
            t = np.arange((i*int(M/2)), (i+2)*int(M/2), 1)
            plt.plot(t, window)
        spectrum += (dt/(M*U))*np.abs(spectrum_temp)**2        
    spectrum /= n_windows
    plt.show()
    freq = np.fft.fftshift(np.fft.fftfreq(M, dt))
    print('Number of windows: %s'%n_windows)
    return freq, spectrum

M = 40
dt = 1
freq, spectrum = WOSA(data, M)
idx = np.where(freq == 0)


fig, ax = plt.subplots(2,1)
ax[0].plot(data, linewidth = '3', color = 'black')
ax[0].set_title('Time series', fontsize = '20')
ax[0].set_ylabel('Value')
ax[0].set_xlabel('Time')
ax[1].plot(freq, 10*np.log10(spectrum/spectrum[idx]), '-.', linewidth = '1', color = 'black')
ax[1].set_title('WOSA, M = %s'%M, fontsize = '20')
ax[1].set_xlabel('Frequency')
ax[1].set_ylabel('dB power')
#ax[1].set_xlim([0,1/(2*dt)])
plt.tight_layout()
plt.show() 