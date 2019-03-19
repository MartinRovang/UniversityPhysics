
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

polar_image = polar_image.astype('uint8').T


def wiener_filter(image, a, K):
        rows, cols = image.shape
        H = np.zeros((rows, cols))
        for y in range(0, rows):
            for x in range(0, cols):
                D = np.sqrt((y-int(rows/2))**2 + (x-int(cols/2))**2)
                if x == 0:
                    H[y,x] = 1
                else:
                    H[y,x] = (np.sin(np.pi*x*a/cols)/(a*np.sin(np.pi*x/cols)))
                    #H[y,x] = np.abs((1/(np.pi*x*a))*np.sin(np.pi*x*a)*np.exp(-1j*np.pi*x*a))
        X = np.fft.fft2(image)
        top = np.abs(H)**2
        bot = H*(np.abs(H)**2+K)
        Y = (top/bot)*X
        for y in range(0, rows):
            for x in range(0, cols):
                D = np.sqrt((y-int(rows/2))**2 + (x-int(cols/2))**2)
                if D < 55:
                    pass
                else:
                    Y[y,x] = 0
        y = np.fft.ifft2(Y)
        return np.abs(y)

im = wiener_filter(polar_image, (1/8)*cols, 1)


fig, ax = plt.subplots(1,2)
ax[0].imshow(polar_image, cmap = 'gray')
ax[1].imshow(im, cmap = 'gray')
plt.show()


# from skimage import color, data, restoration
# rows, cols = image.shape
# H = np.zeros((rows, cols))
# a = (1/8)*cols
# for y in range(0, rows):
#     for x in range(0, cols):
#         #D = np.sqrt((y-int(rows/2))**2 + (x-int(cols/2))**2)
#         if x == 0:
#             H[y,x] = 1
#         else:
#             H[y,x] = (np.sin(np.pi*x*a/cols)/(a*np.sin(np.pi*x/cols)))
# deconvolved_img = restoration.wiener(image, H, 10)

# fig, ax = plt.subplots(1,2)
# ax[0].imshow(polar_image, cmap = 'gray')
# ax[1].imshow(deconvolved_img, cmap = 'gray')
# plt.show()