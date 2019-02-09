

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


B = colormapping(A, values, colors)
print(B.shape)

plt.imshow(B)
plt.show()

# B = Interpolate(A, 200, 200, 'NEAREST')
# C = Interpolate(A, 200, 200, 'LINEAR')

# fig, ax = plt.subplots(1,2)
# ax[0].imshow(B)
# ax[1].imshow(C)
# plt.show()


# B = gamma_transform(A, 0.4)
# print(B)
# plt.imshow(A, cmap = 'gray', vmin = 0, vmax = 255)
# plt.show()
# plt.imshow(B, cmap = 'gray',vmin = 0, vmax = 255)
# plt.show()