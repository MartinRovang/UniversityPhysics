import foxxstats
import matplotlib.pyplot as plt
import numpy as np
import random
x = [random.gauss(0,1) for i in range(0, 100)]



k = foxxstats.MovingAvarage(x, 5)
#k = foxxstats.RandomWalk(0.02, 1000)

plt.plot(x, color = 'black')
plt.plot(k.values())
#plt.plot(0.02*np.arange(0, 1000, 1)+10)

# v = np.array([((x[i] + x[i + 1] + x[i+2])/3) for i in range(0, 100-3)])
# plt.plot(v)


plt.show()