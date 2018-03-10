
# coding: utf-8

# In[4]:

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#Vilkårlig masse
m = 1
#energi array
el = []
el0 = []
#startfart
V0 = 0.5
#Etot
E = (0.5)*m*(V0)**2 + 2*(0.5)
E0 = 1
#Potensiel energi funksjon og tar inn verdier
def V(b,v0):
    R = np.linspace(0.8,5,1000)
    V = v0*((b/R)+(R/b))
    return (R,V)
#gir to variabler en array hver gitt ved initialverdier
A,B = V(2,0.5)

#Loop for å fylle opp Etot array
i = 0
for i in range(0,len(A)):
    el.append(E)
for i in range(0,len(A)):
    el0.append(E0)

#plotter
fig = plt.figure(figsize=(15,10))
plt.plot(A,B,label='V(r)',color='blue')
plt.plot(A,el,'--', label='Etot',color='red')
plt.plot(A,el0,'--',label='Etot0',color='red')
plt.ylabel('Potensial')
plt.xlabel('r')
plt.annotate('r min, E', xy=(1.22, 1.12),xytext=(2, 1.2),
            arrowprops=dict(facecolor='black', shrink=0.05),)
plt.annotate('E', xy=(5, 1.12),xytext=(5, 1.18),
            arrowprops=dict(facecolor='black', shrink=0.05),)
plt.annotate('r maks', xy=(3.3, 1.12),xytext=(3, 1.3),
            arrowprops=dict(facecolor='black', shrink=0.05),)
plt.annotate('Likevektspunkt', xy=(2,1),xytext=(2, 1.1),
            arrowprops=dict(facecolor='black', shrink=0.05),)
plt.annotate('E0', xy=(5, 1),xytext=(5,1.05),
            arrowprops=dict(facecolor='black', shrink=0.05),)

plt.legend(loc='upper left')
plt.show()


# In[ ]:



