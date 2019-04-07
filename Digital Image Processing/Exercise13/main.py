import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image


strawberry = plt.imread('Fig0631(a)(strawberries_coffee_full_color).tif')
#strawberry = plt.imread('Fig0628(b)(jupiter-Io-closeup).tif')


def segment(z, a, C, D0):
    rows, cols, lols = z.shape
    result = np.zeros(z.shape)
    #result = np.zeros((rows,cols))
    for i in range(rows):
        for j in range(cols):
            D = np.sqrt(((z[i,j]-a).T@np.linalg.inv(C)@(z[i,j]-a)))
            if D <= D0:
                result[i,j] = z[i,j]
                #result[i,j] = 1
            
    return result.astype('uint8')


# Subregion a = y1, b = y2, c = x1, d = x2
a, b, c, d = 288, 324, 128, 167

subregion = strawberry[a:b, c:d]

R_mean = np.mean(subregion[:,:,0])
G_mean = np.mean(subregion[:,:,1])
B_mean = np.mean(subregion[:,:,2])

a_mean = np.array([R_mean, G_mean, B_mean])

# C = np.array([[5,0,0],
#             [0,15,0],
#             [0,0,5]])
# Range
D0 = 20



R_flat = subregion[:,:,0].flatten()/255
G_flat = subregion[:,:,0].flatten()/255
B_flat = subregion[:,:,0].flatten()/255

X = np.vstack((R_flat,G_flat,B_flat))

C = np.cov(X)*255
C[0,1] = 0; C[0,2] = 0; C[1,0] = 0
C[1,2] = 0; C[2,0] = 0; C[2,1] = 0


result = segment(strawberry, a_mean, C, D0)

strawberry.setflags(write=1)
strawberry[a:a+2,c:d] = 0
strawberry[b:b+2,c:d] = 0
strawberry[a:b+2,c:c+2] = 0
strawberry[a:b+2,d:d+2] = 0



fig, ax = plt.subplots(1,2)
ax[0].imshow(strawberry)
ax[1].imshow(result)
ax[1].set_title('')
plt.show()