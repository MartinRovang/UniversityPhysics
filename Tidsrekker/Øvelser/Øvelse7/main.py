import numpy as np
import matplotlib.pyplot as plt


N = 51
gauss = np.random.normal(0,1,N)


true_spectral = 1
fft = np.fft.fft(gauss)
freq = np.fft.fftfreq(len(fft))

plt.plot(freq, )