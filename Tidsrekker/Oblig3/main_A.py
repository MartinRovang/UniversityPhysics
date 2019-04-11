
from statsmodels.tsa.stattools import acf, pacf, ccf
from statsmodels.tsa.arima_process import arma2ma, arma2ar
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import statsmodels as sm

# Load data
rec = pd.read_csv('data/rec.txt', delimiter='\t')
rec_df = pd.DataFrame(rec)
time = np.copy(rec_df['year'])
X = np.copy(rec_df['recruitment'])


def periodogram(x, dt = 1):
    """Regular periodogram"""
    #x = np.pad(x, (0,200), 'constant')
    N = len(x)
    spectrum = np.abs(np.fft.fftshift(np.fft.fft(x))**2)
    spectrum *= dt/ N
    freq = np.fft.fftshift(np.fft.fftfreq(N, dt))

    return freq[int(N/2):], spectrum[int(N/2):]


def w_periodogram(x, dt = 1):
    """Windowed periodogram"""
    #x = np.pad(x, (0,300), 'constant')
    N = len(x)
    n = np.arange(0,N,1)
    # Hann window
    window = (1/2)*(1 - np.cos(2*np.pi*n/(N-1)))
    U = (1/N)*np.sum(window**2)
    spectrum = np.abs(np.fft.fftshift(np.fft.fft(window*x)))**2
    spectrum *= (dt/(N*U))
    freq = np.fft.fftshift(np.fft.fftfreq(N, dt))

    return freq[int(N/2):], spectrum[int(N/2):]

# a)Plott tidsrekka, og vis at denne tidsrekka har en sesongvariasjon (selv om den ikke erveldig synlig). Du bestemmer metode selv.

# Find periodogram
freq, periodogram_X = w_periodogram(X)


# # Plot data
# fig, ax = plt.subplots(2,1)
# ax[0].plot(time, X, color = 'black')
# ax[0].set_title('Recruitment series')
# ax[0].set_xlabel('Year')
# ax[0].set_ylabel('Recruitment')
# ax[1].plot(freq[2:]*12, periodogram_X[2:], color = 'black')
# ax[1].set_title('Periodogram(hann windowed)')
# ax[1].set_xlabel('Frequency $\Delta f =$ year')
# ax[1].set_ylabel('Power')
# ax[1].set_xticks([x for x in np.arange(0, 6.5, 1/2)])
# plt.show()


# b)Trekk fra midlere sesongvariasjoner for  ̊a gjøre tidsrekka stasjonær, og plott dataene.Den resulterende tidsrekka skal brukes i alle de neste oppgavene.

def remove_season(x):
    C = np.zeros(12)
    for m in range(0,12):
        C[m] = np.mean(x[m::12])

    # repeat C to create a periodic signal of equal length or longer than the dataset
    repC = np.tile(C, int(np.ceil(len(x)/12)))
    # compute residual (by subtracting periodic signal)
    X = x - repC[:len(x)]
    return X


X_remseason = remove_season(X)

# c)Plott estimert ACF og PACF.

wt_line = 2*np.tile(1/np.sqrt(len(X_remseason)), 41)

fig, ax = plt.subplots(3,1)
ax[0].plot(X_remseason)
ax[1].stem(acf(X_remseason))
ax[1].plot(wt_line, '--', color = 'red'); ax[1].plot(-wt_line, '--', color = 'red')
ax[2].stem(pacf(X_remseason))
ax[2].plot(wt_line, '--', color = 'red'); ax[2].plot(-wt_line, '--', color = 'red')
plt.show()


# d)Basert p ̊a plottene i forrige deloppgave, hvilken orden p og q vil du bruke i en ARMA-modell for disse dataene?


model = sm.tsa.arima_model.ARIMA(X_remseason, order=(2, 0, 0))
model_fit = model.fit()
#print(model_fit.summary())




# Oppgave 2


# a)Plott estimert ACF og PACF for residualene.
res = model_fit.resid

# fig, ax = plt.subplots(3,1)
# ax[0].plot(res)
# ax[1].stem(acf(res))
# ax[1].plot(wt_line, '--', color = 'red'); ax[1].plot(-wt_line, '--', color = 'red')
# ax[2].stem(pacf(res))
# ax[2].plot(wt_line, '--', color = 'red'); ax[2].plot(-wt_line, '--', color = 'red')
# plt.show()

# Siden alle verdiene ligger under standarnormalfordelt  


# Oppgave 3


# a) Basert p ̊a valgt modell: Lever plot av 1,2,...M-stegs BLP der du velgerM≥10.Som en sjekk p ̊a at man har f ̊att det til: m-stegs BLP g ̊ar mot forventningμn ̊arm→∞.
# b) Plott 95% konfidensintervall for prediksjonen.

year = 5
M = 12*year # 12*2 months (2 years)
forecast, stderr, conf_int = model_fit.forecast(steps = M)
# gir ut forecast, std, (1-alpha)% konfidensintervall. Default: 95% konfidensintervall


sliced_time = time[100:]
sliced_X = X_remseason[100:]
time_forecast = np.linspace(sliced_time[-1], sliced_time[-1] + M/12, M)


fig, ax = plt.subplots(figsize = [12,6])
ax.plot(sliced_time, sliced_X, color = 'black', label = 'Recruitment series')
ax.plot(time_forecast, forecast, '-o', mfc='none', color = 'red', linewidth = '1', label = 'Prediction' )
ax.fill_between(time_forecast, conf_int[:,0], conf_int[:,1], facecolor = (0, 0, 1, 0.2), label = '95% CI')
ax.set_xticks([x for x in np.arange(sliced_time[0], sliced_time[-1]+ M/12, 3)])
plt.legend(loc = 'best')
plt.show()



