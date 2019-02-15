
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


def gamma_transform(image = None, gamma, c = 1.0):
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



def contrast_stretch(image = None, E, r0 = 0.5):
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



