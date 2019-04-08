import matplotlib.pyplot as plt 
import numpy as np 
from statsmodels.tsa.stattools import acf, pacf, ccf
from statsmodels.tsa.arima_process import arma2ma, arma2ar
import pandas as pd


def arma1(p, q, phi, theta, N):
    ######### SAMPLE ACF ########
    x = np.zeros(N)
    white = np.random.normal(0,1,N)
    if p == 0:
        phi = 0
    if q == 0:
        theta = 0
    for i in range(1, N):
        x[i] = phi*x[i-1] + theta*white[i-1] + white[i]
    

    ###### THEORETICAL ACF ARMA(1,1) #######
    h = np.arange(1,10,1)
    top = (1 + theta*phi)*(phi + theta)
    bot = (1 + 2*phi*theta + theta**2)
    rho = (top/bot)*phi**(h-1)


    # Plot
    fig, ax = plt.subplots(1,3)
    ax[0].plot(x)
    ax[0].set_title('ARMA(%s,%s), $\\phi = %s,\\theta = %s$'%(p ,q, phi, theta))
    ax[1].stem(acf(x, nlags = 10))
    ax[1].set_title('SAMPLE ACF')
    ax[2].stem(rho)
    ax[2].set_title('THEORETICAL ACF')
    plt.tight_layout()
    plt.show()


def ar1(phi, N):
    x = np.zeros(N)
    white = np.random.normal(0,1,N)
    for i in range(1, N):
        x[i] = phi*x[i-1] + white[i]
    return x


def acf_plot(x, lag):
    plt.stem(acf(x, nlags=lag))
    plt.show()

def pacf_plot(x, lag):
    plt.stem(pacf(x, nlags=lag))
    plt.show()


cmort = np.genfromtxt('cmort.txt', delimiter= '\t')[1:,1]
rec = np.genfromtxt('rec.txt', delimiter= '\t')[1:,1]
cmort = pd.DataFrame(np.diff(np.log(cmort), 1))
rec = pd.DataFrame(np.diff(np.log(rec), 1))





