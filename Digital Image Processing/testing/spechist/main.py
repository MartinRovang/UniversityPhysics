import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
from scipy.signal import convolve2d


image1 = plt.imread('gray.jpeg')
image2 = plt.imread('lighthouse.jpg')[:,:,0]


def equalize(image, specfied_image):
    hist, bins = np.histogram(image.flatten(), bins = 256, range = [0, 256], density = True)
    P = np.cumsum(hist)
    spec_hist, bins_ = np.histogram(specfied_image.flatten(), bins = 256, range = [0, 256], density = True)
    spec_P = np.cumsum(spec_hist)

    s = np.ceil(255*P)
    G = np.ceil(255*spec_P)
    G_mapped = []
    s, G = s.astype('uint8'), G.astype('uint8')

    for i in range(0, 256):
        idx = np.abs(G - s[i]).argmin()
        G_mapped.append(G[idx])

    result = np.zeros(image.shape)
    for i in range(0, 256):
        idx = np.where(image == i)
        result[idx] = G_mapped[i]
        print('%s --> %s'%(s[i], G_mapped[i]))
    
    plt.plot(s, label = 's')
    plt.plot(G, label = 'G')
    plt.legend()
    plt.show()

    return result



result = equalize(image1, image2)



fig, ax = plt.subplots(3,1)
ax[0].hist(image1.flatten(), bins = 256, range = [0, 256], color = 'black')
ax[1].hist(image2.flatten(), bins = 256, range = [0, 256], color = 'black')
ax[2].hist(result.flatten(), bins = 256, range = [0, 256], color = 'black')
plt.tight_layout()
plt.show()

fig, ax = plt.subplots(1,3)
ax[0].imshow(image1, cmap = 'gray')
ax[1].imshow(image2, cmap = 'gray')
ax[2].imshow(result, cmap = 'gray')
plt.tight_layout()
plt.show()