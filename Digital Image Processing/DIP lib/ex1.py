
#%%
import matplotlib.pyplot as plt
import numpy as np 
import scipy
import os, sys
from PIL import Image

#a,b
# 7 rows and 8 columns
A = np.zeros((7,8))

#c

A[:,0] = 1; A[:,1] = 2; A[:,2] = 3; A[4,6] = 5; A[5,6] = 8

print(A)
#d

# NOTEE ON UNIQUE VALUES, every intensity so in this case 1,2,3,5,8
print(np.unique(A))


#e
B = np.random.randint(0, 10, (8,7))

#f

C = A@B



#%% #g
# Flipped
from scipy import misc

flipped_A = np.flipud(A) #A[::-1] # flipusd with numpy
flipped_left_right = np.flip(flipped_A, axis = 1)
ninety_deg = np.rot90(flipped_left_right, k = 1, axes = (0,1))
rot37 = scipy.misc.imrotate(ninety_deg, 37)

img = Image.fromarray(ninety_deg)
rotarr = np.array(img.rotate(37))

plt.imshow(A)
plt.show()
plt.imshow(flipped_A)
plt.show()
plt.imshow(flipped_left_right)
plt.show()
plt.imshow(ninety_deg)
plt.show()
plt.imshow(rot37)
plt.show()
plt.imshow(rotarr)
plt.show()

# h
#%%
from scipy.io import savemat, loadmat
savemat("MatrixA.mat", {'MatrixA':A})




#%%
#### EX 3 A

from scipy import misc
fig2007 = plt.imread('fig2007.tif')
plt.imshow(fig2007, cmap = 'gray')
plt.show()

I = fig2007[1200,:]

plt.plot(I)
plt.show()

unique_values, index = np.unique(fig2007, return_counts = True)
# ls = np.where(index == 1)
# unique_values = unique_values[ls]
# print(unique_values)
print('Amount of unique vals: ',len(unique_values))




#%%


#### EX 3 B


import exifread
from pprint import pprint
im = open('fig2007.tif', 'rb')
tags = exifread.process_file(im)
pprint(tags)


#%%  C
fig2007 = plt.imread('fig2007.tif')
plt.imshow(fig2007, cmap = 'gray')
plt.show()




#%% E

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap
band_colors_number = np.unique(fig2007)

print(unique_values)

# COLOR INTENSITY
N = 6
# RGB MATRIX
vals = np.zeros((N, 3))

# # RED
# vals[:, 0] = np.linspace(1, 0, N)
# # GREEN
# vals[:, 1] = np.linspace(1, 0, N)
# # BLUE
# vals[:, 2] = np.linspace(1, 0, N)

# RED, # GREEN, # BLUE, N = 6 total colors
vals[:, 0], vals[0, 1], vals[:, 2]  =  (0,255/255,0)

# red
vals[1, 0], vals[1, 1], vals[0, 2]  =  (255/255,0,0)

# Orange 255-165-0
vals[2, 0], vals[2, 1], vals[0, 2]  =  (255/255, 165/255,0)

# yellow 	255-255-0
vals[3, 0], vals[3, 1], vals[0, 2]  =  (255/255,255/255,0)

#pink 	255-20-147
vals[4, 0], vals[4, 1], vals[4, 2]  =  (255/255,20/255,147/255)

#black 	0,0,0
vals[5, 0], vals[5, 1], vals[5, 2]  =  (0,0,0)



# MAKE COLORMAP
newcmp = ListedColormap(vals)

plt.figure(figsize = (20,10))
fig2007 = plt.imread('fig2007.tif')
plt.imshow(fig2007, cmap = newcmp)
plt.savefig('homemadecolormap.png')
plt.show()
#%%
#Exercise 4


#%%

#EX 6 A

from scipy.io import savemat, loadmat
IM1 = loadmat('IM1.mat')['IM1']


plt.imshow(B)
plt.colorbar()
plt.show()




#%%
#EX 6 B
from scipy import misc
from scipy.misc import imresize
from scipy.interpolate import interp2d, NearestNDInterpolator
from PIL import Image
import cv2

def zoomout(img, N, M, interp):
    try:
        a, b = img.shape
    except ValueError:
        a, b, c = img.shape

    x,y = np.arange(0,a), np.arange(0,b)
    xx,yy = np.linspace(0,a, M), np.linspace(0,b, N)

    if interp == 'nearest':
        X,Y = np.meshgrid(x,y)
        XX, YY = np.meshgrid(xx,yy)
        X_array, Y_array = X.flatten(), Y.flatten()
        points = np.transpose(np.vstack((X_array, Y_array)))
        IM = np.reshape(img,(1, int(a*b)), order = 'C')
        Interpolator = NearestNDInterpolator(points, IM[0])
        res = Interpolator(XX,YY)

    else:
        Interpolator = interp2d(x, y, img, kind = interp)
        res = Interpolator(xx, yy)

    return res


def zoomout(img, N, M, interp):
    """
    ARGS:

    NEAREST,
    LINEAR,
    BICUBIC,
    LANCZOS
    """

    #res = np.array(Image.fromarray(img).resize((N, M), eval('Image.%s'%interp)))
    res = cv2.resize(img, (N, M) , interpolation = eval('cv2.INTER_%s'%interp))
    return res



B = plt.imread('test.jpg')
plt.imshow(IM1)
plt.savefig('original.png')
plt.show()
plt.imshow(zoomout(IM1, 500, 500, 'LINEAR'))
plt.savefig('zoomed.png')
plt.show()
# plt.imshow(B)
# plt.colorbar()
# plt.show()





#%%
import numpy as np

x = np.zeros((2,2,3))

#RGB
x[0, 0, 0] = 255/255
x[0, 0, 1] = 255/255
x[0, 0, 2] = 255/255
# x[0, 1, 0] = 10
# x[1, 0, 0] = 40
# x[1, 1, 0] = 30



plt.imshow(x)
plt.show()
#%%


A = np.array(plt.imread('test.jpg'))
A[:,:,0] = 0


plt.imshow(A)
plt.show()


#%%
# NEW COLORMAP

# vals[:, 0], vals[0, 1], vals[:, 2]  =  (0,255/255,0)

# # red
# vals[1, 0], vals[1, 1], vals[0, 2]  =  (255/255,0,0)

# # Orange 255-165-0
# vals[2, 0], vals[2, 1], vals[0, 2]  =  (255/255, 165/255,0)

# # yellow 	255-255-0
# vals[3, 0], vals[3, 1], vals[0, 2]  =  (255/255,255/255,0)

# #pink 	255-20-147
# vals[4, 0], vals[4, 1], vals[4, 2]  =  (255/255,20/255,147/255)

# #black 	0,0,0
# vals[5, 0], vals[5, 1], vals[5, 2]  =  (0,0,0)



fig2007 = np.array(plt.imread('test.jpg'))[:,:,0]
fig2007 = plt.imread('fig2007.tif')

#[0.299, 0.587, 0.114] grayscal dot product


print('UniqueVals:',np.unique(fig2007))
a,b = fig2007.shape


NewfigRed = np.zeros((a,b))
NewfigGreen = np.zeros((a,b))
NewfigBlue = np.zeros((a,b))
Newfig = np.zeros((a,b,3))

# Green
dx32 = np.where(fig2007 <= 32)
# Red
dx64 = np.where((fig2007 <= 64) & (fig2007 > 32))
# Orange
dx96 = np.where((fig2007 <= 96) & (fig2007 > 64))
# yellow
dx128 = np.where((fig2007 <= 128) & (fig2007 > 96))
# pink
dx160 = np.where((fig2007 <= 160) & (fig2007 > 128))
# black
dx192 = np.where((fig2007 <= 192) & (fig2007 > 160))

# Green
NewfigGreen[dx32] = 1
# Red
NewfigRed[dx64] = 1
# Orange  (255/255, 165/255,0)
NewfigRed[dx96] = 1
NewfigGreen[dx96] = 165/255
# yellow 	255-255-0
NewfigRed[dx128] = 1
NewfigGreen[dx128] = 1
#pink 	255-20-147
NewfigRed[dx160] = 1
NewfigGreen[dx160] = 20/255
NewfigBlue[dx160] = 147/255
# #black 	0,0,0
NewfigRed[dx192] = 0
NewfigGreen[dx192] = 0
NewfigBlue[dx192] = 0

Newfig[:,:,0] = NewfigRed
Newfig[:,:,1] = NewfigGreen
Newfig[:,:,2] = NewfigBlue


plt.imshow(fig2007, cmap = 'gray')
plt.show()
plt.imshow(Newfig)
plt.show()


#%%
