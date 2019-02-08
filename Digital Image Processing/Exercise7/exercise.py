#%%
# EX 2

import numpy as np 
from PIL import Image
import matplotlib.pyplot as plt


I = np.asarray(Image.open('aerial_view.tif')).astype('uint8')
I = np.asarray(Image.open('aerial_view.tif')).astype('float')

# max_value = np.max(I)
# I *= 1/max_value
# I *= max_value 
I *= 0.5
I = I.astype('uint8')






#%%
# EX 3

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

I1 = np.asarray(Image.open('aerial_view.tif')).astype('float')
I2 = np.asarray(Image.open('spine.tif')).astype('float')

def gamma_transform(image, gvalue, c = 1.0):
    max_value = np.max(image)
    transformed = image.astype('float')
    transformed *= 1.0/max_value
    transformed = c*transformed**gvalue
    return transformed

gamma = 0.4
transformed_image1 = gamma_transform(I1, gamma)
transformed_image2 = gamma_transform(I2, gamma)


fig, ax = plt.subplots(2,2, figsize = (10,15))
ax[0,0].imshow(I1, cmap = 'gray')
ax[0,0].set_title('Original')
ax[0,1].imshow(transformed_image1, cmap = 'gray', vmin = 0, vmax = 1)
ax[0,1].set_title('Gamma transform with $\gamma = %s$'%gamma)

ax[1,0].imshow(I2, cmap = 'gray')
ax[1,0].set_title('Original')
ax[1,1].imshow(transformed_image2, cmap = 'gray', vmin = 0, vmax = 1)
ax[1,1].set_title('Gamma transform with $\gamma = %s$'%gamma)

fig.tight_layout()
plt.show()



#%%
# EX 3

gamma = 1

I1 = np.asarray(Image.open('aerial_view.tif'))
I2 = np.asarray(Image.open('spine.tif'))

def gamma_transform(image, gvalue, k_bit = 3, c = 1.0):
    max_value = np.max(image)
    transformed = image.astype('float')
    transformed *= 1/max_value
    transformed = c*transformed**gvalue
    transformed *= max_value
    transformed = transformed.astype('uint%s'%2**(k_bit))
    print(len(np.unique(transformed)))
    #print(transformed)
    return transformed

transformed_image1 = gamma_transform(I1, gamma)
transformed_image2 = gamma_transform(I2, gamma)


fig, ax = plt.subplots(2,2, figsize = (10,15))
ax[0,0].imshow(I1, cmap = 'gray')
ax[0,0].set_title('Original')
ax[0,1].imshow(transformed_image1, cmap = 'gray')
ax[0,1].set_title('Gamma transform with $\gamma = %s$'%gamma)

ax[1,0].imshow(I2, cmap = 'gray')
ax[1,0].set_title('Original')
ax[1,1].imshow(transformed_image2, cmap = 'gray')
ax[1,1].set_title('Gamma transform with $\gamma = %s$'%gamma)

plt.tight_layout()
plt.show()



#%% EX 4 a)

I = np.asarray(Image.open('magnified-pollen-dark.tif'))

def contrast_strech(image, E, r0 = 0.5):
    max_value = np.max(image)
    transformed = image.astype('float')
    transformed *= 1/max_value
    transformed =  (transformed/r0)**E/(1 + (transformed/r0)**E)
    transformed *= max_value
    transformed = transformed.astype('uint%s'%2**(k_bit))
    return transformed

E, r0 = [2,4,6,8], 0.5
transformed_image1 = contrast_strech(I, E[0], r0)
transformed_image2 = contrast_strech(I, E[1], r0)
transformed_image3 = contrast_strech(I, E[2], r0)
transformed_image4 = contrast_strech(I, E[3], r0)



fig, ax = plt.subplots(3,2, figsize = (10,15))
ax[0,0].imshow(I, cmap = 'gray')
ax[0,0].set_title('Original')

ax[0,1].imshow(transformed_image1, cmap = 'gray')
ax[0,1].set_title('Contrast stretch E = %s, r = %s'%(E[0],r0))

ax[1,0].imshow(transformed_image2, cmap = 'gray')
ax[1,0].set_title('Contrast stretch E = %s, r = %s'%(E[1],r0))

ax[1,1].imshow(transformed_image3, cmap = 'gray')
ax[1,1].set_title('Contrast stretch E = %s, r = %s'%(E[2],r0))

ax[2,0].imshow(transformed_image4, cmap = 'gray')
ax[2,0].set_title('Contrast stretch E = %s, r = %s'%(E[3],r0))

plt.tight_layout()
plt.show()


#%%
