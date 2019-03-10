#%%
import matplotlib.pyplot as plt 
import numpy as np 


data = np.genfromtxt('tidsrekke_oblig2_oppg1.txt')


def periodogram(x, dt):
    N = len(x)
    n = np.arange(0,N,1)
    df = 1/(N*dt)
    f_list = np.arange(0,1/(2*dt), df)
    S = []
    for f in f_list:
        e = np.exp(-1j*2*np.pi*f*n*dt)
        S.append((dt/N)*np.abs(np.sum(x*e))**2)

    return f_list, S


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

# f1, f2 = 0.2, 0.4
# N = 100
# dt = 1
# n = np.arange(0,N,dt)
# data = np.cos(2*np.pi*f1*n) + np.cos(2*np.pi*f2*n)


dt = 1
f_list, S_list = periodogram(data, dt)
fw_list, Sw_list = w_periodogram(data, dt)



fig, ax = plt.subplots(3,1)
ax[0].plot(data, color = 'black', linewidth = 2)
ax[0].set_title('Original time series')
ax[0].set_xlabel('x')
ax[0].set_ylabel('y')
ax[1].plot(f_list, 10*np.log10(S_list/S_list[0]),'--', color = 'black', linewidth = 1)
ax[1].set_title('Periodogram')
ax[1].set_xlabel('Frequecy')
ax[1].set_ylabel('dB')
ax[2].plot(fw_list, 10*np.log10(Sw_list/Sw_list[0]),'--', color = 'black', linewidth = 1)
# ax[2].stem(fw_list, Sw_list)
ax[2].set_title('Periodogram with Hann window')
ax[2].set_xlabel('Frequecy')
ax[2].set_ylabel('dB')
plt.tight_layout()
plt.show()




#%%
import matplotlib.pyplot as plt 
import numpy as np 


data = np.genfromtxt('tidsrekke_oblig2_oppg1.txt')

# f1, f2 = 0.2, 0.4
# N = 100
# dt = 1
# n = np.arange(0,N,dt)
# data = np.cos(2*np.pi*f1*n) + np.cos(2*np.pi*f2*n)


def WOSA(x, M, overlap = 1/2, dt = 1):
    n = np.arange(0, M ,1)
    # Hann window
    tapering_window = (1/2)*(1 - np.cos(2*np.pi*n/(M-1)))
    # number of windows to avarage
    n_windows = 2*int(round(len(x)/M, 1))
    print('Number of windows: %d'%n_windows)
    # initialize spectrum with zeros
    spectrum = np.zeros(M)
    U = (1/M)*np.sum(tapering_window**2)
    for i in range(0, n_windows):
        # tapered DFT of slice N length of signal
        X = np.fft.fft(tapering_window*x[(int(overlap*i)*M):(int(overlap*i)+1)*M])
        spectrum += (dt/(M*U))*np.abs(X)**2

    return spectrum/n_windows

spectrum = WOSA(data, M = 40, overlap = 1/2)
dt = 1
# shift to -pi to pi from 0 to 2pi
spectrum = 10*np.log10(spectrum/spectrum[0])
freq = np.fft.fftfreq(len(spectrum), 1)
plt.plot(freq[0:20], spectrum[0:20], '--', color = 'black', linewidth = 1)
plt.title('WOSA')
plt.xlabel('Frequecy')
plt.ylabel('dB')
plt.show()
