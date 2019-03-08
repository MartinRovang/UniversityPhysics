#%%
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


image = plt.imread('Fig0237(a)(characters test pattern)_POST.tif')
#image = plt.imread('FigP0421(left)(padded_image).tif')
row, col = image.shape
# one = np.pad(image, (row,col), 'constant')
# row, col = one.shape
X = np.fft.fftshift(np.fft.fft2(image))

H = np.zeros((row, col))
sigma = 60
for y in range(row):
    for x in range(col):
        D = np.sqrt((y-int(row/2))**2 + (x-int(col/2))**2)
        H[y,x] = np.exp(-D**2/(2*sigma**2))

G = H # Lowpass
G2 = (1 - H) # Highpass
g = np.fft.fftshift(np.fft.fft2(G2))
G = H*X # Lowpass
G22 = (1 - H)*X # Highpass
G3 = X+G2 # Sharpening edges
# G = G[0:int(row/2),0:int(col/2)]


g = np.abs(np.fft.ifft2(G))
g2 = np.abs(np.fft.ifft2(G22))
g3 = np.abs(np.fft.ifft2(G3))

# fig, ax = plt.subplots(1,4)

# ax[0].imshow(image, cmap = 'gray')
# ax[1].imshow(g, cmap = 'gray')
# ax[2].imshow(g2, cmap = 'gray')
# ax[3].imshow(g3, cmap = 'gray')
# plt.tight_layout()
# plt.show()

fig, ax = plt.subplots(1,3, figsize = [10,10])

ax[0].imshow(image, cmap = 'gray')
ax[1].imshow(np.abs(G2), cmap = 'gray')
ax[2].imshow(g2, cmap = 'gray')
plt.tight_layout()
plt.show()
plt.figure(figsize = (10,10))
plt.imshow(g2, cmap = 'gray')
plt.show()

#%%


image = plt.imread('blurrymoon.tif')
row, col = image.shape
# one = np.pad(image, (row,col), 'constant')
# row, col = one.shape
X = np.fft.fft2(image)

H = np.zeros((row, col))
sigma = 20
for y in range(row):
    for x in range(col):
        D = np.sqrt((y-int(row/2))**2 + (x-int(col/2))**2)
        H[y,x] = np.exp(-D**2/(2*sigma**2))

k = 1
G = (1+k*(1-H))*X
g = np.fft.ifft2(G)

plt.figure(figsize = (10,10))
plt.imshow(np.abs(g), cmap = 'gray')
plt.show()


#%%
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

image = plt.imread('Fig0237(a)(characters test pattern)_POST.tif')
orow, ocol = image.shape
image = np.pad(image, (0,200), 'constant')
row, col = image.shape

X = np.fft.fftshift(np.fft.fft2(image))

H = np.zeros((row, col))
sigma = 60
for y in range(row):
    for x in range(col):
        D = np.sqrt((y-int(row/2))**2 + (x-int(col/2))**2)
        H[y,x] = np.exp(-D**2/(2*sigma**2))

G = H # Lowpass
G2 = (1 - H) # Highpass
g = np.fft.fftshift(np.fft.fft2(G2))
G = H*X # Lowpass
G22 = (1 - H)*X # Highpass
G3 = X+G2 # Sharpening edges
# G = G[0:int(row/2),0:int(col/2)]


g = np.abs(np.fft.ifft2(G))
g2 = np.abs(np.fft.ifft2(G22))
g3 = np.abs(np.fft.ifft2(G3))

# fig, ax = plt.subplots(1,4)

# ax[0].imshow(image, cmap = 'gray')
# ax[1].imshow(g, cmap = 'gray')
# ax[2].imshow(g2, cmap = 'gray')
# ax[3].imshow(g3, cmap = 'gray')
# plt.tight_layout()
# plt.show()

g2 = g2[0:orow, 0:ocol]

fig, ax = plt.subplots(1,3, figsize = [10,10])

ax[0].imshow(image, cmap = 'gray')
ax[1].imshow(np.abs(G2), cmap = 'gray')
ax[2].imshow(g2, cmap = 'gray')
plt.tight_layout()
plt.show()
plt.figure(figsize = (10,10))
plt.imshow(g2, cmap = 'gray')
plt.show()


