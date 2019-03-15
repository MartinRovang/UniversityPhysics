
import numpy as np 
import matplotlib.pyplot as plt
import os
from PIL import Image
import cv2
from scipy.signal import convolve2d



# Loading images
filedir = os.path.dirname(__file__)
imagedir = 'images/'
filename5 = 'starrySky.png'
#filename5 = 'teststars.jpg'
file = os.path.join(filedir, imagedir, filename5)


file = plt.imread(file)
# Transform to 0-255
file = (file-np.min(file))/np.max(file-np.min(file))*255
file = file.astype('uint8')




def butterworth_hp(image, a, K):
        """Butterworth high pass filter, sigma defines the radius around the centered frequency
        and n defines the order.(how close to ideal you want)"""
        row, col = image.shape
        H = np.zeros((row, col))
        for v in range(row):
            for u in range(col):
                top = np.sin(np.pi*a*u/col)
                bot = a*np.sin(np.pi*u/col)
                if u == 0:
                    H[u,v] = 1
                else:
                    H[u,v] = top/bot

        X = np.fft.fft2(image)
        top = np.abs(H)**2
        bot = (H*np.abs(H)**2 + K)
        Y = (top/bot)*X
        y = np.fft.ifft2(Y)
        y = np.abs(y)
        y = (y-np.min(y))/np.max(y-np.min(y))*255
        y = y.astype('uint8')
        return y


file2 = butterworth_hp(file, 200, 2)


fig, ax = plt.subplots(1,2)
ax[0].imshow(file, cmap = 'gray', interpolation = 'none', vmin = 0, vmax = 255)
ax[1].imshow(file2, cmap = 'gray', interpolation = 'none')
plt.show()



