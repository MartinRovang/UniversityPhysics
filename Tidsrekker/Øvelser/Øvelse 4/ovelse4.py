

#%%

# 1.20
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf


white_noise = np.random.normal(0,1,50)

def acvff(x, maxlag):
    y = []
    n = len(x)
    for h in range(0,maxlag+1):
        res = 0
        for t in range(0, n-h):
            res += (x[t+h] - np.mean(x))*(x[t] - np.mean(x))
        res *= n**(-1)
        y.append(res)
    
    return np.array(y)


def acff(x, maxlag, _acvf):
    return _acvf(x, maxlag)/_acvf(x, maxlag)[0]




plt.stem(acvff(white_noise, 20))
plt.show()


plt.stem(acff(white_noise, 20, acvff))
plt.show()



#Actual
plt.stem([1 if i == 0 else 0 for i in range(20+1)])
plt.show()

# The bigger the sample is the closer to the actual ACF we get. 



#%%

# 1.21

import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf

class MovingAvarage(object):
    def __init__(self, data, q):
        self.data = data
        self.q = q



    def values(self):
        q = self.q
        result = np.zeros(len(self.data) - q)
        for i in range(q, len(self.data) - q + 1):
            for j in range(-q , q + 1):
                result[-i] += self.data[-i -j]
            result[-i] /= 2*q + 1
        
        return result




def moving_av_(x,q):
    y = []
    n = len(x)
    for i in range(n-q):
        res = 0
        res = x[i] + x[i+1] + x[i+2]
        res *= 1/3
        y.append(res)
    return y






#Example 1.12
n = 500

t = np.arange(0,n,1)
white_noise = np.random.normal(0,1,n)

x = 2*np.cos(2*np.pi*(t+15)/50) + white_noise

plt.plot(x)
plt.show()

moving_av = MovingAvarage(x, 3)

plt.plot(moving_av.values())
plt.show()

plt.stem(acf(moving_av.values(), nlags = 20))
plt.show()



n = 50

t = np.arange(0,n,1)
white_noise = np.random.normal(0,1,n)

x = 2*np.cos(2*np.pi*(t+15)/50) + white_noise
moving_av = MovingAvarage(x, 3)

plt.stem(acf(moving_av.values(), nlags = 20))
plt.show()


#%%
n = 50

t = np.arange(0,n,1)
white_noise = np.random.normal(0,1,n)

x = 2*np.cos(2*np.pi*(t+15)/50) + white_noise
moving_av = moving_av_(x, 3)

plt.stem(acf(moving_av, nlags = 20))
plt.show()

plt.plot(moving_av)
plt.show()


# Virker ikke som antall gjør stort utslag ved moving avarage, men den skiller seg veldig
# ut med ekte ACF da ekte ACF vil være null ved lag større en q(moving avarage filter length)
# TEORETISK != SAMPLE




#%%
#1.22

import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf


n = 200

t = np.arange(0,n,1)
white_noise = np.random.normal(0,1,n)

x = 10*np.exp(-(t-100)/20)*np.cos(2*np.pi*t/4) + white_noise
x[:100] = 0

plt.plot(x)
plt.show()

plt.stem(acf(x))
plt.show()


# The more lags the less correlation, and the correlation is fluctuates between positive and
# negative correlation and zero.
#%%

# 1.23

import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf


n = 500

t = np.arange(0,n,1)
white_noise = np.random.normal(0,1,n)

x = 2*np.cos(2*np.pi*(t+15)/50) + white_noise

plt.plot(x)
plt.show()

plt.stem(acf(x, nlags= 100))
plt.show()


# The correlation is seasonal and follows a cosine.

