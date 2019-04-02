import matplotlib.pyplot as plt   
import numpy as np

grayscale_trans = np.array([0.2126, 0.7152, 0.0722])
image = plt.imread('c_276004-l_1-k_onkolytiska630.jpg')@grayscale_trans
image = image.astype('uint8')

R = np.zeros(image.shape)
G = np.zeros(image.shape)
B = np.zeros(image.shape)

row, col = image.shape
image_sliced = np.zeros((row, col, 3))


# Slice intensities
idx = np.where(image < 50)
values = image[idx]
R[idx] = values

idx = np.where((image >= 50) & (image < 100))
values = image[idx]
G[idx] = values
B[idx] = values

idx = np.where((image >= 100))
values = image[idx]
R[idx] = values
B[idx] = values


# Enter colors matricies
image_sliced[:,:,0] = R
image_sliced[:,:,1] = G
image_sliced[:,:,2] = B



# Plot
fig, ax = plt.subplots(1, 3)
ax[0].imshow(image, cmap = 'gray')
ax[1].imshow(image, cmap = 'inferno')
ax[2].imshow(image_sliced)
plt.show()