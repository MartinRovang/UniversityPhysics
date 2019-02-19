#%%
import matplotlib.pyplot as plt
import numpy as np 
from PIL import Image
from DIPpack import histeq



fig3161 = np.array(Image.open('3161.tif'))
fig3162 = np.array(Image.open('3162.tif'))
fig3163 = np.array(Image.open('3163.tif'))
fig3164 = np.array(Image.open('3164.tif'))

#fig, ax = plt.subplots(2,1)


plt.imshow(fig3161, cmap = 'gray', vmin = 0, vmax = 255)
plt.show()
plt.hist(fig3161.flatten(), range = [0,255], bins = 255, color = 'white')
plt.show()


#%%
import matplotlib.pyplot as plt
from DIPpack import histeq


equalized1 = histeq(fig3161, L = 256)
equalized2 = histeq(fig3162, L = 256)
equalized3 = histeq(fig3163, L = 256)
equalized4 = histeq(fig3164, L = 256)

fig, ax = plt.subplots(4,3, figsize = [20,20])


ax[0,0].imshow(fig3161, cmap = 'gray', vmin = 0, vmax = 255)
ax[0,1].imshow(equalized1, cmap = 'gray', vmin = 0, vmax = 255)
ax[0,2].hist(equalized1.flatten(), range = [0,255], bins = 255, color = 'white')

ax[1,0].imshow(fig3162, cmap = 'gray', vmin = 0, vmax = 255)
ax[1,1].imshow(equalized2, cmap = 'gray', vmin = 0, vmax = 255)
ax[1,2].hist(equalized2.flatten(), range = [0,255], bins = 255, color = 'white')

ax[2,0].imshow(fig3163, cmap = 'gray', vmin = 0, vmax = 255)
ax[2,1].imshow(equalized3, cmap = 'gray', vmin = 0, vmax = 255)
ax[2,2].hist(equalized3.flatten(), range = [0,255], bins = 255, color = 'white')

ax[3,0].imshow(fig3164, cmap = 'gray', vmin = 0, vmax = 255)
ax[3,1].imshow(equalized4, cmap = 'gray', vmin = 0, vmax = 255)
ax[3,2].hist(equalized4.flatten(), range = [0,255], bins = 255, color = 'white')


plt.tight_layout()
plt.show()


# plt.hist(equalized.flatten(), range = [0,255], bins = 255, color = 'white')
# plt.show()

# plt.imshow(fig3161, cmap = 'gray', vmin = 0, vmax = 255)
# plt.show()
# plt.imshow(equalized, cmap = 'gray', vmin = 0, vmax = 255)
# plt.show()


# plt.plot(probability)
# plt.show()


#%%


from scipy.signal import convolve2d
import matplotlib.pyplot as plt
import numpy as np 
from PIL import Image


fig333 = np.array(Image.open('fig333.tif'))


def smoothing(img, boxsize = 3):
    boxkernal = np.ones((boxsize, boxsize))/(boxsize**2)
    img = np.pad(img, (boxsize, boxsize), mode = 'constant')

    result = convolve2d(boxkernal, img, mode = 'valid')

    return result



result1 = smoothing(fig333, boxsize = 3)
result2 = smoothing(fig333, boxsize = 11)
result3 = smoothing(fig333, boxsize = 21)

fig, ax = plt.subplots(2,2, figsize = [15,15])

ax[0,0].imshow(fig333, cmap = 'gray')
ax[0,1].imshow(result1, cmap = 'gray')
ax[1,0].imshow(result2, cmap = 'gray')
ax[1,1].imshow(result3, cmap = 'gray')
plt.show()






#%%


from scipy.signal import convolve2d
import matplotlib.pyplot as plt
import numpy as np 
from PIL import Image


blurrymoon = np.array(Image.open('blurrymoon.tif'))


def lapsharp(img, maskret = False):
    """
    img -> 2D array
    maskret = True -> returns result and mask
    maskret = False -> returns result
    """
    lapmask = np.zeros((3, 3))
    padded_image = np.pad(img, (1, 1), mode = 'symmetric')
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
    
    edges = convolve2d(lapmask, padded_image, mode = 'valid')
    result = img + c*edges

    if maskret == True:
        return result, mask
    else:
        return result


result = lapsharp(blurrymoon)

fig, ax = plt.subplots(1,2, figsize = [15, 15])

ax[0].imshow(blurrymoon, cmap = 'gray', vmin = 0, vmax = 255)
ax[1].imshow(result, cmap = 'gray', vmin = 0, vmax = 255)
plt.show()

#%%