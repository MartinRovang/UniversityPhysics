import matplotlib.pyplot as plt 
from scipy.io.wavfile import read, write
import numpy as np

def saw(N, t, f):
    result = []
    t = np.arange(0, t, 1/20000)
    n = np.arange(1, N, 1)
    result = np.zeros(t.shape)
    for i,x in enumerate(t):
        result[i] = np.sum((1/n)*np.sin(np.pi*n*x*f))
        result[i] /= np.pi
    
    return result


x = saw(500, 10, 2)
plt.plot(x)
plt.show()


write('test.wav', 44100, x)
