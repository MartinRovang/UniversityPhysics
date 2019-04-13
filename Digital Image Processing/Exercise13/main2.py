
#%% 
import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
from scipy.signal import convolve2d
from mpl_toolkits.mplot3d import axes3d


image = plt.imread('Fig1016(a)(building_original).tif')




def marr_hild(image, sigma):
    # distance larger then 3sigma(99.8%?) from the mean are small to be ignored
    # But we need smallest ODD so we +1

    # Normalize image
    image.setflags(write=1)
    image = image/255
    size = int(2*(np.ceil(3*sigma))+1)

    x, y = np.meshgrid(np.linspace(-size/2, size/2, size), np.linspace(-size/2, size/2, size))
    # x = x.astype('int')
    # y = y.astype('int')
    kernel = np.abs((x**2 + y**2 -2*sigma**2)/(sigma**4)*np.exp(-(x**2 + y**2) / (2*sigma**2)))
    # lap = np.array([[1, 1, 1],
    #                [1, -8, 1],
    #                [1, 1, 1]])

    
    # kernel = convolve2d(G, lap, 'same')

    kernel -= np.mean(kernel)
    print(np.sum(kernel))
    print(kernel.shape)
    kern_size = kernel.shape[0]

    mask = convolve2d(image, kernel, 'same')

    print(np.unique(mask))


    # Zero crossings
    result = np.zeros(image.shape)
    rows, cols = image.shape

    # 4% of maximum value
    T = np.max(mask)*0.04

    # # Use 3x3 kernel check
    for row in range(1, rows-1):
        for col in range(1 ,cols-1):
            left = mask[row,col-1]
            right = mask[row, col+1]
            up = mask[row-1, col]
            down = mask[row+1, col]
            diagdown1 = mask[row-1, col-1]
            diagup1 = mask[row-1, col+1]
            diagdown2 = mask[row-1, col-1]
            diagup2 = mask[row+1, col+1]

            if ((np.sign(left) != np.sign(right)) and ( np.sign(up) != np.sign(down))) or ((np.sign(diagdown1) != np.sign(diagup1)) and (np.sign(diagdown2) != np.sign(diagup2))):
                if np.abs(left-right) > T or np.abs(up-down) > T or np.abs(diagdown1-diagup1) > T or np.abs(diagdown2-diagup2) > T:
                    result[row, col] = 1


    # Kernel needs to sum to zero.3
    return mask, kernel, result



sigma = 8
Z, kernel, result = marr_hild(image, sigma)

fig, ax = plt.subplots(1, 2)
ax[0].imshow(Z, cmap = 'gray')
ax[1].imshow(result, cmap = 'gray')
plt.show()
plt.imshow(kernel, cmap = 'inferno')
plt.title('N = %s'%(kernel.shape[0]))
plt.show()

# X, Y = np.meshgrid(np.arange(0,sigma*6+1,1), np.arange(0,sigma*6+1,1))

# # Plot sexy 3d
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# #ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2)
# ax.plot_surface(X, Y, kernel, rstride=2, cstride=2, cmap='jet')
# plt.show()


