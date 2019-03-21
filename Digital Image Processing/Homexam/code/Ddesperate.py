

import numpy as np
from numpy import linalg
import matplotlib.pyplot as plt
import os
from PIL import Image
import cv2
from scipy.signal import convolve2d
from skimage import color, data, restoration
img = color.rgb2gray(data.astronaut())
psf = np.ones((5, 5)) / 25
img = convolve2d(img, psf, 'same')
img += 0.1 * img.std() * np.random.standard_normal(img.shape)
deconvolved_img = restoration.wiener(img, psf, 0.5)


fig, ax = plt.subplots(1,2)

ax[0].imshow(img, cmap = 'gray')
ax[1].imshow(deconvolved_img, cmap = 'gray')
plt.show()