#%%
import matplotlib.pyplot as plt 
import numpy as np 


data = np.genfromtxt('tidsrekke_oblig2_oppg1.txt')


def periodogram(x, dt):
    N = len(x)
    spectrum = np.abs(np.fft.fftshift(np.fft.fft(x))**2)
    spectrum *= dt/ N
    freq = np.fft.fftshift(np.fft.fftfreq(N, dt))

    return freq, spectrum


def w_periodogram(x, dt):
    N = len(x)
    n = np.arange(0,N,1)
    # Hann window
    window = (1/2)*(1 - np.cos(2*np.pi*n/(N-1)))
    U = (1/N)*np.sum(window**2)
    spectrum = np.abs(np.fft.fftshift(np.fft.fft(window*x))**2)
    spectrum *= (dt/(N*U))
    freq = np.fft.fftshift(np.fft.fftfreq(N, dt))
    return freq, spectrum

# f1, f2 = 0.2, 0.4
# N = 100
# dt = 1
# n = np.arange(0,N,dt)
# data = np.cos(2*np.pi*f1*n) + np.cos(2*np.pi*f2*n)


dt = 1
freq, spectrum = periodogram(data, dt)
freqw, wspectrum = w_periodogram(data, dt)

idx = np.where(freq == 0)
widx = np.where(freqw == 0)

fig, ax = plt.subplots(3,1)
ax[0].plot(data)
ax[0].set_title('Original time series')
ax[1].plot(freq, 10*np.log10(spectrum/spectrum[idx]))
ax[1].set_xlim([0, 1/(2*dt)])
ax[1].set_title('Periodogram')
ax[2].plot(freqw, 10*np.log10(wspectrum/wspectrum[widx]))
ax[2].set_xlim([0, 1/(2*dt)])
ax[2].set_title('Periodogram with Hann window')
plt.tight_layout()
plt.show()