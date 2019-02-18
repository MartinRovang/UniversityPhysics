
import numpy as np


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



def histeq(img, L, prob = False):
    """
    img -> np array
    L -> max intensity level i.e 256
    prob = True returns probability array, default = False

    Return result, probability
    or 
    Return result
    """
    M, N = img.shape
    vals, index, n_vals = np.unique(img, return_counts = True, return_index = True)
    probability = np.array([(x/(M*N)) for x in n_vals])
    result = img.astype('float')

    for i in range(0, L):
        idx = np.where(img == i)
        result[idx] = (L-1)*np.sum(probability[0:i+1])

    result = result.astype('uint8')

    if prob == True:
        return result, probability
    else:
        return result