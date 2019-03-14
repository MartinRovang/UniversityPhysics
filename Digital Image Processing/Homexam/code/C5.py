import numpy as np 
import matplotlib.pyplot as plt
import os
from PIL import Image
import cv2
from scipy.signal import convolve2d


filedir = os.path.dirname(__file__)
imagedir = 'images/'
filename1 = 'F1.png'
file1 = os.path.join(filedir, imagedir, filename1)

filename2 = 'F2.png'
file2 = os.path.join(filedir, imagedir, filename2)

filename3 = 'F3.png'
file3 = os.path.join(filedir, imagedir, filename3)

filename4 = 'F4.png'
file4 = os.path.join(filedir, imagedir, filename4)

filename5 = 'F5.png'
file5 = os.path.join(filedir, imagedir, filename5)

F1 = plt.imread(file1)
F2 = plt.imread(file2)
F3 = plt.imread(file3)
F4 = plt.imread(file4)
F5 = plt.imread(file5)

# Transform to 0-255
F3 *= 255
F4 *= 255
F5 *= 255
F3 = F3.astype('uint8')
F4 = F4.astype('uint8')
F5 = F5.astype('uint8')

# Fourier, shift absolute value and decibel 
Y2 = 10*np.log10(np.abs(np.fft.fftshift(np.fft.fft2(F4))))

# Get frequencies sampling 1
N2 , M2 = Y2.shape
Y2freqN = np.fft.fftshift(np.fft.fftfreq(N2, 1))
Y2freqM = np.fft.fftshift(np.fft.fftfreq(M2, 1))

# plot
fig, ax = plt.subplots(1,2)
ax[0].imshow(F4, cmap='gray', interpolation = 'none', vmin = 0, vmax = 255)
ax[0].set_title('F4')
ax[1].imshow(Y2, cmap=plt.cm.BuPu_r, extent=(Y2freqN.min(),Y2freqN.max(),Y2freqM.min(),Y2freqM.max()))
ax[1].set_title('Frequency spectrum in dB scale, T = 20')
plt.savefig('findfreqfreq.pdf', bbox_inches = 'tight',
    pad_inches = 0)
plt.show()

