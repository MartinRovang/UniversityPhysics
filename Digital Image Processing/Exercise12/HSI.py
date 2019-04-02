import matplotlib.pyplot as plt
import numpy as np


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
    R = R/np.max(R)
    G = G/np.max(G)
    B = B/np.max(B)

    # Get degrees
    top = (1/2)*((R-G)+(R-B))
    bot = np.sqrt((R-G)**2 + (R-B)*(G-B)+0.0001)
    theta = np.arccos(top/bot)

    # Hue
    idx1 = np.where(B <= G)
    idx2 = np.where(B > G)
    H = np.zeros(R.shape)
    H[idx1] = theta[idx1]
    H[idx2] = 360 - theta[idx2]

    # Saturation
    S = 1 - (3/(R+G+B))*np.minimum(R,G,B)


    # Intensity
    I = (1/3)*(R+G+B)


    return H,S,I