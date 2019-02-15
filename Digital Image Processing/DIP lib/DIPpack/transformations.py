
import numpy as np

def gamma_transform(image, gvalue, c = 1.0):
    """
    Image -> Image
    gvalue -> Gamma value
    c -> constant

    Returns 0-255 int array
    
    """
    # Transform to float 0-1 to comform to the gamma transform 1^(0.4) = 1 
    transformed = image.astype('float')
    transformed /= np.max(image)
    transformed = c*transformed**gvalue
    transformed *= np.max(image)
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
    transformed /=  np.max(transformed)
    transformed =  (transformed/r0)**E/(1 + (transformed/r0)**E)
    transformed *= np.max(image)
    transformed = transformed.astype('uint8')
    return transformed



