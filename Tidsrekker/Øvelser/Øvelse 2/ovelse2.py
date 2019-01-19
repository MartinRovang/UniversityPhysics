
#%%
import matplotlib.pyplot as plt 
import numpy as np
import random 
random.seed(1400)

# Signal a
w_noise = [random.gauss(0,1) for i in range(200)]
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
cov_a = s*s + 1
cov_b = s_b*s_b + 1

plt.figure(figsize = (20,10))
plt.stem(cov_a)
plt.title('COV function a', fontsize = 30)
plt.show()
plt.figure(figsize = (20,10))
plt.stem(cov_b)
plt.title('COV function b', fontsize = 30)
plt.show()


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
h_amount = 50
for h in range(h_amount):
    y = 0
    for i in range(0, h_amount):
        y += x[i]*x[i+h]
    y_arr.append(y)


y_arr = np.array(y_arr)
y_arr /=  max(y_arr)
plt.stem(y_arr)
plt.show()

#%%

###########################TEST######################################

# import random 
# import numpy as np
# import pandas as pd 

# data = pd.read_csv('ASETEK.csv')['Adj Close']

# # stationary_transform_OSEBX = np.log(y[1:])-np.log(y[:-1])
# y = np.zeros(len(data))

# for i in range(0, len(data)):
#     try:
#         y[i] = np.log((data[i]/data[i - 1]))
#     except:
#         print('excepted')


# plt.plot(y)
# plt.show()

# y_arr = []
# for h in range(30):
#     g = 0
#     for i in range(0, len(y)-30):
#         g += y[i]*y[i+h]
#     y_arr.append(g)


# y_arr = np.array(y_arr)
# y_arr /=  max(y_arr)
# plt.stem(y_arr)
# plt.show()


###########################TEST######################################
#%%
