from statsmodels.tsa.stattools import acf, pacf, ccf
from statsmodels.tsa.arima_process import arma2ma, arma2ar, ArmaProcess

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os


# g)

def AR1(a, phi, n, M):
    x = np.zeros(n)
    x[0] = 1
    for i in range(1, n):
        x[i] = a + phi*x[i-1] + np.random.normal(0, 1)

    phi1 = np.zeros(M+1)
    for i in range(M+1):
        phi1[i] = phi**i

    BLP = np.zeros(M+1)
    for i in range(M+1):
        BLP[i] = a*np.sum(phi1[:i]) + phi**(i)*x[-1]


    error_phi = np.zeros(M+1)
    for i in range(0, M):
        error_phi[i] = phi**(2*i)
    
    error = np.zeros(M+1)
    for i in range(M+1):
        error[i] = np.sum(error_phi[:i])

    return x, BLP, error




x, BLP, error = AR1(1.1, 0.90, 100, 40)
x_list = np.arange(len(x)-1, len(x) + len(BLP)-1, 1)


plt.plot(x,linewidth = '1' , label = 'AR(1)')
plt.fill_between(x_list, BLP+2*np.sqrt(error), BLP-2*np.sqrt(error), edgecolor=(0,0,0,0.3), facecolor = (0,0,1,0.05), label = 'Prediction error 95%')
#plt.fill_between(x_list, BLP+error, BLP-error, facecolor = 'blue', alpha = 0.1, label = 'Prediction error')
plt.plot(x_list, BLP, '-o', mfc='none', color = 'red', linewidth = '1', label = 'Prediction')
plt.legend(loc = 'best')
plt.show()





# arparams = np.array([-.9])
# maparams = np.array([-0.7, 0])
# ar = np.r_[1, arparams] # add zero-lag and negate
# ma = np.r_[1, maparams] # add zero-lag

# arma_process = ArmaProcess(ar, ma)
# y = arma_process.generate_sample(250)
# fig, ax = plt.subplots(1,2)
# ax[0].stem(acf(y))
# ax[1].stem(pacf(y))
# plt.show()