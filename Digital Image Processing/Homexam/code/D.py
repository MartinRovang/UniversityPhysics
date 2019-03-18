
import numpy as np
from numpy import linalg
import matplotlib.pyplot as plt
import os
from PIL import Image
import cv2
from scipy.signal import convolve2d



# Loading images
filedir = os.path.dirname(__file__)
imagedir = 'images/'
filename5 = 'starrySky.png'
#filename5 = 'teststars.jpg'
file = os.path.join(filedir, imagedir, filename5)


image = plt.imread(file)
# Transform to 0-255
image = (image-np.min(image))/np.max(image-np.min(image))*255
image = image.astype('uint8')
rows, cols = image.shape
center = np.sqrt(((int(rows/2)**2)+((int(cols/2))**2)))
polar_image = cv2.linearPolar(image,(rows/2, cols/2), center, cv2.WARP_FILL_OUTLIERS)

polar_image = polar_image.astype('uint8')

fig, ax = plt.subplots(1,2)


ax[0].imshow(polar_image, cmap = 'gray')
ax[1].imshow(image, cmap = 'gray')
plt.show()



def wiener_filter(image, a):
        row, col = image.shape
        H = np.zeros((row, col))
        for y in range(row):
            for x in range(col):
                D = np.sqrt((y-int(rows/2))**2 + (x-int(cols/2))**2)
                if (a*np.sin(np.pi*x/cols)) > 0.0002:
                    if D > 0:
                        H[y,x] = (np.sin(np.pi*x*a/cols)/(a*np.sin(np.pi*x/cols)))
                    else:
                        H[y,x] = 1
                else:
                    H[y,x] = 0.0002
        X = np.fft.fftshift(np.fft.fft2(image))
        Y = X/H
        y = np.fft.ifft2(np.fft.fftshift(Y))
        return X


# def wiener_filter(image, sigma, n):
#         """Butterworth high pass filter, sigma defines the radius around the centered frequency
#         and n defines the order.(how close to ideal you want)"""
#         row, col = image.shape
#         H = np.zeros((row, col))
#         for y in range(row):
#             for x in range(col):
#                 D = np.sqrt((y-int(row/2))**2 + (x-int(col/2))**2)
#                 if D > 0:
#                     H[y,x] = 1/(1+ (D/sigma)**(2*n))
#                 else:
#                     H[y,x] = 0
#         X = np.fft.fftshift(np.fft.fft2(image))
#         # sharp image
#         Y = H*X
#         Y = np.fft.fftshift(Y)
#         y = np.fft.ifft2(Y)
#         return np.abs(y)

#im = wiener_filter(polar_image,5, 1)
# im = wiener_filter(polar_image, 20)

# plt.imshow(polar_image, cmap = 'gray')
# plt.show()


