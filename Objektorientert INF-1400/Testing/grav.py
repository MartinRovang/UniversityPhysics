import numpy as np 
import matplotlib.pyplot as plt


xx, yy = np.arange(-10, 10, 0.1), np.arange(-10, 10, 0.1)
X, Y = np.meshgrid(xx, yy)
 
r, theta = np.sqrt(X**2 + Y**2), np.arctan2(Y,X)


g = -1/(r**2+1)




plt.imshow(g, cmap = 'inferno')
plt.colorbar()
plt.show()

