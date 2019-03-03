
#%%
import numpy as np
import matplotlib.pyplot as plt

#%%
def periodogram(signal, f):
    N = len(signal)
    n = np.arange(0,N,1)
    e = np.exp(-1j*2*np.pi*f*n)
    S = (1/N)*np.abs(np.sum(signal*e))**2
    return S

def plot_per(N):
    real_spec = 1
    t = np.linspace(0, 10, N)
    f0 = 90
    gaussian_proc = np.random.normal(0,1,N)
    #gaussian_proc = np.random.normal(0,1,N) + np.sin(2*np.pi*f0*t) # add signal
    S_list = []
    m = np.arange(0, N/2, 1) # fourier frequency n/(N*dt), n = 0,1,2,3,4... N/2
    f_list = m/N # fourier frequency n/(N*dt), n = 0,1,2,3,4... N/2 Se kompendium s.32
    # f_list = np.arange(0, 100, 1)/N
    for f in f_list:
        S = S_list.append(periodogram(gaussian_proc, f))
    fig, ax = plt.subplots()

    ax.plot(f_list, S_list)
    ax.set_title('Frequency')
    ax.plot(f_list, np.full(len(S_list), real_spec), '-.')
    plt.tight_layout()
    plt.show()
    
N = 51
plot_per(N)



#%%
N = 101
plot_per(N)

#%%
N = 401
plot_per(N)