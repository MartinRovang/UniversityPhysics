#%%


"""
TASK C1-3

"""


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

# Make histogram
fig, ax = plt.subplots(1,2)
ax[0].hist(F1.flatten(), bins = 256)
ax[0].set_title('Histogram F1')

ax[1].hist(F2.flatten(), bins = 256)
ax[1].set_title('Histogram F2')

plt.savefig('noisehist.pdf')
plt.tight_layout()
plt.show()



#%%

def dB(x):
    """dB scale of signal"""
    return 10*np.log10(x+1)


fig, ax = plt.subplots(1,3)

spectrum3 = np.fft.fftshift(np.fft.fft2(F3))
spectrum4 = np.fft.fftshift(np.fft.fft2(F4))
spectrum5 = np.fft.fftshift(np.fft.fft2(F5))
ax[0].imshow(np.abs(spectrum3), cmap = 'seismic')
ax[0].set_title('F3')
ax[0].set_xlim([260,340])
ax[0].set_ylim([260,340])
ax[1].imshow(np.abs(spectrum4), cmap = 'seismic')
ax[1].set_title('F4')
ax[1].set_xlim([260,340])
ax[1].set_ylim([260,340])
ax[2].imshow(np.abs(spectrum5), cmap = 'seismic')
ax[2].set_title('F5')
ax[2].set_xlim([260,340])
ax[2].set_ylim([260,340])
plt.tight_layout()
plt.savefig('fourierrep.pdf')
plt.show()



#%%

def medianfilter(image, boxsize = 3):
        """
        Uses median filter, convolution in spatial domain\n
        returns processed image.
        """
        image_padded = np.pad(image, (boxsize,boxsize) , mode = 'symmetric')
        result = np.zeros(image.shape)
        rows, cols = image.shape
        # Traverse the image and apply filter.
        for row in range(rows):
            for col in range(cols):
                result[row, col] = np.median(image_padded[row:row + boxsize,col:col + boxsize].flatten())
        return result

# Filter image
filteredsalt = medianfilter(F1)

# Plot
fig, ax = plt.subplots(1,2)
ax[0].imshow(F1, cmap = 'gray', vmin = 0, vmax = 255, interpolation="none")
ax[1].imshow(filteredsalt, cmap = 'gray', vmin = 0, vmax = 255, interpolation="none")
ax[0].set_title('Original')
ax[1].set_title('Salt/pepper image, median filtered.')
plt.tight_layout()
plt.savefig('Filtered_saltimage.pdf', bbox_inches = 'tight',
    pad_inches = 0)
plt.show()

#%%
def adaptive_filter(image, boxsize = 3):
        """
        Adptive filtering, found variance of noise by find variance of a slice in the top image.
        Uses local var and local mean to set pixel value.
        """
        # Pad image
        image_padded = np.pad(image, (boxsize, boxsize) , mode = 'symmetric')
        result = np.zeros(image.shape)
        rows, cols = image_padded.shape
        # Get histogram of strip in image
        hist, bins = np.histogram(F2[0:100,:].flatten(),256)
        # Intensities
        r = np.array([x for x in range(256)])
        # Get size
        rows, cols = image.shape
        # Get probabilites
        prob = hist/(rows*cols)
        # Get mean
        m = np.sum(r*prob)
        # Get variance estimate of noise
        variance_noise = np.sum((r-m)**2*prob)
        
        # Traverse the image and apply filter.
        for row in range(rows):
            for col in range(cols):
                local_var = np.var(image_padded[row:row + boxsize,col:col + boxsize])
                local_mean = np.mean(image_padded[row:row + boxsize,col:col + boxsize])
                kernel_placement = image_padded[row:row + boxsize,col:col + boxsize] 
                current_val = image_padded[row,col]
                if variance_noise > local_var:
                    result[row, col] = current_val - 1*(current_val - local_mean)
                
                else:
                    result[row, col] = current_val - (variance_noise/local_var)*(current_val - local_mean)
        
        return result.astype('uint8')

# Run filter on image F2
filteredimage = adaptive_filter(F2, boxsize= 3)

# Plot
fig, ax = plt.subplots(1,2)
ax[0].imshow(F2, cmap = 'gray', interpolation = 'none', vmin = 0, vmax = 255)
ax[1].imshow(filteredimage, cmap = 'gray', interpolation = 'none', vmin = 0, vmax = 255)
ax[0].set_title('Original')
ax[1].set_title('Adaptive filtered')
plt.tight_layout()
plt.savefig('gaussianfiltered.pdf', bbox_inches = 'tight',
    pad_inches = 0)
plt.show()



#%%



