import numpy as np 
import matplotlib.pyplot as plt


data = np.genfromtxt('tidsrekke_oblig2_oppg1.txt')


def find_freqs(spectrum, freq, freqs = 5):
    """Find the frequency with highest power"""
    frequencies = []
    # Slice away double side
    spectrum = spectrum[int(len(spectrum)/2):len(spectrum)]
    freq = freq[int(len(freq)/2):len(freq)]
    # Find the most powerfull frequencies
    for i in range(freqs):
        idx = np.argmax(spectrum)
        frequencies.append(freq[idx])
        spectrum = np.delete(spectrum,idx)
    return frequencies





def periodogram(x, dt):
    """Regular periodogram"""
    #x = np.pad(x, (0,200), 'constant')
    N = len(x)
    spectrum = np.abs(np.fft.fftshift(np.fft.fft(x))**2)
    spectrum *= dt/ N
    freq = np.fft.fftshift(np.fft.fftfreq(N, dt))

    return freq, spectrum


def w_periodogram(x, dt):
    """Windowed periodogram"""
    #x = np.pad(x, (0,200), 'constant')
    N = len(x)
    n = np.arange(0,N,1)
    # Hann window
    window = (1/2)*(1 - np.cos(2*np.pi*n/(N-1)))
    U = (1/N)*np.sum(window**2)
    spectrum = np.abs(np.fft.fftshift(np.fft.fft(window*x)))**2
    spectrum *= (dt/(N*U))
    freq = np.fft.fftshift(np.fft.fftfreq(N, dt))
    return freq, spectrum

dt = 1
freq, spectrum = periodogram(data, dt)
freqw, wspectrum = w_periodogram(data, dt)

# Find the most powerfull frequencies in decending order
print(find_freqs(spectrum, freq))
print(find_freqs(wspectrum, freqw))


# Find index corresponding to f = 0 
idx = np.where(freq == 0)
widx = np.where(freqw == 0)

# Plot
fig, ax = plt.subplots(3,1)
ax[0].plot(data, color = 'black', linewidth = 1)
ax[0].set_title('Original time series')
ax[0].set_xlabel('x')
ax[0].set_ylabel('y')
ax[1].plot(freq, 10*np.log10(spectrum/spectrum[idx]),'--', color = 'black', linewidth = 1)
ax[1].set_title('Periodogram')
ax[1].set_xlabel('Frequency')
ax[1].set_ylabel('dB')
ax[2].plot(freqw, 10*np.log10(wspectrum/wspectrum[widx]),'--', color = 'black', linewidth = 1)
ax[2].set_title('Periodogram with Hann window')
ax[2].set_xlabel('Frequency')
ax[2].set_ylabel('dB')
ax[1].set_xticks([x for x in np.arange(-0.5,0.5,0.1)])
ax[2].set_xticks([x for x in np.arange(-0.5,0.5,0.1)])
ax[1].grid()
ax[2].grid()
plt.tight_layout()
plt.savefig('rapport/taskb.pdf', bbox_inches = 'tight',
    pad_inches = 0)
plt.show()
