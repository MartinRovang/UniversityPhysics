
#%%
import matplotlib.pyplot as plt 
import numpy as np
import random 
from statsmodels.tsa.stattools import acf

random.seed(1400)

sigma_sq = 1

# Signal a
w_noise = [random.gauss(0,sigma_sq) for i in range(200)]
t = np.arange(0,200,1)

s = 10*np.exp(-(t-100)/20)*np.cos(2*np.pi*t/4)
s[:100] = 0

x = s+w_noise


plt.figure(figsize = (20,10))
plt.plot(x)
plt.show()

# Signal b

s_b = 10*np.exp(-(t-100)/200)*np.cos(2*np.pi*t/4)
s_b[:100] = 0



x_b = s_b+w_noise


plt.figure(figsize = (20,10))
plt.plot(x_b)
plt.show()



#%%

# Meanfunctions E[x_t] => whitenoise = zero, cos is left

mean_a = s
mean_b = s_b

plt.figure(figsize = (20,10))
plt.plot(mean_a)
plt.title('Mean function a', fontsize = 30)
plt.show()
plt.figure(figsize = (20,10))
plt.plot(mean_b)
plt.title('Mean function b', fontsize = 30)
plt.show()

# COVARIANCE FUNCTIONS
def autocovariance(s, t, sigma_sq):
    if s == t:
        return sigma_sq
    else:
        return 0

s, t = (1,1)

a = [autocovariance(s,t, sigma_sq) for i in range(0,len(x))]


plt.figure(figsize = (20,10))
plt.stem(a)
plt.title('COV function a', fontsize = 30)
plt.show()
plt.figure(figsize = (20,10))
# plt.stem(cov_b)
# plt.title('COV function b', fontsize = 30)
# plt.show()


#%%

# Autocovariance function






#%% 

# 1.7
import random 
import numpy as np

w_noise = [random.gauss(0,1) for i in range(200)]

x = np.zeros(200)

for i in range(1,199):
    x[i] = w_noise[i-1] + 2*w_noise[i] + w_noise[i+1]


plt.plot(x)
plt.show()

#%% 1.7 # Autocorrelation function
import random 
import numpy as np

w_noise = [random.gauss(0, 1) for i in range(200)]

x = np.zeros(200)

for i in range(1, 199):
    x[i] = w_noise[i-1] + 2*w_noise[i] + w_noise[i+1]

y_arr = []
h_amount = 40
for h in range(h_amount):
    y = 0
    for i in range(0, h_amount):
        y += x[i]*x[i+h]
    y_arr.append(y)

a2 = acf(x)

y_arr = np.array(y_arr)
y_arr /=  max(y_arr)
plt.stem(y_arr)
plt.show()

plt.stem(a2)
plt.show()

#%%

###########################TEST######################################

import random 
import numpy as np
import pandas as pd 

data = np.array(pd.read_csv('ASETEK.csv')['Adj Close'][1:]).astype(float)

# Transform
stationary_transform_OSEBX = np.log(data[1:])-np.log(data[:-1])
print(np.mean(stationary_transform_OSEBX))

y = acf(data)
g = acf(stationary_transform_OSEBX)
plt.plot(stationary_transform_OSEBX)
plt.show()
plt.stem(g)
plt.show()


###########################TEST######################################
#%%
