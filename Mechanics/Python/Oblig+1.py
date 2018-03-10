
# coding: utf-8

# In[1]:

import numpy as np
import matplotlib.pyplot as plt
#Konstante verdier
k = 16
m = 1
dt = 0.01
dt2 = 0.001
w2 = k/m
w = np.sqrt(k/m)
mu = 1/16
g = 9.81
#Startbetingelser
x = 1
q = (3*np.pi/2)
#Starthastighet
x1 = 0
#Starttid
t = 0
#Lager en tidsarray og posisjonsarray for å plotte de
tarray = []
xarray = []
tarray2 = []
xarray2 = []
tarray3 = []
xarray3 = []
#loop som løser diff. lign. numerisk ved å iterere opp verdiene per tidssteg
while (t < 10):
    #Posisjonen
    #Hastighet
    #Akselerasjonen
    x2 = -x*w2
    x = x + x1*dt
    x1 = x1 + x2*dt
    #Tid
    t = t + dt
    #Legger til i array for hver iterering
    tarray.append(t)
    xarray.append(x)
    
#Loop for løsning med annet dt
x = 1
t = 0
x1 = 0
while (t < 10):
    #Akselerasjonen
    x2 = -x*w2
    #Hastighet
    x = x + x1*dt2
    x1 = x1 + x2*dt2
    #Posisjonen
    #Tid
    t = t + dt2
    #Legger til i array for hver iterering
    tarray2.append(t)
    xarray2.append(x)
    
#Loop for løsning med friksjon
x = 1
t = 0
x1 = 0 #(hvis jeg har null hastighet så deler jeg på null i enhetsvektoren får jeg error)
while (t < 10):
    #Akselerasjonen med friksjon
    x2 = -x*w2 - mu*g*np.sign(x1)
    #Posisjonen
    x = x + x1*dt2
    #Hastighet
    x1 = x1 + x2*dt2
    #Tid
    t = t + dt2
    #Legger til i array for hver iterering
    tarray3.append(t)
    xarray3.append(x)


    
    
#Eksakt plot
A = 1
te = np.linspace(0,10,1000)
x = A*np.cos(w*te )

#Plott alle
fig = plt.figure(figsize=(25,15))
plt.subplot(2,2,1)
plt.plot(tarray,xarray, label='dt = 0.1',color='g')
plt.legend(loc='upper left')
plt.subplot(2,2,2)
plt.plot(tarray2,xarray2, label='dt = 0.001',color='b')
plt.legend(loc='upper left')
plt.subplot(2,2,3)
plt.plot(tarray3,xarray3, label='Friksjon',color='black')
plt.legend(loc='upper left')
plt.subplot(2,2,4)
plt.plot(te,x, label='Eksakt',color='red')
plt.legend(loc='upper left')
plt.show()


# In[ ]:



