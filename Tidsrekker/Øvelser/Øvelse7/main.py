
#%%
import numpy as np
import matplotlib.pyplot as plt

#%%
def periodogram(signal, f):
    N = len(signal)
    n = np.arange(0,N,1)
    e = np.exp(-1j*2*np.pi*f*n*(10/N))
    S = (1/N)*np.abs(np.sum(signal*e))**2
    return S

def plot_per(N, dB = False):
    """dB gir mindre differanse mellom frekvensene"""
    real_spec = 1
    dt = 10/(N-1)
    t = np.linspace(0, 10, N)
    f0 = 10
    gaussian_proc = np.random.normal(0,1,N)
    gaussian_proc = np.random.normal(0,1,N) + 2*np.sin(2*np.pi*f0*t) # add signal
    S_list = []
    print('Lowest resolution you can see, %.3f'%(1/(N*dt)))
    print('Highest frequency to observe is, %.3f'%(1/(2*dt)))
    m = np.arange(0, N, 1) # fourier frequency n/(N*dt), n = 0,1,2,3,4... N/2
    f_list = m/10 # fourier frequency n/(N*dt), n = 0,1,2,3,4... N/2 Se kompendium s.32
    # f_list = np.arange(0, 100, 1)/N
    for f in f_list:
        S_list.append(periodogram(gaussian_proc, f))
    fig, ax = plt.subplots(2,1)

    ax[0].plot(gaussian_proc)
    if dB == True:
        ax[1].plot(f_list, np.log10(S_list), color = 'black', linewidth = 2)
        ax[1].plot(f_list, np.log10(np.full(len(S_list), real_spec)), '-.')
        ax[1].set_title('Frequency')
    else:
        ax[1].plot(f_list, S_list, color = 'black', linewidth = 2)
        ax[1].plot(f_list, np.full(len(S_list), real_spec), '-.')
        ax[1].set_title('Frequency')
    #ax[1].set_ylim([0,10])
    plt.tight_layout()
    plt.show()
    
N = 51
plot_per(N, dB = True)



#%%
N = 101
plot_per(N)

#%%
N = 401
plot_per(N, dB = True)

#%%
N = 401
f0 = 10
t = np.linspace(0, 10, N)
#gaussian_proc = np.random.normal(0,1,N)
gaussian_proc = np.random.normal(0,1,N) + np.sin(2*np.pi*f0*t) # add signal
spectrum = np.fft.fft(gaussian_proc)
freq = np.fft.fftshift(np.fft.fftfreq(len(spectrum), 10/N))
spectrum = np.abs(spectrum)
dbspectrum = np.log10(np.abs(spectrum))
plt.plot(freq, spectrum)
plt.show()

#%%
N = 200
f0 = 7
t = np.linspace(0, 10, N)
dt = 10/N
print('Highest resolution: %.3f'%(1/(2*dt)))
#gaussian_proc = np.random.normal(0,1,N)
gaussian_proc = np.random.normal(0,1,N) + np.sin(2*np.pi*f0*t) # add signal
spectrum = np.fft.fft(gaussian_proc)
freq = np.fft.fftfreq(N, dt)
s_shift, f_shift = np.fft.fftshift([freq, spectrum])
spectrum = np.abs(spectrum)
#dbspectrum = np.log10(np.abs(spectrum))
plt.plot(f_shift, np.abs(s_shift))
plt.show()


#%%
