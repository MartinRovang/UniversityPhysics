
import cv2

def Interpolate(img, newN, newM, interp):
    """
    ARGS:
    newN -> New N dimension
    newM -> New M dimension

    interp:

    'NEAREST',
    'LINEAR',
    'BICUBIC',
    'LANCZOS'
    """

    #res = np.array(Image.fromarray(img).resize((N, M), eval('Image.%s'%interp)))
    res = cv2.resize(img, (newN, newM) , interpolation = eval('cv2.INTER_%s'%interp))
    return res