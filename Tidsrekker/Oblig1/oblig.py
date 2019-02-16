
import numpy as np 
from statsmodels.tsa.stattools import acf
import random
import matplotlib.pyplot as plt

data = np.array([random.gauss(0,1) for x in range(200)])

# random_walk = np.cumsum(data)

# t = np.linspace(0,1000, 1)

# signal = np.cos(t) + data

# differenced = []
# for i in range(1,len(data)):
#     try:
#         differenced.append(data[i] - data[i - 1])
#     except:
#         print('failed')


o = np.array([np.sqrt(1/len(data)) for x in range(40)])*2

# k = acf(differenced)
# plt.plot(data)
# plt.stem(k)
# plt.show()

n = 250
rho = np.array([random.gauss(0,1/n) for x in range(n)])




# plt.plot(-o,'--', color = 'black', label = '$2/\sqrt{n}$')
# plt.plot(o,'--' , color = 'black')
# plt.stem(acf(data), label = 'ACF')
# plt.legend(loc = 'best')
# plt.xlabel('Lag', fontsize = 15)
# plt.ylabel('$\hat{\\rho}(h)$', fontsize = 15)
# plt.show()


from scipy.stats import norm
ss = norm.cdf(2) - norm.cdf(-2)
print(ss)


