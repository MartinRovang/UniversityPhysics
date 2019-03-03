
import numpy as np
from scipy.signal import convolve2d

def transform_image_255(image):
    image *= 255
    image = image.astype('uint8')
    return image

def transform_image_01(image):
    image = np.array(image)
    transformed = image.astype('float')
    transformed /= 255
    return transformed


def gamma_transform(image, gamma, c = 1.0):
    """
    Image -> Image
    gamma -> Gamma value
    c -> constant

    Returns 0-255 int array
    """

    transformed = transform_image_01(image)
    transformed = c*transformed**gamma

    transformed = transform_image_255(transformed)
    return transformed



def contrast_stretch(image, E, r0 = 0.5):
    """
    Image -> Image
    E = Contrast stretch factor
    r0 = constant

    Returns 0-255 int array
    """
    transformed = transform_image_01(image)
    transformed = ((transformed / r0) **E)/(1 + (transformed / r0) **E)
    transformed = transform_image_255(transformed)


    return transformed



def histeq(img, L, prob = False, stairplot = False):
    """
    img -> np array
    L -> max intensity level i.e 256
    prob = True returns probability array, default = False
    stairplot = False -> plots staircase plot default = False

    Return result, probability
    or 
    Return result
    """
    M, N = img.shape
    hist, bins = np.histogram(img.flatten(),L,[0,L])
    probability = hist/(M*N)
    result = img.astype('float')
    stair = []

    for i in range(0, L):
        idx = np.where(img == i)
        result[idx] = (L-1)*np.sum(probability[0:i+1])
        stair.append((L-1)*np.sum(probability[0:i+1]))
    result = result.astype('uint8')

    if stairplot == True:
        return result, stair

    if prob == True:
        return result, probability
    else:
        return result



def smoothing(img, boxsize = 3):
    """
    Avarage smoothing of 2D array
    boxsize -> size of boxkernal filter
    returns filtered 2D array
    *(truncate)
    """


    boxkernal = np.ones((boxsize, boxsize))/(boxsize**2)
    #img = np.pad(img, (boxsize, boxsize), mode = 'constant')
    result = convolve2d(img, boxkernal, mode = 'same')

    return result





def lapsharp(img, maskret = False):
    """
    img -> 2D array
    maskret = True -> returns result and mask
    maskret = False -> returns result

    *(truncate)
    """
    lapmask = np.zeros((3, 3))
    #padded_image = np.pad(img, (1, 1), mode = 'symmetric')
    # lap is linear therefore;
    # lap f(x,y) = f(x + 1, y) + f(x - 1, y) + f(x, y + 1) + f(x, y - 1) - 4f(x,y)
    #--------------------
    c = -1 # Depends on kernel
    lapmask[0,0] = 0
    lapmask[0,1] = 1
    lapmask[0,2] = 0

    lapmask[1,0] = 1
    lapmask[1,1] = -4
    lapmask[1,2] = 1

    lapmask[2,0] = 0
    lapmask[2,1] = 1
    lapmask[2,2] = 0
    #--------------------
    
    mask = convolve2d(img, lapmask, mode = 'same')
    result = img + c*mask


    if maskret == True:
        return result, mask
    else:
        return result