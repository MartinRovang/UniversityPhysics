import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image


strawberry = np.array(plt.imread('Fig0631(a)(strawberries_coffee_full_color).tif'))
#strawberry = np.array(plt.imread('Fig0628(b)(jupiter-Io-closeup).tif'))


def segment(z, a, C, D0):
    rows, cols, *k = z.shape
    result = np.zeros(z.shape)
    #result = np.zeros((rows,cols))
    for i in range(rows):
        for j in range(cols):
            # Mahomtis distance
            D = np.sqrt((z[i,j]-a).T@np.linalg.inv(C)@(z[i,j]-a))
            if D <= D0:
                result[i,j] = z[i,j]
                #result[i,j] = 1
            
    return result.astype('uint8')


# Subregion a = y1, b = y2, c = x1, d = x2
x1, x2, y1, y2 = 209, 297, 75, 186

subregion = strawberry[x1:x2, y1:y2]

R_mean = np.mean(subregion[:,:,0])
G_mean = np.mean(subregion[:,:,1])
B_mean = np.mean(subregion[:,:,2])

a_mean = np.array([R_mean, G_mean, B_mean])
D0 = 5



R_flat = subregion[:,:,0].flatten()
G_flat = subregion[:,:,1].flatten()
B_flat = subregion[:,:,2].flatten()

X = np.vstack((R_flat,G_flat,B_flat))
C = np.cov(X)
# C[0,1] = 0; C[0,2] = 0; C[1,0] = 0
# C[1,2] = 0; C[2,0] = 0; C[2,1] = 0

result = segment(strawberry, a_mean, C, D0)


strawberry[x1:x1+2,y1:y2] = 0
strawberry[x2:x2+2,y1:y2] = 0
strawberry[x1:x2+2,y1:y1+2] = 0
strawberry[x1:x2+2,y2:y2+2] = 0



fig, ax = plt.subplots(1,2)
ax[0].imshow(strawberry)
ax[1].imshow(result)
ax[1].set_title('')
plt.show()