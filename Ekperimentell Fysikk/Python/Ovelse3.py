import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy.polynomial.polynomial as poly
import matplotlib.patches as patches
import matplotlib.path as path



SMALL_SIZE = 8
MEDIUM_SIZE = 10
BIGGER_SIZE = 14
plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=BIGGER_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title


#Import data
temp1,first = np.array(np.linspace(5,100,20)),np.array([0.3])
temp2,second = np.array(np.linspace(5,100,20)),np.array([0.2])
temp11 = np.concatenate((first,temp1), axis=0)
temp22 = np.concatenate((second, temp2), axis=0)

volt1 = np.array([0.015,0.184, 0.498, 0.564, 0.798, 1.002, 1.234, 1.390, 1.642, 1.782, 2.001, 2.205, 2.439, 2.615, 2.891, 3.112, 3.336, 3.501, 3.729, 3.940, 4.080])
volt2 = np.array([0.007,0.252, 0.414, 0.607, 0.826, 1.009, 1.235, 1.418, 1.642, 1.852, 2.075, 2.229, 2.447, 2.671, 2.867, 3.067, 3.226, 3.498, 3.744, 3.911, 4.074])


coefs,cov = np.polyfit(temp11, volt1,1,cov=True)
coefs2,cov2 = np.polyfit(temp22, volt2,1,cov=True)

coefs11,cov11 = np.polyfit(temp11,volt1,2,cov=True)
coefs22,cov22 = np.polyfit(temp22, volt2,2,cov=True)

yerr = volt1*0.00003 + 100*0.00003
xerr = np.array([0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.5])
yerr2 = volt2*0.00003 + 100*0.00003
xerr2 = np.array([0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.5])
plt.figure(figsize=(10,6))
plt.yticks(np.arange(0,5,0.5))
plt.plot(temp11,coefs[0]*temp11+coefs[1],label='y = 0.041321x - 0.021002 ')
plt.errorbar(temp11,volt1, xerr=xerr,yerr=yerr, capsize = 2,label='Forsøk 1')
plt.legend(loc='upper left')
plt.xlabel('Temperatur [$^{\circ}$C]')
plt.ylabel('Spenning[mV]')
plt.savefig('Plotreg1.pdf')
plt.show()
plt.figure(figsize=(10,6))
plt.errorbar(temp22,volt2, xerr=xerr2,yerr=yerr2, capsize = 2,label='Forsøk 2')
plt.plot(temp11,coefs2[0]*temp11+coefs2[1],label='y = 0.040915x + 0.004849')
plt.legend(loc='upper left')
plt.xlabel('Temperatur [$^{\circ}$C]')
plt.ylabel('Spenning[mV]')
plt.savefig('Plotreg2.pdf')
plt.show()
from scipy import stats
import sys

#---------------------------RESIDUALS---------------------
Residual = volt1 - (coefs2[0]*temp11+coefs2[1])
Residual2 = volt1 - (coefs11[0]*temp11**2 + coefs11[1]*temp11+coefs11[2])
Residual12 = volt2 - (coefs2[0]*temp22+coefs2[1])
Residual22 = volt2 - (coefs22[0]*temp22**2 + coefs22[1]*temp22+coefs22[2])

#!/usr/bin/env python
import numpy as np
import matplotlib.mlab as mlab

# the histogram of the data
plt.figure(figsize=(10,6))
plt.bar(temp11-1,abs(Residual), facecolor='yellow', edgecolor='green',label='Residuals Lin reg')
plt.bar(temp11,abs(Residual2), facecolor='red', edgecolor='blue',label='Residuals Lin reg annengrad')
plt.legend(loc='upper right')
plt.title('Forsøk 1')
plt.xlabel('Temperatur [$^\circ$C]')
plt.ylabel('Residualer [mV]')
plt.savefig('Res1.pdf')

errorstig , errorkonstantledd = (np.sqrt(np.diag(cov)))
print("Usikkerhet alpha: %f Usikkerhet beta: %f" %(errorstig, errorkonstantledd))
print("Alpha: %f Beta: %f" %(coefs[0],coefs[1]))

plt.show()
# the histogram of the data step 2
plt.figure(figsize=(10,6))
plt.bar(temp22-1,abs(Residual12), facecolor='yellow', edgecolor='green',label='Residuals Lin reg')
plt.bar(temp22,abs(Residual22), facecolor='red', edgecolor='blue',label='Residuals Lin reg annengrad')
plt.legend(loc='upper right')
plt.title('Forsøk 2')
plt.xlabel('Temperatur [$^\circ$C]')
plt.ylabel('Residualer [mV]')
plt.savefig('Res2.pdf')

errorstig2 , errorkonstantledd2 = (np.sqrt(np.diag(cov2)))
print("Usikkerhet alpha: %f Usikkerhet beta: %f" %(errorstig2, errorkonstantledd2))
print("Alpha: %f Beta: %f" %(coefs2[0],coefs2[1]))
plt.show()

plt.figure(figsize=(10,6))
plt.bar(temp11,abs(Residual-Residual2), facecolor='red', edgecolor='blue',label='differanse residuals')
plt.legend(loc='upper right')
plt.title('Differanse i residualene forsøk 1')
plt.xlabel('Temperatur [$^\circ$C]')
plt.ylabel('Residualer [mV]')
plt.savefig('Restot.pdf')
plt.show()


plt.figure(figsize=(10,6))
plt.bar(temp22,abs(Residual12-Residual22), facecolor='red', edgecolor='blue',label='differanse residuals')
plt.legend(loc='upper right')
plt.title('Differanse i residualene forsøk 2')
plt.xlabel('Temperatur [$^\circ$C]')
plt.ylabel('Residualer [mV]')
plt.savefig('Restot2.pdf')
plt.show()

print(sum(abs(Residual)))
print(sum(abs(Residual2)))
print(sum(abs(Residual12)))
print(sum(abs(Residual22)))

# plt.figure(figsize=(10,6))
# plt.title('Sum av residualer')
# plt.ylabel('Sum')
# plt.bar(1,0.7431,0.10, facecolor='grey', edgecolor='yellow',label='Sum lin reg.')
# plt.bar(1.2,0.7315,0.10, facecolor='grey', edgecolor='green',label='Sum 2grad reg.')
# plt.savefig('sumres.pdf')
# plt.show()
mu, sigma  = np.mean(Residual), np.std(Residual)
normaldist = np.random.normal(mu, sigma, 1000)

mu2, sigma2  = np.mean(Residual2), np.std(Residual2)
normaldist2 = np.random.normal(mu2, sigma2, 1000)

x = np.arange(len(normaldist))
#
# plt.scatter(x,normaldist)
# plt.scatter(x, normaldist2)
#
# plt.show()
#
#
plt.hist(abs(normaldist2), 100, facecolor='yellow', edgecolor='green',label='Residualer 2grad reg')
plt.hist(-abs(normaldist), 100, facecolor='red', edgecolor='blue',label='Residuals Lin reg')
plt.show()
