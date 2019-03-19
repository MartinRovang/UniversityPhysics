#%%
import numpy as np 
import matplotlib.pyplot as plt
import os
from PIL import Image
import cv2
from scipy.signal import convolve2d

# Load images
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
F1 = (F1-np.min(F1))/np.max(F1-np.min(F1))*255
F2 = (F2-np.min(F2))/np.max(F2-np.min(F2))*255
F3 = (F3-np.min(F3))/np.max(F3-np.min(F3))*255
F4 = (F4-np.min(F4))/np.max(F4-np.min(F4))*255
F5 = (F5-np.min(F5))/np.max(F5-np.min(F5))*255

F1 = F1.astype('uint8')
F2 = F2.astype('uint8')
F3 = F3.astype('uint8')
F4 = F4.astype('uint8')
F5 = F5.astype('uint8')


def gaussian_lp(image, sigma):
        """Gaussian low pass filter, sigma defines the radius around the centered frequency(cutoff)"""
        row, col = image.shape
        H = np.zeros((row, col))
        for y in range(row):
            for x in range(col):
                D = np.sqrt((y-int(row/2))**2 + (x-int(col/2))**2)
                H[y,x] = np.exp(-D**2/(2*sigma**2))
        X = np.fft.fftshift(np.fft.fft2(image))
        Y = np.fft.fftshift(X-H)
        y = np.fft.ifft2(Y)
        return np.abs(y)


def estimate_noise(image, sigma = 10):
    slice = image[0:100,:]
    slicearray = np.zeros(image.shape)
    rows, cols = image.shape
    H = np.zeros((rows, cols))
    for y in range(rows):
        for x in range(cols):
            D = np.sqrt((y-int(rows/2))**2 + (x-int(cols/2))**2)
            H[y,x] = np.exp(-D**2/(2*sigma**2))
    
    slicearray[0:100,:] = slice
    NY = np.fft.fftshift(np.fft.fft2(slicearray))
    X = np.fft.fftshift(np.fft.fft2(image))
    G = X - NY*H
    G = np.fft.fftshift(G)
    g = np.fft.ifft2(G)
    return np.abs(g)


estimated_noie = estimate_noise(F2)
plt.imshow(estimated_noie, cmap = 'gray')
plt.show()


# sigma = 10

# # Lowpass image F2
# image = gaussian_lp(F2, sigma)

# # Plot
# fig, ax = plt.subplots(1,2)
# ax[0].imshow(F2, cmap = 'gray', interpolation = 'none', vmin = 0, vmax = 255)
# ax[0].set_title('Original F2')
# ax[1].imshow(image, cmap = 'gray', interpolation = 'none', vmin = 0, vmax = 255)
# ax[1].set_title('Gaussian lowpass, $\sigma$ = %s'%sigma)
# plt.show()


#%%


