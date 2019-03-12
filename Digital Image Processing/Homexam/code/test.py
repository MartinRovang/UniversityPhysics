import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

image = plt.imread('images\Fig_part_B.tif')
print(image.shape)
def watermark(x):
    """Watermarks the image by replacing the least significant bits of the image."""
    x = format(x, '#010b')
    toadd = '00'
    temp = x[:-2] + toadd
    result = int(temp, 2)
    return result

vecwatermark = np.vectorize(watermark)

print(np.unique(image))
print(np.unique(vecwatermark(image)))


fig, ax = plt.subplots(2,1)
ax[0].hist(image.flatten(), bins = 256, align = 'mid')
ax[0].set_title('Original')
ax[1].hist(vecwatermark(image).flatten(), bins = 256, align = 'mid')
ax[1].set_title('Two least significant bits to zero')
plt.tight_layout()
plt.show()


fig, ax = plt.subplots(2,1)
ax[0].imshow(image, cmap = 'gray')
ax[0].set_title('Original')
ax[1].imshow(vecwatermark(image), cmap = 'gray')
ax[1].set_title('Two least significant bits to zero')
plt.tight_layout()
plt.show()



