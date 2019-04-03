import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
from scipy.signal import convolve2d
Image2 = plt.imread('blaklokke.jpg')[:,:,0]

Image = np.zeros((7, 8))

Image[3,2] = 1
Image[3,3] = 1
Image[2,3] = 1
Image[4,3] = 1
Image[3,4] = 1
Image[2,4] = 1
Image[4,4] = 1
Image[3,5] = 1



def sobel(image):
    gx = np.array([
    [-1, -2, -1],
     [0, 0, 0], 
     [1, 2, 1]])
    
    gy = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]])

    gx_mask = np.abs(convolve2d(image, gx, 'same'))
    gy_mask = np.abs(convolve2d(image, gy, 'same'))

    result = gx_mask + gy_mask

    return result



resultimage = sobel(Image2)
fig, ax = plt.subplots(1,2)

clb = ax[0].imshow(Image2, cmap = 'inferno')
ax[0].set_title('Orignal')
plt.colorbar(clb, ax = ax[0])
clb1 = ax[1].imshow(resultimage, cmap = 'inferno')
ax[1].set_title('Sobel operated')
plt.colorbar(clb1, ax = ax[1])
plt.show()