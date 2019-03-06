#%%
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


image = plt.imread('test.jpg')[:,:,0]
row, col = image.shape
# one = np.pad(image, (row,col), 'constant')
# row, col = one.shape
X = np.fft.fftshift(np.fft.fft2(image))

H = np.zeros((row, col))
sigma = 50
for y in range(row):
    for x in range(col):
        D = np.sqrt((y-int(row/2))**2 + (x-int(col/2))**2)
        H[y,x] = np.exp(-D**2/(2*sigma**2))

G = H # Lowpass
G2 = (1 - H) # Highpass
g = np.fft.fftshift(np.fft.fft2(G2))
plt.imshow(np.log(np.abs(g)+1), cmap = 'gray')
plt.show()
G = H*X # Lowpass
G2 = (1 - H)*X # Highpass
G3 = X+G2 # Sharpening edges
# G = G[0:int(row/2),0:int(col/2)]

plt.imshow(np.abs(H), cmap = 'gray')
plt.show()

g = np.abs(np.fft.ifft2(G))
g2 = np.abs(np.fft.ifft2(G2))
g3 = np.abs(np.fft.ifft2(G3))

fig, ax = plt.subplots(1,4)

ax[0].imshow(image, cmap = 'gray')
ax[1].imshow(g, cmap = 'gray')
ax[2].imshow(g2, cmap = 'gray')
ax[3].imshow(g3, cmap = 'gray')
plt.tight_layout()
plt.show()




#%%

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


H = np.zeros((1000, 1000))
row, col = H.shape
sigma = 10
for y in range(row):
    for x in range(col):
        D = np.sqrt((y-int(row/2))**2 + (x-int(col/2))**2)
        if D > sigma:
            H[y,x] = 1
        else:
            H[y,x] = 0


plt.imshow(H, cmap = 'gray')
plt.show()

h = np.fft.fftshift(np.fft.ifft2(H))

plt.imshow(np.log(np.abs(h)), cmap = 'gray')
plt.show()