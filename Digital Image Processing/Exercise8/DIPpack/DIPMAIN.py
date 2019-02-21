from DIPpack.imginfo import getinfo
from DIPpack.interpol import Interpolate
from DIPpack.colormap import colormapping
from DIPpack.transformations import gamma_transform, contrast_stretch, histeq, lapsharp, smoothing
import numpy as np
from PIL import Image



class DiPpackage:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = np.array(Image.open(image_path))


    def show(self):
        return self.image


    def gamma_transform(self, gamma, c = 1):
        """
        gamma -> Gamma value
        c -> constant

        Returns 0-255 int array
        """
        return gamma_transform(self.image, gamma)

    def getinfo(self):
        """Image --> path to image"""
        getinfo(self.image_path)
    
    def Interpolate(self, newN, newM, interp):
        """
        ARGS:
        newN -> New N dimension
        newM -> New M dimension

        interp:

        'NEAREST',
        'LINEAR',
        'CUBIC',
        'LANCZOS'
        """
        return Interpolate(self.image, newN, newM, interp)

    def contrast_stretch(self, E, r0 = 0.5):
        """
        E = Contrast stretch factor
        r0 = constant

        Returns 0-255 int array
        """
        return contrast_stretch(self.image, E, r0)


    def histeq(self, L = 256, prob = False, stairplot = False):
        """
        L -> max intensity level i.e 256
        prob = True returns probability array, default = False
        stairplot = False -> plots staircase plot

        Return result, probability
        or 
        Return result
        """
        return histeq(self.image, L, prob, stairplot)



    def smoothing(self, boxsize = 3):
        """
        Avarage smoothing of 2D array
        boxsize -> size of boxkernal filter
        returns filtered 2D array
        *(truncate)
        """
        return smoothing(self.image, boxsize)
    

    def lapsharp(self, maskret = False):
        """
        maskret = True -> returns result and mask
        maskret = False -> returns result

        *(truncate)
        """

        return lapsharp(self.image, maskret)



    def colormap(self, values, colors):
        """
        Image -> numpy array
        values = [0,1,2,3,4,5,6,...]\n
        colors = {'red': [2,5,1,81,12,43,8,..], 'green': [2,5,1,81,12,43,8,..], 
        'blue': [2,5,1,81,12,43,8,..]}

        maps values 0,1,.... to color red2,5,...+ green2,5,... + blue,2,5,....
        Example: 0 intensity will map to color (2, 2, 2) (RGB) etc.
        If not specified it turns black -> (0, 0, 0).
        # """

        return colormapping(self.image, values, colors)