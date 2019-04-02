import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from HSI import RGB_to_HSI


test = plt.imread('Fig0630(01)(strawberries_fullcolor).tif')

blaklokke = plt.imread('blaklokke.jpg')
red_blaklokke = blaklokke[:,:,0]
green_blaklokke = blaklokke[:,:,1]
blue_blaklokke = blaklokke[:,:,2] 

# Task a
fig, ax = plt.subplots(2,2)
ax[0,0].imshow(blaklokke)
ax[0,0].set_title('Original')
ax[0,1].imshow(red_blaklokke, cmap = 'gray')
ax[0,1].set_title('Red channel')
ax[1,0].imshow(green_blaklokke, cmap = 'gray')
ax[1,0].set_title('Green channel')
ax[1,1].imshow(blue_blaklokke, cmap = 'gray')
ax[1,1].set_title('Blue channel')
plt.tight_layout()
plt.show()


# Task b
fig, ax = plt.subplots(1,3, figsize = [15,5])
ax[0].hist(red_blaklokke.flatten(), bins = 256)
ax[0].set_title('Red channel')
ax[1].hist(blue_blaklokke.flatten(), bins = 256)
ax[1].set_title('Green channel')
ax[2].hist(green_blaklokke.flatten(), bins = 256)
ax[2].set_title('Blue channel')
plt.tight_layout()
plt.show()


# Task C
H, S, I = RGB_to_HSI(blaklokke)

fig, ax = plt.subplots(2,2)
ax[0,0].imshow(blaklokke)
ax[0,0].set_title('Original')
ax[0,1].imshow(H, cmap = 'gray')
ax[0,1].set_title('Hue')
ax[1,0].imshow(S, cmap = 'gray')
ax[1,0].set_title('Saturation')
ax[1,1].imshow(I, cmap = 'gray')
ax[1,1].set_title('Intensity')
plt.tight_layout()
plt.show()



# Task D
fig, ax = plt.subplots(1,3, figsize = [15,5])
ax[0].hist(H.flatten(), bins = 256)
ax[0].set_title('Hue channel')
ax[1].hist(S.flatten(), bins = 256)
ax[1].set_title('Saturation channel')
ax[2].hist(I.flatten(), bins = 256)
ax[2].set_title('Intensity channel')
plt.tight_layout()
plt.show()