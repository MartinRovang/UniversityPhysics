import matplotlib.pyplot as plt 
from scipy.io.wavfile import read, write
import numpy as np



N = 60000
dt = 1/44100
total = N*dt
print('total time: %s seconds'%total)
t = np.arange(0, total, dt)
x = np.random.normal(0, 1, N)
y = np.cos(2*np.pi*200*t) + x

B = 100
t = np.arange(-total/2, total/2, dt)
h = 2*B*np.sinc(2*np.pi*B*t)

H = np.fft.fftshift(np.fft.fft(h))
Y = np.fft.fftshift(np.fft.fft(y))

plt.plot(np.abs(H))
plt.show()

y = np.fft.fftshift(np.fft.ifft(H*Y))
spectrum = np.abs(np.fft.fftshift(np.fft.fft(y)))**2
freq = np.fft.fftshift(np.fft.fftfreq(len(y), dt))



fig, ax = plt.subplots(2,1)
ax[0].plot(y)
ax[1].plot(freq, np.log10(spectrum))
plt.show()


y = y/np.max(y)
write('test.wav', 44100, y)
