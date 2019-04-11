import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
from scipy.signal import convolve2d
from mpl_toolkits.mplot3d import axes3d


image = plt.imread('Fig1016(a)(building_original).tif')
image = plt.imread('blaklokke.jpg')[:,:,0]




def otsu_glob(image):
    image.setflags(write=1)
    N = len(image.flatten())
    hist, bins = np.histogram(image.flatten(), bins = 255, range = [0, 255])
    p = hist/N
    cum_mean = []
    mean_glob = 0
    var_glob = 0
    between_class_var = 0
    best_val_k = 0
    best_val_BCV = 0
    cum_mean_value = 0

    # Cumsum probability
    cum_P = np.cumsum(p)
    
    for k in range(len(p)):
        # cum_P.append(np.sum(p[:k]))
        cum_mean_value += k*p[k]
        cum_mean.append(cum_mean_value)

        # Global mean
        mean_glob += k*p[k]

    for k in range(len(p)):
        # between-class variance
        between_class_var = (mean_glob*cum_P[k] - cum_mean[k])**2/(cum_P[k]*(1 - cum_P[k]))

        # Global variance
        var_glob += (k - mean_glob)**2*p[k]

        # Find best k
        if between_class_var >= best_val_BCV:
            if between_class_var == best_val_BCV:
                print('Non unique at k = %s'%k)
            # best between-class variance
            best_val_BCV = between_class_var
            # best k value
            best_val_k = k

    print('k = %s'%best_val_k)


    # Seperability measure
    nu_sep_measure = best_val_BCV/var_glob
    # Seperated image
    g = np.copy(image)
    g[g <= best_val_k] = 0; g[g > best_val_k ] = 1

    print('Seperability measure: %s'%nu_sep_measure)

    plt.hist(image.flatten(), bins= 256, label = 'Image histogram')
    plt.axvline(best_val_k, color='k', linestyle='dashed', linewidth=1, label = 'best histogram segmentation')
    plt.legend(loc = 'best')
    plt.show()

    return g


plt.imshow(otsu_glob(image), cmap = 'inferno')
plt.show()