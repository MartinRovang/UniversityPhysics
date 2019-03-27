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
F2 = (F2-np.min(F2))/np.max(F2-np.min(F2))*255
F2 = F2.astype('uint8')

def alpha_trimmed_mean(image, d, boxsize = 3):
        """
        Adptive filtering, found variance of noise by find variance of a slice in the top image.
        Uses local var and local mean to set pixel value.
        """
        # Pad image
        image_padded = np.pad(image, (boxsize, boxsize) , mode = 'symmetric')
        result = np.zeros(image.shape)
        rows, cols = image_padded.shape

        # Find bins
        hist, bins = np.histogram(F2.flatten(), 256)
        
        # Intensities
        r = np.array([x for x in range(256)])
        # Get size
        rows,cols = image.shape

        # Multiply by 2 because there is 2 time the new pad size in each dimension.
        for row in range((rows)):
            for col in range((cols)):
                sorted_vals = sorted(image_padded[row:row + boxsize,col:col + boxsize].flatten(), reverse = True)
                sorted_len = len(sorted_vals)
                sorted_vals_cut = sorted_vals[int(d/2): int(sorted_len-d/2)]
                result[row, col] = np.sum(sorted_vals_cut)//(sorted_len - d)
        return result.astype('uint8')

# Run filter on image F2
image = alpha_trimmed_mean(F2, d = 2, boxsize= 3)

# Plot
fig, ax = plt.subplots(1,2)
ax[0].imshow(F2, cmap = 'gray', interpolation = 'none', vmin = 0, vmax= 255)
ax[0].set_title('Original')
ax[1].imshow(image, cmap = 'gray', interpolation = 'none', vmin = 0, vmax= 255)
ax[1].set_title('Alpha trimmed filtered')
plt.tight_layout()
plt.savefig('alphatrimmed.pdf', bbox_inches = 'tight',
    pad_inches = 0)
plt.show()