from statsmodels.tsa.stattools import acf, pacf, ccf
from statsmodels.tsa.arima_process import arma2ma, arma2ar
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os


# g)

def AR1(a, phi, n, M):
    x = np.zeros(n)
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






x, BLP, error_phi1 = AR1(1.1, 0.9, 150, 30)

x_list = np.arange(len(x)-1, len(x) + len(BLP)-1, 1)


plt.plot(x,linewidth = '1' , label = 'AR(1)')
#plt.fill_between(x_list, BLP+2*error_phi1, BLP-2*error_phi1, facecolor = 'blue', alpha = 0.1, label = 'Prediction error 2std')
plt.fill_between(x_list, BLP+error_phi1, BLP-error_phi1, facecolor = 'blue', alpha = 0.1, label = 'Prediction error')
plt.plot(x_list, BLP, '--', color = 'black', linewidth = '1', label = 'Prediction')
plt.legend(loc = 'best')
plt.show()