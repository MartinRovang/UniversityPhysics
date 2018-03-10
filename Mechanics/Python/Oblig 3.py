import numpy as np
import matplotlib.pyplot as plt


import numpy as np
import matplotlib.pyplot as plt

#Posisjon,hastighet og tids array.
yarray = [0]
dyarray = [0]
tarray = []
equilibriumarray = []
dq = 20
#Konstanter
c = 16
d = 20
dt = 0.001
k = 135
t = 0
m = 70
g = 9.81
#Iterator
i = 0

#Loop for bevegelsen
while t < 40:
    #Bevegelse når y > d, bruker eulers metode cromer metode v[i + 1]dt
    if yarray[i] > d:
        ddy = g  + (-1/m)*(c*dyarray[i]+k*(yarray[i]-d))
        dy = ddy *dt + dyarray[i]
        y = dy *dt + yarray[i]
    #Bevegelse når y <= d
    else:
        ddy = g
        dy = ddy *dt + dyarray[i]
        y = dy *dt + yarray[i]
    #Legger inn verdiene i array
    yarray.append(y)
    equilibriumarray.append(dq)
    dyarray.append(dy)
    t += dt
    tarray.append(t)
    i += 1

#lager array for sluttposisjon
lastposarray = np.zeros(len(yarray[:-1]))
lp = yarray[-1]
lastposarray1 = lastposarray +  lp

#Plotter verdier
fig = plt.figure(figsize=(10,5))
plt.subplot(2,2,1)
plt.plot(tarray,yarray[:-1],label='y(t)')
plt.legend(loc='lower right')
plt.plot(tarray,equilibriumarray,"--",label='Lengden på strikken')
plt.legend(loc='lower right')
plt.plot(tarray,lastposarray1,"--",label='Sluttposisjon')
plt.legend(loc='lower right')
plt.ylabel('Høyde')
plt.xlabel('Tid')
plt.subplot(2,2,2)
plt.plot(tarray,dyarray[:-1],label='v(t)')
plt.legend(loc='lower right')
plt.ylabel('Hastighet')
plt.xlabel('Tid')

plt.show()
