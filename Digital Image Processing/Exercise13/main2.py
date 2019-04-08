import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
from scipy.signal import convolve2d
from mpl_toolkits.mplot3d import axes3d

image = plt.imread('Fig1016(a)(building_original).tif')




def marr_hild_part12(image, sigma):
    # distance larger then 3sigma(99.8%?) from the mean are small to be ignored
    # But we need smallest ODD so we +1

    # Normalize image
    image.setflags(write=1)
    image = image/255

    kernelsize = 6*sigma+1
    kernel = np.zeros((kernelsize, kernelsize))

    # laplacian of gaussian
    for y in range(kernelsize):
        for x in range(kernelsize):
            mid = int(kernelsize/2)
            exp = np.exp(-(((x-mid)**2 +(y-mid)**2)/(2*sigma**2)))
            kernel[y,x] = (((y-mid)**2 + (x-mid)**2 - 2*sigma**2)/(sigma**4))*exp
    # use the negative version (flips the mexican hat)
    kernel *= -1
    mask = convolve2d(image, kernel, 'same')

    # Kernel needs to sum to zero.
    return mask, kernel


Z, kernel = marr_hild_part12(image, 1)

plt.imshow(Z, cmap = 'gray')
plt.show()



plt.imshow(kernel, cmap = 'gray')
plt.colorbar()
plt.show()


#X, Y = np.meshgrid(np.arange(0,100,1), np.arange(0,100,1))

# Plot sexy 3d
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# #ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2)
# ax.plot_surface(X, Y, Z, rstride=2, cstride=2, cmap='jet')
# plt.show()