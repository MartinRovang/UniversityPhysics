#%%
import matplotlib.pyplot as plt
import numpy as np 

# Plot Hann window;

N = 32
n = np.linspace(0,N,N)
window = (1/2)*(1 - np.cos(2*np.pi*n/(N-1)))
plt.plot(n, window)
plt.show()


#%%
spectrum = np.fft.fftshift(np.fft.fft(window, n = 1000))
freq = np.fft.fftshift(np.fft.fftfreq(len(spectrum)))
plt.plot(freq, 10*np.log10(np.abs(spectrum)**2))
plt.show()


# window = np.pad(window, (500,500), 'constant')
n = np.arange(0,N,1)
dt = 1
df = 1/(N*dt)
f_list = np.arange(-1/(2*dt),1/(2*dt), df)
f0 = 1/(N-1)
spectrum = []
for f in f_list:
    spectrum.append(np.sum((1/2)*np.exp(-1j*2*np.pi*f*n)) - np.sum((1/4)*(np.exp(-1j*2*np.pi*(f+f0)*n) + np.exp(-1j*2*np.pi*(f0-f)*n))))

plt.plot(f_list, 10*np.log10(np.abs(spectrum)**2))
plt.show()

#%%


def periodogram(x, N):
    n = np.arange(0,N,1)
    dt = 1
    df = 1/(N*dt)
    f_list = np.arange(0,1/(2*dt), df)
    S = []
    for f in f_list:
        e = np.exp(-1j*2*np.pi*f*n*(len(x)/(N-1)))
        S.append((1/(N-1)*np.abs(np.sum(x*e))**2))
    return f_list, S


def w_periodogram(x, N):
    n = np.arange(0,N,1)
    window = (1/2)*(1 - np.cos(2*np.pi*n/(N-1)))
    U = (1/(N-1))*np.sum(window**2)
    dt = 1
    df = 1/(N*dt)
    f_list = np.arange(0,1/(2*dt), df)
    S = []
    for f in f_list:
        e = np.exp(-1j*2*np.pi*f*n*(len(x)/(N-1)))
        S.append((1/((N-1)*U)*np.abs(np.sum(window*x*e))**2))
    return f_list, S


N = 32
A = 2
w_noise = np.random.normal(0,0.5,N)
f0 = 0.1
dt = 1
t = np.arange(0,N,dt)
theta =  np.random.uniform(low=0, high=2*np.pi, size=1)
x = A*np.cos(2*np.pi*f0*t + theta[0]) + w_noise

plt.plot(t,x)
plt.show()

flist1, S = periodogram(x,N)
flist2, Sw = w_periodogram(x,N)

plt.stem(flist1, S)
plt.show()
plt.stem(flist2, Sw)
plt.show()


# The window is more conservative around the frequencies.


#%%


#%%
import matplotlib.pyplot as plt
import numpy as np 

# Plot Hamming window;

N = 32
n = np.linspace(0,N,N)
window = (0.54 - 0.46*np.cos(2*np.pi*n/(N-1)))
plt.plot(n, window)
plt.show()


#%%
spectrum = np.fft.fftshift(np.fft.fft(window, n = 1000))
freq = np.fft.fftshift(np.fft.fftfreq(len(spectrum)))
plt.plot(freq, 10*np.log10(np.abs(spectrum)**2))
plt.show()


# n = np.arange(0,N,1)
# dt = 1
# df = 1/(N*dt)
# f_list = np.arange(-1/(2*dt),1/(2*dt), df)
# f0 = 1/(N-1)
# spectrum = []
# for f in f_list:
#     spectrum.append(np.sum((1/2)*np.exp(-1j*2*np.pi*f*n)) - np.sum((1/4)*(np.exp(-1j*2*np.pi*(f+f0)*n) + np.exp(-1j*2*np.pi*(f0-f)*n))))

# plt.stem(f_list, np.abs(spectrum))
# plt.show()

#%%


def periodogram(x, N, dt):
    N = len(x)
    df = 1/(N*dt)
    f_list = np.arange(0,1/(2*dt), df)
    S = []
    n = np.arange(0,N,1)
    for f in f_list:
        e = np.exp(-1j*2*np.pi*f*n*(len(x)/(N-1)))
        S.append((1/(N-1)*np.abs(np.sum(x*e))**2))
    return f_list, S


def w_periodogram(x, N, dt):
    N = len(x)
    df = 1/(N*dt)
    f_list = np.arange(0,1/(2*dt), df)
    S = []
    n = np.arange(0,N,1)
    window = (1/2)*(1 - np.cos(2*np.pi*n/(N-1)))
    U = (1/(N-1))*np.sum(window**2)
    for f in f_list:
        e = np.exp(-1j*2*np.pi*f*n*(len(x)/(N-1)))
        S.append((1/((N-1)*U)*np.abs(np.sum(window*x*e))**2))
    return f_list, S
N = 128
f0 = 0.1
f1 = 0.2
dt = 1
t = np.arange(0,N,dt)
theta =  np.random.uniform(low=0, high=2*np.pi, size=1)
x = np.cos(2*np.pi*f0*t + theta[0]) + 0.001*np.cos(2*np.pi*f1*t + theta[0])
print('Highest frequency resolution is %f'%(1/(2*dt)))
flist1, S = periodogram(x,N,dt)
flist2, Sw = w_periodogram(x,N,dt)

plt.plot(flist1, 10*np.log10(S))
plt.show()
plt.plot(flist2, 10*np.log10(Sw))
plt.show()


#%%
N = 256
A = 0.3
f0 = 0.1
dt = 1
t = np.arange(0,N,dt)
theta =  np.random.uniform(low=0, high=2*np.pi, size=1)
w_noise = np.random.normal(0,0.5,N)
x = A*np.cos(2*np.pi*f0*t + theta[0]) + w_noise


M = 32
n = np.arange(0,M,1)
tapering_window = (1/2)*(1 - np.cos(2*np.pi*n/(M-1)))
# number of windows to avarage
n_windows = int(len(x)/M - 1)
# initialize spectrum with zeros
spectrum = np.zeros(M)
for i in range(n_windows):
    # tapered DFT of slice N length of signal
    X = np.fft.fft(tapering_window*x[(i*M):(i+1)*M])
    spectrum += np.abs(X)**2

spectrum /= n_windows
# shift to -pi to pi from 0 to 2pi
spectrum = 10*np.log10(np.fft.fftshift(spectrum))
freq = np.fft.fftshift(np.fft.fftfreq(len(spectrum)))
plt.plot(freq, X)
plt.show()

#%%
N = 256
A = 0.3
f0 = 0.1
dt = 1
t = np.arange(0,N,dt)
theta =  np.random.uniform(low=0, high=2*np.pi, size=1)
w_noise = np.random.normal(0,0.5,N)
x = A*np.cos(2*np.pi*f0*t + theta[0]) + w_noise


M = 64
n = np.arange(0,M,1)
tapering_window = (1/2)*(1 - np.cos(2*np.pi*n/(M-1)))
# number of windows to avarage
n_windows = int(len(x)/M - 1)
# initialize spectrum with zeros
spectrum = np.zeros(M)
for i in range(n_windows):
    # tapered DFT of slice N length of signal
    X = np.fft.fft(tapering_window*x[(i*M):(i+1)*M])
    spectrum += np.abs(X)**2

X /= n_windows
# shift to -pi to pi from 0 to 2pi
spectrum = 10*np.log10(np.fft.fftshift(spectrum))
freq = np.fft.fftshift(np.fft.fftfreq(len(spectrum)))
plt.plot(freq, X)
plt.show()