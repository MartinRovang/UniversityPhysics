
#%%

import numpy as np
import matplotlib.pyplot as plt


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


#%%

def plot_fft(N, M):
    real_spec = 1
    gaussian_proc = np.random.normal(0, 1, N)
    fft = np.fft.fft(gaussian_proc, n = M)
    freq = np.fft.fftfreq(len(fft))
    fig, ax = plt.subplots()

    ax.stem(freq, np.abs(fft))
    ax.set_title('Frequency')
    ax.plot(freq, np.full(len(fft), real_spec), '-.')
    #ax.set_xlim([0,0.5])
    plt.tight_layout()
    plt.show()


plot_fft(51, 1000)


#%%

plot_fft(51, 512)



#%% 

import numpy as np
import matplotlib.pyplot as plt

A = 1
dt = 0.2
n = np.arange(0,40,dt)
N = len(n)
df = 1/(N*dt)
f_fourier = k*df # k = 0,1,2,3,4 N-1
f0 = 0.6 + 1/2*df


theta = np.random.uniform(low=0, high=2*pi, size=1)
Xt = A*np.sin(2*pi*f0*n + theta)
#Xt = np.random.normal(0, 1, N)
#plt.plot(Xt)

# beregn periodogrammet
S_per = dt/N*abs(np.fft.fft(Xt))**2
freq = np.fft.fftfreq(N, d=dt)
S_shift,f_shift = np.fft.fftshift([freq,S_per])

fig, ax = plt.subplots(figsize = [10,7])
ax.stem(f_shift, S_shift)
ax.grid()
ax.set_xlim(-1/(2*dt),1/(2*dt))
ax.tick_params(axis='both',labelsize=18)
plt.show()


#%%

import time                                                

def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print ('%r (%r, %r) %2.2f sec' % \
              (method.__name__, args, kw, te-ts))
        return result

    return timed


@timeit
def f2(a):
    time.sleep(2)
    print ('f2',a)

f2(42)