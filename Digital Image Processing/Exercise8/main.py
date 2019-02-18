#%%
import matplotlib.pyplot as plt
import numpy as np 
from PIL import Image
from DIPpack import histeq



fig316 = np.array(Image.open('316.tif'))




#fig, ax = plt.subplots(2,1)


plt.imshow(fig316, cmap = 'gray', vmin = 0, vmax = 255)
plt.show()
plt.hist(fig316.flatten(), range = [0,255], bins = 255, color = 'white')
plt.show()


#%%
import matplotlib.pyplot as plt
from DIPpack import histeq
equalized = histeq(fig316, L = 256)


plt.hist(fig316.flatten(), range = [0,255], bins = 255, color = 'white')
plt.show()
plt.hist(equalized.flatten(), range = [0,255], bins = 255, color = 'white')
plt.show()

plt.imshow(fig316, cmap = 'gray', vmin = 0, vmax = 255)
plt.show()
plt.imshow(equalized, cmap = 'gray', vmin = 0, vmax = 255)
plt.show()


# plt.plot(probability)
# plt.show()


#%%


A = [2,3,1]


print(A[0:1])