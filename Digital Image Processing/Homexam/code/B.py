import numpy as np 
import matplotlib.pyplot as plt
import os
from PIL import Image
import cv2
from scipy.signal import convolve2d

# Load images
filedir = os.path.dirname(__file__)
imagedir = 'images/'
filename = 'Fig_part_B.tif'
file = os.path.join(filedir, imagedir, filename)

image = plt.imread(file)

def resize_image(image, newN, newM):
    """Resizing by taking only the second pixel (50% resizing)"""
    resize = np.zeros((newM, newN))
    row, col = resize.shape
    try:
        for j in range(col):
            for i in range(row):
                resize[i, j] = image[i*2, j*2]
    except:
        pass

    return resize



row, col = image.shape
imagerez = resize_image(image, int(col*0.5), int(row*0.5))

fig, ax = plt.subplots(1,2)
ax[0].imshow(imagerez, cmap = 'gray', interpolation="none")
ax[0].set_title('Resized 50%')
ax[1].imshow(image, cmap = 'gray', interpolation="none")
ax[1].set_title('Original image')
plt.tight_layout()
plt.savefig('resized.pdf', bbox_inches = 'tight',
    pad_inches = 0)
plt.show()

def smoothing(image, boxsize = 3):
        """
        Avarage smoothing of 2D array
        boxsize -> size of boxkernal filter
        returns filtered 2D array
        """
        boxkernal = np.ones((boxsize, boxsize))/(boxsize**2)
        result = convolve2d(image, boxkernal, mode = 'same')
        return result.astype('uint8')


# Use these to smooth before resizing.

smooth1 = smoothing(image, boxsize = 3)
smooth2 = smoothing(image, boxsize = 5)
smooth3 = smoothing(image, boxsize = 10)

smooth1 = resize_image(smooth1, int(col*0.5), int(row*0.5))
smooth2 = resize_image(smooth2, int(col*0.5), int(row*0.5))
smooth3 = resize_image(smooth3, int(col*0.5), int(row*0.5))

# smooth1 = resize_image(image, int(col*0.5), int(row*0.5))
# smooth2 = resize_image(image, int(col*0.5), int(row*0.5))
# smooth3 = resize_image(image, int(col*0.5), int(row*0.5))

# smooth1 = smoothing(imagerez1, boxsize = 3)
# smooth2 = smoothing(imagerez2, boxsize = 5)
# smooth3 = smoothing(imagerez3, boxsize = 10)

fig, ax = plt.subplots(1,3)
ax[0].imshow(smooth1, cmap = 'gray', interpolation="none", vmin = 0, vmax = 255)
ax[0].set_title('Smoothing, kernel 3x3')
ax[1].imshow(smooth2, cmap = 'gray', interpolation="none", vmin = 0, vmax = 255)
ax[1].set_title('Smoothing, kernel 5x5')
ax[2].imshow(smooth3, cmap = 'gray', interpolation="none", vmin = 0, vmax = 255)
ax[2].set_title('Smoothing, kernel 10x10')
plt.tight_layout()
plt.savefig('smoothing.pdf', bbox_inches = 'tight', pad_inches = 0)
plt.show()

def lapsharp(image, maskret = False):
        """
        img -> 2D array
        maskret = True -> returns result and mask
        maskret = False -> returns result
        """
        #padded_image = np.pad(img, (1, 1), mode = 'symmetric')
        # lap is linear therefore;
        # lap f(x,y) = f(x + 1, y) + f(x - 1, y) + f(x, y + 1) + f(x, y - 1) - 4f(x,y)...
        #--------------------
        c = -1 # Depends on kernel
        # make zero kernal
        lapmask = np.zeros((3, 3))
        
        # add values to kernel
        lapmask[0,0] = 1
        lapmask[0,1] = 1
        lapmask[0,2] = 1

        lapmask[1,0] = 1
        lapmask[1,1] = -8
        lapmask[1,2] = 1

        lapmask[2,0] = 1
        lapmask[2,1] = 1
        lapmask[2,2] = 1
        #--------------------
        mask = convolve2d(image, lapmask, mode = 'same')
        result = image + c*mask

        # Map values to 0-255
        g1 = image - np.min(image)
        g = g1/np.max(g1) *255
        g = g.astype('uint8')

        if maskret == True:
            return g, mask
        else:
            return g.astype('uint8')

def gaussian_hp(image, sigma):
        """Gaussian high pass filter sigma defines the radius around the centered frequency"""
        row, col = image.shape
        H = np.zeros((row, col))
        for y in range(row):
            for x in range(col):
                D = np.sqrt((y-int(row/2))**2 + (x-int(col/2))**2)
                H[y,x] = np.exp(-D**2/(2*sigma**2))
        H_hp = (1-H)
        X = np.fft.fftshift(np.fft.fft2(image))
        Y = np.fft.fftshift((1+H_hp)*X)
        y = np.fft.ifft2(Y)
        return np.abs(y)

sigma = 40

# If enabled blurring before resizing
# sharpedimage = lapsharp(smooth1)
# sharpedimage2 = gaussian_hp(smooth1, sigma) + smooth1  # Adding highpass mask to blurred image to sharp it.


sharpedimage = lapsharp(smooth1)
sharpedimage2 = gaussian_hp(smooth1, sigma)  # Adding highpass mask to blurred image to sharp it.

fig, ax = plt.subplots(1,2)
ax[0].imshow(sharpedimage, cmap = 'gray', vmin = 0, vmax = 255, interpolation="none")
ax[0].set_title('Sharpened, Laplace kernel')
ax[1].imshow(sharpedimage2, cmap = 'gray', vmin = 0, vmax = 255, interpolation="none")
ax[1].set_title('Sharpened, gaussian highpass $\sigma = %s$'%sigma)
plt.tight_layout()
plt.savefig('sharpened.pdf', bbox_inches = 'tight',
    pad_inches = 0)
plt.show()


