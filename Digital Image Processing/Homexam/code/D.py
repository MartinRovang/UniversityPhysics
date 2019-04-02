
import numpy as np
from numpy import linalg
import matplotlib.pyplot as plt
import os
from PIL import Image
import cv2
from scipy.signal import convolve2d



# Loading images
filedir = os.path.dirname(__file__)
imagedir = 'images/'
filename5 = 'starrySky.png'
file = os.path.join(filedir, imagedir, filename5)

# Transpose
image = plt.imread(file)
# Transform to 0-255
image = (image-np.min(image))/np.max(image-np.min(image))*255
image = image.astype('uint8')
rows, cols = image.shape
radius = np.sqrt((rows/2-25)**2 +(cols/2-25)**2)
polar_image = cv2.linearPolar(image, (int(rows/2), int(cols/2)), radius, (cv2.WARP_FILL_OUTLIERS+cv2.INTER_LINEAR))

# Flip image with transpose
polar_image = polar_image.astype('uint8').T


def wiener_filter(image, a, K):
    """Wiener filter, a = displacement, K = Inverse signal to noise ratio. """
    rows, cols = image.shape
    H = np.zeros((rows, cols))
    for v in range(int(-rows/2), int(rows/2)):
        for u in range(int(-cols/2), int(cols/2)):
            if u == 0:
                H[v+int(rows/2),u+int(cols/2)] = 1
            else:
                H[v+int(rows/2),u+int(cols/2)] = (1/a)*(np.sin(np.pi*u*a/cols)/(np.sin(np.pi*u/cols)))

    # H.H^*
    H_abs = (H*np.conj(H))
    X = np.fft.fftshift(np.fft.fft2(image))
    top = H_abs
    bot = H*(H_abs + K)
    G = (top/bot)*X
    y = np.fft.ifft2(G)

    # Return image
    return np.abs(y)


# Apply filter and then taking it to the second power to remove some noise.
im = wiener_filter(polar_image, a = (1/8)*cols, K =0.01)**2

# Return image to cartesian coordinates.
im2 = cv2.linearPolar(im.T, (int(rows/2), int(cols/2)), radius, (cv2.WARP_INVERSE_MAP + cv2.INTER_LINEAR))


# Plot
fig, ax = plt.subplots(1,1)
ax.imshow(image, cmap = 'gray')
ax.set_title('Original')
plt.tight_layout()
plt.savefig('carttopol_trans_back1.pdf', bbox_inches = 'tight',
    pad_inches = 0)
plt.show()

fig, ax = plt.subplots(1,1)
ax.imshow(im, cmap = 'gray')
ax.set_title('Wiener filtered')
plt.tight_layout()
plt.savefig('carttopol_trans_back2.pdf', bbox_inches = 'tight',
    pad_inches = 0)
plt.show()


fig, ax = plt.subplots(1,1)
ax.imshow(im2, cmap = 'gray')
ax.set_title('Transformed back to cartesian.')
plt.tight_layout()
plt.savefig('carttopol_trans_back_original.pdf', bbox_inches = 'tight',
    pad_inches = 0)
plt.show()
