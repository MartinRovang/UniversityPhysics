import matplotlib.pyplot as plt
import numpy as np


def normalize(x):
    g = x/255

    return g


def RGB_to_HSI(image):
    """Transform RGB to HSI"""
    
    # Seperate RGB
    R = image[:,:,0]
    G = image[:,:,1]
    B = image[:,:,2]

    # Normalize
    R.setflags(write=1)
    G.setflags(write=1)
    B.setflags(write=1)
    R = normalize(R)
    G = normalize(G)
    B = normalize(B)

    # Get degrees
    top = (1/2)*((R-G)+(R-B))
    bot = np.sqrt((R-G)**2 + (R-B)*(G-B)+0.000001)
    theta = np.arccos(top/bot)

    # Hue
    idx1 = np.where(B <= G)
    idx2 = np.where(B > G)
    H = np.zeros(R.shape)
    H[idx1] = theta[idx1]
    H[idx2] = (2*np.pi - theta[idx2])

    # Normalize Hue
    H = H/(2*np.pi)


    # Saturation
    min_RG = np.minimum(R,G)
    minimum_RGB = np.minimum(min_RG,B)
    S = 1 - (3/(R+G+B))*minimum_RGB


    # Intensity
    I = (1/3)*(R+G+B)


    return H, S, I