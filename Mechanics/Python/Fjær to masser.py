import numpy as np
import matplotlib.pyplot as plt


x1array = [0]
x2array = [1.5]
dx1array = [0]
dx2array = [0]
tarray = []


i = 0
dt = 0.01
k = 1
t = 0
m = 1
while t < 10:
    ddx1 = -k*(2*x1array[i]-x2array[i])/m
    ddx2 = -k*(2*x2array[i]-x1array[i])/m
    dx1 = ddx1 *dt + dx1array[i]
    dx2 = ddx2 * dt + dx2array[i]
    x1 = dx1 *dt + x1array[i]
    x2 = dx2 *dt + x2array[i]
    x1array.append(x1)
    x2array.append(x2)
    dx1array.append(dx1)
    dx2array.append(dx2)
    t += dt
    tarray.append(t)
    i += 1

plt.plot(tarray,x1array[:-1])
plt.plot(tarray,x2array[:-1])
plt.show()