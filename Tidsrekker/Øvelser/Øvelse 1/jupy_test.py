

#%% Testing stat
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
import pandas as pd
import numpy as np


dat = sm.datasets.get_rdataset("Guerry", "HistData").data
# results = smf.ols('Lottery ~ Literacy + np.log(Pop1831)', data=dat).fit()
# print(results.summary())

dat = {'Penis':[5,10,20,10,20,20,10,10,1],'Size': [30,10,20,30,10,8,2,19,7]}

dat = pd.DataFrame(dat)

result = smf.ols('Penis ~ Size', data = dat).fit()
result.summary()
#dat

#%% testing random walk

import random
import numpy as np
random.seed(154)
w_noise = [random.gauss(0,1) for i in range(200)]
drift = 0.2

time = list(range(0,200))

# x = []
# for t in time:
#     x.append(drift*t+sum(w_noise[:t]))
    
time = np.arange(0,200,1)

x = drift*time + np.cumsum(w_noise)
plt.figure(figsize = (20,10))
plt.plot(time,x)
plt.show()




#%%
import random
import numpy as np
#random.seed(154)

# white noise
w_noise = [random.gauss(0,1) for i in range(100)]
# autoregression
x = np.zeros(100)
x[0] = w_noise[0]
x[1] = w_noise[1]
a1 = -0.8
for i in range(2,100):
    x[i] = -a1*x[i-1] + w_noise[i]


# 4 point running avarage
v = np.zeros(100)

for i in range(2,100):
    v[i] = (x[i] + x[i-1] + x[i-2] + x[i-3])/4

plt.figure(figsize = (20,10))
plt.plot(x+v)
#plt.plot(v,'--')
plt.show()
#%%
