#%%
import numpy as np 
import matplotlib.pyplot as plt
import os
from PIL import Image
import cv2
from scipy.signal import convolve2d

# Load images
filedir = os.path.dirname(__file__)
imagedir = 'images/'
filename1 = 'F1.png'
file1 = os.path.join(filedir, imagedir, filename1)

filename2 = 'F2.png'
file2 = os.path.join(filedir, imagedir, filename2)

filename3 = 'F3.png'
file3 = os.path.join(filedir, imagedir, filename3)

filename4 = 'F4.png'
file4 = os.path.join(filedir, imagedir, filename4)

filename5 = 'F5.png'
file5 = os.path.join(filedir, imagedir, filename5)

F1 = plt.imread(file1)
F2 = plt.imread(file2)
F3 = plt.imread(file3)
F4 = plt.imread(file4)
F5 = plt.imread(file5)

# Transform to 0-255
F1 = (F1-np.min(F1))/np.max(F1-np.min(F1))*255
F2 = (F2-np.min(F2))/np.max(F2-np.min(F2))*255
F3 = (F3-np.min(F3))/np.max(F3-np.min(F3))*255
F4 = (F4-np.min(F4))/np.max(F4-np.min(F4))*255
F5 = (F5-np.min(F5))/np.max(F5-np.min(F5))*255
F1 = F1.astype('uint8')
F2 = F2.astype('uint8')
F3 = F3.astype('uint8')
F4 = F4.astype('uint8')
F5 = F5.astype('uint8')


def adaptive(image, boxsize = 5):
        """
        Adptive filtering, found variance of noise by find variance of a slice in the top image.
        Uses local var and local mean to set pixel value.
        """
        # Pad image
        image_padded = np.pad(image, (boxsize, boxsize) , mode = 'symmetric')
        result = np.zeros(image.shape)
        rows, cols = image_padded.shape


        hist, bins = np.histogram(F2.flatten(),256)

        r = np.array([x for x in range(256)])

        rows,cols = image.shape
        prob = hist/(rows*cols)

        m = np.sum(r*prob)
        variance_noise = np.sum((r-m)**2*prob)


        #variance_noise = np.var(image[5,0:cols])
        #print(variance_noise)

        # Multiply by 2 because there is 2 time the new pad size in each dimension.
        for row in range((rows-boxsize*2)):
            for col in range((cols-boxsize*2)):

                local_var = np.var(image_padded[row:row + boxsize,col:col + boxsize])
                local_mean = np.mean(image_padded[row:row + boxsize,col:col + boxsize])
                kernel_placement = image_padded[row:row + boxsize,col:col + boxsize] 
                current_val = image_padded[row,col]
                if variance_noise > local_var:
                    result[row, col] = current_val - 1*(current_val - local_mean)
                else:
                    result[row, col] = current_val - (variance_noise/local_var)*(current_val - local_mean)
        
        return result.astype('uint8')

image = adaptive(F2, boxsize= 3)

fig, ax = plt.subplots(1,2)

ax[0].imshow(F2, cmap = 'gray', vmin = 0, vmax= 255)
ax[1].imshow(image, cmap = 'gray', vmin = 0, vmax= 255)
plt.show()