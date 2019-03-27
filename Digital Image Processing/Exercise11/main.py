

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image



gauss_image = plt.imread('Fig0508(a)(circuit-board-pepper-prob-pt1).tif')
pepper_image = plt.imread('Fig0507(b)(ckt-board-gauss-var-400).tif')


def geometric_mean(image, kernelsize):
    rows, cols = image.shape
    result = np.zeros(image.shape)
    image = np.pad(image, (int(kernelsize//2), int(kernelsize//2)), 'symmetric')
    for y in range(rows):
        for x in range(cols):
            current_placement = image[y:y+kernelsize, x:x+kernelsize].flatten()
            result[y,x] = np.prod(current_placement)**(1/(kernelsize**2))
    return result



def harmonic_mean(image, kernelsize):
    result = np.zeros(image.shape)
    rows, cols = image.shape
    image = np.pad(image, (int(kernelsize//2), int(kernelsize//2)), 'symmetric')
    for y in range(rows):
        for x in range(cols):
            current_placement = image[y:y+kernelsize, x:x+kernelsize].flatten()
            sum_val = np.sum(current_placement)
            if sum_val > 0:
                result[y,x] = kernelsize**2/(1/np.sum(current_placement))
            else:
                result[y,x] = 255
    return result



def plot_image(image1, image2):
    fig, ax = plt.subplots(1,2)
    ax[0].imshow(image1, cmap='gray')
    ax[0].set_title('Orginal Image')
    ax[1].imshow(image2, cmap = 'gray')
    ax[1].set_title('Filtered image')
    plt.tight_layout()
    plt.show()



geomfiltered = geometric_mean(gauss_image, 3)
harmonyfiltered = harmonic_mean(gauss_image, 3)


def alpha_trimmed_mean(image, d, boxsize = 3):
        """
        Alpha trimmed mean filter.
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


image = alpha_trimmed_mean(gauss_image, d = 2, boxsize= 3)