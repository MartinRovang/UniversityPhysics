
#%%
from DIPpack import colormapping
from DIPpack.interpol import Interpolate
from DIPpack.imginfo import getinfo
from DIPpack.transformations import gamma_transform, contrast_stretch
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

A = np.asarray(Image.open('test.tif'))

# print(np.unique(A))

values = [13,28,73,77,56,60,67]
colors = {'red': [255,5,1,81,12,43,8], 'green': [0,5,1,81,12,43,8], 'blue': [0,5,1,81,12,43,8]}


# B = colormapping(A, values, colors)
# print(B.shape)


# B = Interpolate(A, 7, 7, 'NEAREST')
# # C = Interpolate(A, 200, 200, 'LINEAR')
# plt.imshow(B)
# plt.show()


# fig, ax = plt.subplots(1,2)
# ax[0].imshow(B)
# ax[1].imshow(C)
# plt.show()


B = gamma_transform(A, 1)
plt.imshow(A, cmap = 'gray', vmin = 0, vmax = 255)
plt.show()
plt.imshow(B, cmap = 'gray',vmin = 0, vmax = 255)
plt.show()



# B = contrast_stretch(A, 8)
# plt.imshow(A, cmap = 'gray', vmin = 0, vmax = 255)
# plt.show()
# plt.imshow(B, cmap = 'gray',vmin = 0, vmax = 255)
# plt.show()

#%%

# A = np.zeros((5,5))
# A[3,3] = 1
# filterr = np.zeros((3,3))

# k = 1
# for i in range(0, 3):
#     for j in range(0, 3):
#         filterr[i,j] = k
#         k += 1

# print(filterr)



# fig, ax = plt.subplots()
# plt.imshow(A)
# #plt.imshow(C)
# plt.show()

#%%
