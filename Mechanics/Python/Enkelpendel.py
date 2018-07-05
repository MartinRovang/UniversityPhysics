import numpy as np
import matplotlib.pyplot as plt




xarray = [1]
dxarray = [0]
tarray = [0]
dt = 0.1
t = 0
ddxarray = [0]


while t < 30:
    ddx = -(9.81/2)*np.sin(xarray[-1])
    dx = ddx*dt + dxarray[-1]
    x =  dx*dt + xarray[-1]
    t += dt
    tarray.append(t)
    xarray.append(x)
    dxarray.append(dx)
    ddxarray.append(ddx)




plt.plot(tarray,xarray)
plt.show()

