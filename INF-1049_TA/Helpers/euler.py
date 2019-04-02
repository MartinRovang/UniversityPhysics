
import numpy as np 
import matplotlib.pyplot as plt 




def ForwardEuler(X0, V0, m, dt, t):
    N = int(t/dt)
    x = np.zeros(N)
    v = np.zeros(N)
    a = np.zeros(N)
    t = np.arange(0, t, dt)
    x[0] = X0
    v[0] = V0
    for k in range(0, N-1):
        # Med demping (-0.1*np.sign(v[k]))
        a[k] = -(x[k]/m) -0.1*np.sign(v[k])
        v[k+1] = a[k]*dt + v[k]
        x[k+1] = v[k]*dt + x[k]
    return x, t


u, t = ForwardEuler(X0 = 5, V0 = 0, m = 1, dt = 0.001, t = 50)


plt.plot(t, u)
plt.show()
