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
        e = np.exp(-1j*2*np.pi*f*n*(len(x)/(N-1)))
        S.append((1/(N-1)*np.abs(np.sum(x*e))**2))
    # Get value of f = 0
    e = np.exp(-1j*2*np.pi*0*n*(len(x)/(N-1)))
    S0 = ((1/(N-1)*np.abs(np.sum(x*e))**2))

    return f_list, S, S0


def w_periodogram(x, dt):
    N = len(x)
    n = np.arange(0,N,1)
    # Hann window
    window = (1/2)*(1 - np.cos(2*np.pi*n/(N-1)))
    U = (1/(N-1))*np.sum(window**2)
    df = 1/(N*dt)
    f_list = np.arange(0,1/(2*dt), df)
    S = []
    for f in f_list:
        e = np.exp(-1j*2*np.pi*f*n*(len(x)/(N-1)))
        S.append((1/((N-1)*U)*np.abs(np.sum(window*x*e))**2))
    # Get value of f = 0
    e = np.exp(-1j*2*np.pi*0*n*(len(x)/(N-1)))
    S0 = ((1/((N-1)*U)*np.abs(np.sum(window*x*e))**2))

    return f_list, S, S0

# f1, f2 = 0.2, 0.4
# N = 100
# dt = 1
# n = np.arange(0,N,dt)
# data = np.cos(2*np.pi*f1*n) + np.cos(2*np.pi*f2*n)


dt = 1
f_list, S_list, S0 = periodogram(data, dt)
fw_list, Sw_list, S02 = w_periodogram(data, dt)



fig, ax = plt.subplots(3,1)
ax[0].plot(data)
ax[0].set_title('Original time series')
ax[1].stem(f_list, 10*np.log10(S_list/S0))
# ax[1].stem(f_list, S_list)
ax[1].set_title('Periodogram')
ax[2].stem(fw_list, 10*np.log10(Sw_list/S02))
# ax[2].stem(fw_list, Sw_list)
ax[2].set_title('Periodogram with Hann window')
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


def WOSA(x, M, overlap = 1/2):
    n = np.arange(0, M ,1)
    # Hann window
    tapering_window = (1/2)*(1 - np.cos(2*np.pi*n/(M-1)))
    # number of windows to avarage
    n_windows = int(len(x)/(M*overlap))-1
    print(n_windows)
    # initialize spectrum with zeros
    spectrum = np.zeros(M)
    for i in range(n_windows):
        # tapered DFT of slice N length of signal
        X = np.fft.fft(tapering_window*x[(int(overlap*i)*M):(int(overlap*i)+1)*M])
        spectrum += np.abs(X)**2
    spectrum /= n_windows
    return spectrum

spectrum = WOSA(data, M = 40, overlap = 1/2)

# shift to -pi to pi from 0 to 2pi
spectrum = 10*np.log10(np.fft.fftshift(spectrum))
freq = np.fft.fftshift(np.fft.fftfreq(len(spectrum)))
plt.stem(freq, spectrum)
plt.show()
