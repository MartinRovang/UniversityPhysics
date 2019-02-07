import numpy as np 
from PIL import Image
import matplotlib.pyplot as plt


I = np.asarray(Image.open('rose1024.tif')).astype('uint8')
I = np.asarray(Image.open('rose1024.tif')).astype('float')

# max_value = np.max(I)
# I *= 1/max_value
# I *= max_value 
I *= 0.5
I = I.astype('uint8')


print(I)


plt.imshow(I)
plt.show()