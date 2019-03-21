

"""TASK C7-2"""



import numpy as np 
import matplotlib.pyplot as plt
import os
from PIL import Image
import cv2
from scipy.signal import convolve2d



# Load images
filedir = os.path.dirname(__file__)
imagedir = 'images/'
filename5 = 'F5.png'
file5 = os.path.join(filedir, imagedir, filename5)

filename3 = 'F3.png'
file3 = os.path.join(filedir, imagedir, filename3)

filename4 = 'F4.png'
file4 = os.path.join(filedir, imagedir, filename4)

filename5 = 'F5.png'
file5 = os.path.join(filedir, imagedir, filename5)


F3 = plt.imread(file3)
F4 = plt.imread(file4)
F5 = plt.imread(file5)


# Transform to 0-255
F3 = (F3-np.min(F3))/np.max(F3-np.min(F3))*255
F4 = (F4-np.min(F4))/np.max(F4-np.min(F4))*255
F5 = (F5-np.min(F5))/np.max(F5-np.min(F5))*255
F3 = F3.astype('uint8')
F4 = F4.astype('uint8')
F5 = F5.astype('uint8')

def butter_notch_filter(image, sigma, notches, n):
        """Butterworth notch reject, sigma defines the radius around the notch frequency
        and n defines the order.(how close to ideal you want)"""
        row, col = image.shape
        res = np.ones((row, col))
        for h in notches:
            H = np.zeros((row, col))
            for y in range(row):
                for x in range(col):
                    # Notch
                    Dp = np.sqrt((y-int(row/2)-h[1])**2 + (x-int(col/2)-h[0])**2)
                    Dn = np.sqrt((y-int(row/2)+h[1])**2 + (x-int(col/2)+h[0])**2)
                    if Dp > 0 and Dn > 0:
                        H[y,x] = (1/(1+ (sigma/Dp)**n))*(1/(1+ (sigma/Dn)**n))
                    else:
                        H[y,x] = 0
            # add product to new resulting image.
            res *= H
        H = res
        X = np.fft.fftshift(np.fft.fft2(image))
        Y = np.fft.fftshift(X*H)
        y = np.fft.ifft2(Y)
        return np.abs(y), H

def butterworth_hp_sharp(image, sigma, n, k):
        """Butterworth high pass filter, sigma defines the radius around the centered frequency
        and n defines the order.(how close to ideal you want)"""
        row, col = image.shape
        H = np.zeros((row, col))
        for y in range(row):
            for x in range(col):
                D = np.sqrt((y-int(row/2))**2 + (x-int(col/2))**2)
                if D > 0:
                    H[y,x] = 1/(1+ (sigma/D)**(2*n))
                else:
                    H[y,x] = 0
        X = np.fft.fftshift(np.fft.fft2(image))
        # sharp image
        Y = (1+k*H)*X
        Y = np.fft.fftshift(Y)
        y = np.fft.ifft2(Y)
        return np.abs(y)


mid = 300 # Centered frequency, since notch filter have origo in center we need this to subtract.
notches = np.array([[330-mid, 0]])


# Use filters
y, H = butter_notch_filter(F4, 1, notches, 3)
y = butterworth_hp_sharp(y, 8, 5, k = 1)

# Convert back to 255 after masking
y = (y-np.min(y))/np.max(y-np.min(y))*255
y = y.astype('uint8')

# Get size of filter
N , M = H.shape

# Find real frequencies
HfreqN = np.fft.fftshift(np.fft.fftfreq(N, 1))
HfreqM = np.fft.fftshift(np.fft.fftfreq(M, 1))

# Plot
fig, ax = plt.subplots(1,2)
ax[0].imshow(F4, cmap = 'gray')
ax[0].set_title('Original')
ax[1].imshow(y, cmap = 'gray')
ax[1].set_title('Filtered image')
plt.savefig('C7F4.pdf', bbox_inches = 'tight', pad_inches = 0)
plt.show()

# Decibel frequency spectrum of image F4
Y = 10*np.log10(np.abs(np.fft.fftshift(np.fft.fft2(F4))))

# Plot
fig, ax = plt.subplots(1,2)
ax[0].imshow(Y, cmap = plt.cm.BuPu_r, aspect='auto', extent=(HfreqN.min(),HfreqN.max(),HfreqM.min(),HfreqM.max()))
ax[0].set_title('Frequency spectrum of F4')
ax[1].imshow(H, cmap = 'gray', aspect='auto', extent=(HfreqN.min(),HfreqN.max(),HfreqM.min(),HfreqM.max()))
ax[1].set_title('Notch filter in frequency dom.')
ax[0].set_xlim([-0.08,0.08])
ax[0].set_ylim([-0.08,0.08])
ax[1].set_xlim([-0.08,0.08])
ax[1].set_ylim([-0.08,0.08])
plt.savefig('C7F4freq.pdf', bbox_inches = 'tight',
    pad_inches = 0)
plt.show()

