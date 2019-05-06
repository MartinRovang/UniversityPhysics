import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
from scipy.signal import convolve2d

image1 = plt.imread('lighthouse.jpg')
image2 = plt.imread('tint_target.jpg')
N = 3

def equalize(image, specfied_image, N):
    result_finished = image.copy()
    for j in range(N):
        imagenow = np.copy(image)[:,:,j]
        specfied_imagenow = np.copy(specfied_image)[:,:,j]

        hist, bins = np.histogram(imagenow.flatten(), bins = 256, density = True)
        spec_hist, bins_ = np.histogram(specfied_imagenow.flatten(), bins = 256, density = True)

        s = hist.cumsum()
        s = (255 * s / s[-1]).astype(np.uint8)

        G = spec_hist.cumsum()
        G = (255 * G / G[-1]).astype(np.uint8)


        result1 = np.interp(imagenow.flatten(), bins_[:-1], s)
        result2 = np.interp(result1, G , bins_[:-1])


        result_finished[:,:,j] = result2.reshape((imagenow.shape[0], imagenow.shape[1]))
        
        plt.plot(s, label = 's')
        plt.plot(G, label = 'G')
        plt.legend()
        plt.show()

    return result_finished



result = equalize(image1, image2, N)

colors = ['red','green','blue']
fig, ax = plt.subplots(3,1)
for i in range(N):
    ax[0].hist(image1[:,:,i].flatten(), bins = 256, range = [0, 256], color = colors[i])
    ax[1].hist(image2[:,:,i].flatten(), bins = 256, range = [0, 256], color = colors[i])
    ax[2].hist(result[:,:,i].flatten(), bins = 256, range = [0, 256], color = colors[i])
plt.tight_layout()
plt.show()

fig, ax = plt.subplots(1,3)
ax[0].imshow(image1)
ax[1].imshow(image2)
ax[2].imshow(result)
plt.tight_layout()
plt.show()




