import numpy as np 
import matplotlib.pyplot as plt
import os
from PIL import Image
import cv2
from scipy.signal import convolve2d



# Loading files
filedir = os.path.dirname(__file__)
imagedir = 'images/'
filename5 = 'F5.png'
file5 = os.path.join(filedir, imagedir, filename5)

# Image import as floating values convert to 255
F5 = plt.imread(file5)
F5 *= 255
F5 = F5.astype('uint8')

# Fourier transform
spectrum = np.fft.fftshift(np.fft.fft2(F5))
spectrum1 = 10*np.log10(np.abs(spectrum))

# get shape
N , M = spectrum1.shape
# Find right frequency, sampling rate 1
HfreqN = np.fft.fftshift(np.fft.fftfreq(N, 1))
HfreqM = np.fft.fftshift(np.fft.fftfreq(M, 1))


# Plot
fig, ax = plt.subplots(1,2)
ax[0].imshow(F5, cmap = 'gray')
ax[1].set_title('Spectrum F5')
ax[1].imshow(spectrum1, cmap = plt.cm.BuPu_r, aspect='auto', extent=(HfreqN.min(),HfreqN.max(),HfreqM.min(),HfreqM.max()))
ax[0].set_title('F5')
# ax[1].set_xlim([-1, 1])
# ax[1].set_ylim([-1, 1])
plt.savefig('superpositionfreq.pdf', bbox_inches = 'tight',
    pad_inches = 0)
plt.show()



