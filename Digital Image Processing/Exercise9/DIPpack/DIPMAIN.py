from DIPpack.imginfo import getinfo
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import exifread
from pprint import pprint
from scipy.signal import convolve2d
from scipy.ndimage.interpolation import rotate
import cv2


class DiPpackage:
    """Initate the image for processing\n
        image_path = None, image_new: 2Darray"""
    def __init__(self, image_path = None, image_new = [[None]]):
        """Initate the image for processing"""
        self.image_path = image_path
        if image_new[0][0] != None:
            self.image = image_new
        elif image_path != None:
            self.image = np.array(Image.open(image_path))
        else:
            raise Exception('You must an image input')

    def rotate(self, angle, axes=(1, 0), reshape=True, output=None, order=3, mode='constant', cval=0.0, prefilter=True):
        """Rotate image"""

        return rotate(self.image, angle, axes=(1, 0), reshape=True, output=None, order=3, mode='constant', cval=0.0, prefilter=True)

    def plot(self, ax = 'plt', cmap = 'gray'):
        """Plots the image"""
        eval(f'{ax}.imshow(self.image, cmap = cmap, vmin = 0, vmax = 255)')


    def transform_image_255(self, image):
        image *= 255
        image = image.astype('uint8')
        return image

    def transform_image_01(self, image):
        transformed = image.astype('float')
        transformed /= 255
        return transformed


    def gamma_transform(self, gamma, c = 1):
        """
        Image -> Image
        gamma -> Gamma value
        c -> constant

        Returns 0-255 int array
        """

        transformed = self.transform_image_01(self.image)
        transformed = c*transformed**gamma

        transformed = self.transform_image_255(transformed)
        return transformed

    def getinfo(self):
        """Image --> path to image"""
        im = open(Image, 'rb')
        tags = exifread.process_file(im)
        pprint(tags)
    
    def interpolate(self, newN, newM, interp):
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

        #res = np.array(Image.fromarray(img).resize((N, M), eval('Image.%s'%interp)))
        res = cv2.resize(self.image, (newN, newM) , interpolation = eval('cv2.INTER_%s'%interp))
        return res

    def contrast_stretch(self, E, r0 = 0.5):
        """
        Image -> Image
        E = Contrast stretch factor
        r0 = constant

        Returns 0-255 int array
        """
        transformed = self.transform_image_01(self.image)
        transformed = ((transformed / r0) **E)/(1 + (transformed / r0) **E)
        transformed = self.transform_image_255(transformed)


        return transformed


    def histeq(self, L, prob = False, stairplot = False):
        """
        img -> np array
        L -> max intensity level i.e 256
        prob = True returns probability array, default = False
        stairplot = False -> plots staircase plot default = False

        Return result, probability
        or 
        Return result
        """
        M, N = self.img.shape
        hist, bins = np.histogram(self.img.flatten(),L,[0,L])
        probability = hist/(M*N)
        result = self.img.astype('float')
        stair = []

        for i in range(0, L):
            idx = np.where(self.img == i)
            result[idx] = (L-1)*np.sum(probability[0:i+1])
            stair.append((L-1)*np.sum(probability[0:i+1]))
        result = result.astype('uint8')

        if stairplot == True:
            return result, stair

        if prob == True:
            return result, probability
        else:
            return result



    def smoothing(self, boxsize = 3):
        """
        Avarage smoothing of 2D array
        boxsize -> size of boxkernal filter
        returns filtered 2D array
        *(truncate)
        """


        boxkernal = np.ones((boxsize, boxsize))/(boxsize**2)
        #img = np.pad(img, (boxsize, boxsize), mode = 'constant')
        result = convolve2d(self.img, boxkernal, mode = 'same')

        return result
    

    def lapsharp(self, maskret = False):
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
        
        mask = convolve2d(self.img, lapmask, mode = 'same')
        result = self.img + c*mask


        if maskret == True:
            return result, mask
        else:
            return result



    def colormap(self, values, colors):
        """
        Image -> numpy array
        values = [0,1,2,3,4,5,6,...]\n
        colors = {'red': [2,5,1,81,12,43,8,..], 'green': [2,5,1,81,12,43,8,..], 'blue': [2,5,1,81,12,43,8,..]}

        maps values 0,1,.... to color red2,5,...+ green2,5,... + blue,2,5,....
        Example: 0 intensity will map to color (2, 2, 2) (RGB) etc.
        If not specified it turns black -> (0, 0, 0).
        # """
        
        self.image = Image

        try:
            a,b = Image.shape
            NewfigRed = np.zeros((a,b))
            NewfigGreen = np.zeros((a,b))
            NewfigBlue = np.zeros((a,b))
            Newfig = np.zeros((a,b,3))
            for counter, value in enumerate(values):
                dx = np.where(Image == value)
                for color in colors:
                    if color == 'red':
                        NewfigRed[dx] = colors[color][counter]
                    if color == 'green':
                        NewfigGreen[dx] = colors[color][counter]
                    if color == 'blue':
                        NewfigBlue[dx] = colors[color][counter]

            Newfig[:,:,0] = NewfigRed
            Newfig[:,:,1] = NewfigGreen
            Newfig[:,:,2] = NewfigBlue

            return Newfig.astype('uint8')
        except Exception as e:
            print(e)
            print('Dictionary lists(colors) and values list must have same length!')


    def medianfilter(self, boxsize = 3):
        """
        Uses median filter\n
            returns processed image.
        """
        image = self.image
        image_padded = np.pad(image, (boxsize, boxsize) , mode = 'constant')
        result = np.zeros(image.shape)
        rows, cols = image_padded.shape
        # Multiply by 2 because there is 2 time the new pad size in each dimension.
        for row in range((rows-boxsize*2)):
            for col in range((cols-boxsize*2)):
                result[row, col] = np.median(image[row:row + boxsize+1,col:col + boxsize+1].flatten())
        return result



    def fft(self):
        fft = np.fft.fft2(self.image)
        fft = np.fft.fftshift(fft)
        return fft
    
    def ifft(self, N = 1):
        fft = np.fft.ifft2(self.image)
        return fft



