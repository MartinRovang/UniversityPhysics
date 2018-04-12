import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import epsilon_0
import sympy
from matplotlib.patches import Circle
from matplotlib.mlab import griddata


charge_colors = {True: '#aa0000', False: '#0000aa'}

#Necessarys
X, Y = np.meshgrid(np.linspace(-2,2,200), np.linspace(-2,2,200))



class charge:
    def __init__(self, q,x,y):
        self.q = q
        self.x = x
        self.y = y

def E_Felt(X,Y,q,x,y):
    hypotinus = (np.hypot(X-x,Y-y))**3
    hypotinus[hypotinus<0.0001]=0.0001
    r = hypotinus
    scales = 4*np.pi*epsilon_0
    return q * (X - x) / (r*scales), \
           q * (Y - y) / (r*scales)


def V_Felt(X,Y,q,x,y):
    scales = 4*np.pi*epsilon_0
    hypotinus = (np.hypot(X-x,Y-y))**2
    hypotinus[hypotinus<0.01]=0.01
    r = hypotinus
    return q / (r*scales)

def V_total(X, Y, charges):
    Vit = 0
    for C in charges:
        V = V_Felt(X,Y,C.q,C.x,C.y)
        Vit = Vit + V
    return Vit
#-------------------------------------------------------------
def E_Felt1(X,Y,q,x,y):
    hypotinus = (np.hypot(X-x,Y-y))**3
    hypotinus[hypotinus<0.0001]=0.0001
    r = hypotinus
    scales = 4*np.pi*epsilon_0
    return q /(r*scales)

def E_total1(X, Y, charges):
    Vit = 0
    for C in charges:
        V = E_Felt1(X,Y,C.q,C.x,C.y)
        Vit = Vit + V
    return Vit
#-------------------------------------------------------------


def E_total(X, Y, charges):
    Ex, Ey = 0, 0
    for C in charges:
        E = E_Felt(X,Y,C.q,C.x,C.y)
        Ex = Ex + E[0]
        Ey = Ey + E[1]
    return Ex, Ey


def pol2cart(r, phi):
    x = r * np.cos(phi)
    y = r * np.sin(phi)
    return(x, y)

fig = plt.figure()
ax = fig.add_subplot(111)

def circleq(r,N,Q):
    print("Configuring Circle")
    count = 0
    phi = 0
    i = 0
    x = np.array([])
    y = np.array([])
    chargess = np.array([])
    while (count < N):
        split = 2*np.pi/N
        x = np.append(x,pol2cart(r,phi)[0])
        y = np.append(y,pol2cart(r,phi)[1])
        count += 1
        phi += split
    while (i < N):
        chargess = np.append(chargess,charge(Q/N,x[i],y[i]))
        i += 1
    print("Iteration finished")
    return chargess



def lines(N,Q,h):
    print("Configuring Lines")
    count = 0
    i2 = 0
    N1 = 0
    i = 0
    sign = 1
    x = np.array([])
    y = np.array([])
    chargess = np.array([])
    while (count < N):
        x = np.append(x,-N/4*0.1 +count*0.1)
        y = np.append(y,-h)
        N1 += 1
        while (i2 < N1):
            x = np.append(x,-N/4*0.1 +count*0.1)
            y = np.append(y,h)
            i2 += 1
        count += 1
    while (i < N):
        chargess = np.append(chargess,charge((-sign)*Q/N,x[i],y[i]))
        sign = sign*(-1)
        i += 1
    print("Iteration finished")
    return chargess

linecharges = lines(30,1,0.1)
chargez = circleq(1,100,1)

xcharge = np.array([])
ycharge = np.array([])
for C in chargez:
    xcharge  = np.append(xcharge,C.x)
    ycharge = np.append(ycharge,C.y)

xline = np.array([])
yline = np.array([])
for C in linecharges:
    xline  = np.append(xline,C.x)
    yline = np.append(yline,C.y)


#Circle field
# for i in range(len(xcharge)):
#     ax.add_artist(Circle((xcharge[i],ycharge[i]),0.005,color=charge_colors[True]))
# Ex,Ey = E_total(X,Y,chargez)[0],E_total(X,Y,chargez)[1]
# Vtot = V_total(X,Y,chargez)
# plt.contourf(X,Y,Vtot,200, cmap = plt.cm.jet)
# cbar = plt.colorbar(label = 'Potensial V')
# plt.contour(X,Y,Vtot,1)
# plt.streamplot(X,Y,Ex,Ey,density=[2, 1],linewidth=0.2,color='black')
# plt.show()


#Line field
# for i in range(len(xline)):
#     ax.add_artist(Circle((xline[i],yline[i]),0.03,color=charge_colors[yline[i]>0]))
Xl, Yl = np.meshgrid(np.linspace(-2,2,70), np.linspace(-2,2,70))
Exl,Eyl = E_total(Xl,Yl,linecharges)[0],E_total(Xl,Yl,linecharges)[1]
Vtotal = V_total(Xl,Yl,linecharges)
plt.contourf(Xl,Yl,Vtotal,200, cmap = plt.cm.jet)
cbar = plt.colorbar(label = 'Potensial V')
plt.contour(Xl,Yl,Vtotal,1)
plt.streamplot(Xl,Yl,Exl,Eyl,density=[2, 1],linewidth=0.2,color='black')

plt.show()
