#%%

from DIPpack import Interpolate, lapsharp
from scipy.signal import convolve2d
import matplotlib.pyplot as plt
import numpy as np 
from PIL import Image




back = np.array(Image.open('trashkval.jpg'))
M,N,c = back.shape
plt.axis('off')
plt.imshow(back)
plt.show()

#%%
newback = Interpolate(back, N*5, M*5, 'CUBIC')
print(newback.shape)
plt.figure(figsize = (15,20))
plt.axis('off')
plt.imshow(newback)
plt.savefig('Newkval.png')
plt.show()

# plt.figure(figsize = (15,20))
# lapped1 = lapsharp(newback[:,:,0])
# lapped2 = lapsharp(newback[:,:,1])
# lapped3 = lapsharp(newback[:,:,2])

# lapped = np.zeros(newback.shape)
# lapped[:,:,0] = lapped1
# lapped[:,:,1] = lapped2
# lapped[:,:,2] = lapped3

# plt.axis('off')
# plt.imshow(newback)
# plt.savefig('Newkval2.png')
# plt.show()
