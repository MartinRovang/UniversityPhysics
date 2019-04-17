import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
from scipy.signal import convolve2d


image = plt.imread('Fig1016(a)(building_original).tif')



def gradient(image):
    gx = np.array([[-1, -2, -1],
                    [0, 0, 0],
                    [1, 2, 1]
                    ])

    gy = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]
                    ])
    
    Gx = convolve2d(image, gx, 'same', boundary = 'symm')
    Gy = convolve2d(image, gy, 'same', boundary = 'symm')

    M = np.sqrt(Gx**2 + Gy**2)
    alpha = np.degrees(np.arctan2(Gy, Gx))

    return M, alpha




def canny(image, sigma, TH, TL):

    size = int(2*(np.ceil(3*sigma))+1)
    print(size)
    rows, cols = image.shape
    TH = int(TH*255)
    TL = int(TL*255)

    x, y = np.meshgrid(np.linspace(-size/2, size/2, size), np.linspace(-size/2, size/2, size))
    G = np.exp(-(x**2 + y**2) / (2*sigma**2))

    # Smoothed image
    fs = convolve2d(image, G, 'same', boundary ='symm')

    M, alpha = gradient(image)
    gN = np.zeros(image.shape)
    gNH = np.zeros(image.shape)
    gNL = np.zeros(image.shape)

    for i in range(1, rows-1):
        for j in range(1, cols-1):
            alpha_val = alpha[i,j]
            K = M[i,j]
            diag1 = None; diag2 = None
            horizontal = None; vertical = None

            if alpha_val >= -22.5 and alpha_val <= 22.5 or (alpha_val >= -157.5 and alpha_val <= 157.5):
                horizontal = True
            
            if alpha_val >= -67.5 and alpha_val <= -22.5 or (alpha_val >= 112.5 and alpha_val <= 157.5):
                diag1 = True

            if alpha_val >= -157.5 and alpha_val <= -112.5 or (alpha_val >= 22.5 and alpha_val <= 67.5):
                diag2 = True

            if alpha_val >= 67.5 and alpha_val <= 112.5 or (alpha_val >= -112.5 and alpha_val <= -67.5):
                vertical = True
            
            if horizontal:
                d1 = M[i, j - 1]
                d2 = M[i, j + 1]
                if K >= d1 or K >= d2:
                    gN[i,j] = K

            if vertical:
                d1 = M[i - 1, j]
                d2 = M[i + 1, j]
                if K >= d1 or K >= d2:
                    gN[i,j] = K
            
            if diag1:
                d1 = M[i - 1, j - 1]
                d2 = M[i + 1, j + 1]
                if K >= d1 or K >= d2:
                    gN[i,j] = K

            if diag2:
                d1 = M[i + 1, j - 1]
                d2 = M[i - 1, j + 1]
                if K >= d1 or K >= d2:
                    gN[i,j] = K

    gNH_idx = np.where(gN >= TH)
    gNL_idx = np.where(gN >= TL)
    gNH[gNH_idx] = np.copy(gN[gNH_idx])
    gNL[gNL_idx] = np.copy(gN[gNL_idx])
    gNL -= gNH


    return gNL, gNH





M, gN = canny(image, sigma = 4, TH = 0.10, TL = 0.04)
fig, ax = plt.subplots(1, 2)

ax[0].imshow(M, cmap = 'gray')
ax[1].imshow(gN, cmap = 'gray')
plt.show()

