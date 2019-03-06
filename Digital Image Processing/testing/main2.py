import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


image = plt.imread('test.jpg')[:,:,0]
row, col = image.shape
# one = np.pad(image, (row,col), 'constant')
# row, col = one.shape
X = np.fft.fftshift(np.fft.fft2(image))
image2 = np.pad(image, (1000,1000), 'constant')
X2 = np.fft.fftshift(np.fft.fft2(image2))

fig, ax = plt.subplots(2,1)

ax[0].imshow(np.log(np.abs(X)+1))
ax[1].imshow(np.log(np.abs(X2)+1))
plt.show()


#%%
import numpy as np
import matplotlib.pyplot as plt

w = 0.25
n = np.arange(-20,20,1)
h = np.sinc(n*w)

H = np.fft.fftshift(1 - np.fft.fft(h))
freq = np.fft.fftshift(np.fft.fftfreq(len(H)))

plt.plot(n, h)
plt.show()

plt.plot(freq, H)
plt.show()