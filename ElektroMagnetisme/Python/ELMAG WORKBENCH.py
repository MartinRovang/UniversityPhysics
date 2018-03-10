import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import epsilon_0

# qs = [(1,2,3),(1,4,3)]
# for x,y,z in qs:


class charge:
    def __init__(self, q,x,y):
        self.q = q
        self.x = x
        self.y = y


def E_Felt(X,Y,q,x,y):
    scales = 4*np.pi*epsilon_0
    return q * (X - x) / (scales*((X - x) ** 2 + (Y - y) ** 2)) ** (3/2), \
           q * (Y - y) / (scales*((X - x) ** 2 + (Y - y) ** 2)) ** (3/2)


def E_total(X, Y, charges):
    Ex, Ey = 0, 0
    for C in charges:
        E = E_Felt(X,Y,C.q,C.x,C.y)
        Ex = Ex + E[0]
        Ey = Ey + E[1]
    return Ex, Ey

charges = [charge(1, 1, 0), charge(1, -1, 0), charge(-1, 0, 1), charge(-1, 0, -1)]
charge = [charge(1, 0, 0)]


X, Y = np.meshgrid(np.linspace(-10,10,200), np.linspace(-10,10,200))
Ex, Ey = E_total(X,Y,charge)[0],E_total(X,Y,charge)[1]

plt.scatter(0,0 , color= 'red')
plt.streamplot(X,Y,Ex,Ey, density=[0.5, 1])
plt.show()


Ex,Ey = np.zeros(len(Ex)),np.zeros(len(Ey))
Ex,Ey = E_total(X,Y,charges)[0],E_total(X,Y,charges)[1]

plt.scatter([0,0],[1,-1] , color= 'blue')
plt.scatter([1,-1],[0,0] , color= 'red')
plt.streamplot(X,Y,Ex,Ey,density=[5, 1])


plt.show()
