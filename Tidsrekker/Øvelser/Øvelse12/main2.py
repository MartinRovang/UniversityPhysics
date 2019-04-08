from statsmodels.tsa.stattools import acf, pacf, ccf
from statsmodels.tsa.arima_process import arma2ma, arma2ar
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os



def AR1(phi, N, m):
    x = np.zeros(N)
    x[0] = np.random.normal(0, 1)
    for i in range(1, N):
        x[i] = phi*x[i - 1] + np.random.normal(0, 1)
        
    psi = np.array([phi**j for j in range(N)])
    P = np.cumsum(psi[:m]**2*1)
    return x, P


phi = 0.9
N = 100
m = 100

x, P = AR1(phi, N, m)

plt.plot(x)
plt.fill_between([x for x in range(m)], x+2*np.sqrt(P), x-2*np.sqrt(P), facecolor = (0, 0 , 0, 0.4))
plt.show()


print(f'last P {AR1(phi, N, m)[1][-1]}')
print(f'Variance: {np.var(AR1(phi, N, m)[0])}')