import numpy as np 
from scipy.io.wavfile import read, write
import matplotlib.pyplot as plt

print(100000/44100)


x = np.zeros(100000)
phi = -0.8

for i in range(1, len(x)):
    x[i] = phi*x[i-1] + np.random.normal(0,1)


plt.plot(x)
plt.show()


x = x/np.max(x)


write('test.wav', 44100, x)