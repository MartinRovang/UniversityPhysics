

import matplotlib.pyplot as plt 
import numpy as np 

X, Y = np.meshgrid(np.linspace(-2,2,500), np.linspace(-2,2,500))

r = np.sqrt(X**2 + Y**2)

Z = -100/r**2
Z[Z < -1000] = -1000


Zx = Z*np.cos(np.arctan(Y/X))
Zy = Z*np.sin(np.arctan(Y/X))

idx = np.where(X < 0)
Zx[idx]*= -1
Zy[idx]*= -1

Zx[Z == -1000] = 0
Zy[Z == -1000] = 0




plt.streamplot(X, Y, Zx, Zy, linewidth= 1, color = 'black')
plt.contourf(X, Y, Z, 300, cmap = plt.cm.jet)
plt.colorbar()
plt.show()