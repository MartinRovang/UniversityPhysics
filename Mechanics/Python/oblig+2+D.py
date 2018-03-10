
# coding: utf-8

# In[2]:

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_context("talk")
#Massen vi gir den en vilkårlig verdi
m = 1
#Arrays å fylle for plot
tarray = []
Vtarray = []
Ttarray = []
Veffarray = []
#Startverdi r = b = 2
rarray = [2]
#tidssteg
dt = 0.001
#starttid
t = 0
b = 2
#startposisjon
r0 = 2  #r0 = b
#Startfart
V0 = (1/2)
#Etotal
E = 3 * V0
#Energiarray
el = []
i = 0
#Starthastighet
r01 = np.sqrt((7/4)*V0)
#Plotter r(t)
while (t < 10):
    #Test om rota blir negativ (altså negativ energi, dette er ikke mulig)
    Rtest = (2 / m) * (E - V0 * ((b / rarray[i]) + (rarray[i] / b)) - (V0 * m)/(2 * m * rarray[i]**2))
    if (Rtest >= 0):
        r01 = np.sqrt((2 / m) * (E - V0 * ((b / rarray[i]) + (rarray[i] / b)) - (V0 * m)/(2 * m * rarray[i]**2)))
    else:
        #bryter loopen hvis rota blir negativ
        break
    #Itererer posisjon
    r = r01 * dt + rarray[i]
    #Itererer V(t)
    Vt = V0 * ((b / rarray[i]) + (rarray[i] / b))
    #Itererer T(t) (tangentiell)
    Tt = (V0 * m)/(2 * m * rarray[i]**2)
    t = t + dt
    #Fyller opp arrays for plotting
    tarray.append(t)
    rarray.append(r)
    Vtarray.append(Vt)
    Ttarray.append(Tt)
    Veff = Vtarray[i] + Ttarray[i]
    Veffarray.append(Veff)
    i += 1
#Plott Etot
for i in range(0,len(tarray)):
    el.append(E)

print('Maks avstand:', rarray[-1])
    
    
plt.show()
#Plott alle
fig = plt.figure(figsize=(30,25))
plt.subplot(2,2,1)
plt.plot(tarray, rarray[:len(rarray)-1],label='r(t)',color='g')
plt.legend(loc='upper left')
plt.ylabel('r')
plt.xlabel('t')
plt.subplot(2,2,2)
plt.plot(tarray, Vtarray,label='V(t)',color='b')
plt.legend(loc='upper left')
plt.plot(tarray, Veffarray,label='Veff(t)',color='black')
plt.legend(loc='upper left')
plt.plot(tarray,Ttarray,label='VTangensiell(t)',color='green')
plt.legend(loc='upper left')
plt.plot(tarray,el,'--',label='Etot',color='red')
plt.legend(loc='upper left')
plt.ylabel('E')
plt.xlabel('t')
plt.show()


# In[ ]:



