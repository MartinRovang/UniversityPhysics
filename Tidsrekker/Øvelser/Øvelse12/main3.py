from statsmodels.tsa.stattools import acf, pacf, ccf
from statsmodels.tsa.arima_process import arma2ma, arma2ar
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import statsmodels.api as sm

# Load data
data = pd.read_csv('rec.txt', delimiter='\t')
df = pd.DataFrame(data)
# find normal distribution CI
normal_std = np.tile(2/np.sqrt(len(df['recruitment'])), 40)


# Plot data, acf and pacf with the normal distribution CI
fig, ax = plt.subplots(3,1)
ax[0].plot(df['year'], df['recruitment'])
ax[1].stem(acf(df['recruitment']))
ax[1].plot(normal_std, '--', color = 'red')
ax[1].plot(-normal_std, '--', color = 'red')
ax[2].stem(pacf(df['recruitment']))
ax[2].plot(normal_std, '--', color = 'red')
ax[2].plot(-normal_std, '--', color = 'red')
plt.show()




# Perform linear regression, assuming AR(2)
Z1 = np.copy(df['recruitment'])
Z2 = np.roll(np.copy(df['recruitment']), 1)
Y = np.roll(np.copy(df['recruitment']), 2)
X = np.column_stack((Z1, Z2))
X = sm.add_constant(X) # NB: må spesifiseres dersom vi skal ha konstantledd i modellen.
model = sm.OLS(Y,X)
results = model.fit()
beta0, beta2, beta1 = results.params

# Estimate model xxx -> linear regression
xxx = np.zeros(len(df['recruitment']))
xx = np.copy(df['recruitment'])
xxx[0], xxx[1] = xx[0], xx[1]
for i in range(2, len(df['recruitment'])):
    xxx[i] = beta0 + beta1*xx[i-1] + beta2*xx[i-2]

# Find residuals and the standarddeviation for modeling noise
residuals = xx - xxx
std = np.std(residuals)

# Make regression
x = np.zeros(len(df['recruitment']))
x[0], x[1] = xx[0], xx[1]
for i in range(2, len(df['recruitment'])):
    x[i] = beta0 + beta1*x[i-1] + beta2*x[i-2] + np.random.normal(0, std)


# QQ plot
fig = sm.qqplot(residuals, fit=True, line='45')
plt.show()

# ACF, PACF of residuals
normal_std = np.tile(2/np.sqrt(len(residuals)), 40)
fig, ax = plt.subplots(2,1)
ax[0].stem(acf(residuals))
ax[1].stem(pacf(residuals))
ax[0].plot(normal_std, '--', color = 'red')
ax[0].plot(-normal_std, '--', color = 'red')
ax[1].plot(normal_std, '--', color = 'red')
ax[1].plot(-normal_std, '--', color = 'red')
plt.show()

# Plot real and estimated data
fig, ax = plt.subplots(2,1)
ax[0].plot(df['year'] ,df['recruitment'])
ax[1].plot(df['year'], x)
plt.show()

