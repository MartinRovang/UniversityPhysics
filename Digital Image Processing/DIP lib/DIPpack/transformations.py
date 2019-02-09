
import numpy as np

def gamma_transform(image, gvalue, c = 1.0):
    """
    Image -> Image
    gvalue -> Gamma value
    c -> constant

    Return 0-1 float array
    
    """
    transformed = image.astype('float')
    transformed /= 255
    transformed = c*transformed**gvalue
    transformed *= 255
    transformed = transformed.astype('uint8')
    return transformed



def contrast_stretch(image, E, r0 = 0.5):
    """
    Image -> Image
    E = Contrast stretch factor
    r0 = constant

    Returns 0-255 int array
    """
    transformed = image.astype('float')
    transformed /= 255
    transformed =  (transformed/r0)**E/(1 + (transformed/r0)**E)
    transformed *= 255
    transformed = transformed.astype('uint8')
    return transformed