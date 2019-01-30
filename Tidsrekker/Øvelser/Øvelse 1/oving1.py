

#%% Task 1
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import datetime as dt
import matplotlib.dates as mdates

df = pd.DataFrame(pd.read_csv('osebx.csv'))
y = np.array(df['Last'])[::-1]

df = pd.DataFrame(pd.read_csv('osebx.csv'))
dates = df.iloc[:,0]
Last = df.iloc[:,1]
datoliste = dates.values
 
for k in range(len(datoliste)):
    year = datoliste[k][6:8]
    if 30<= int(year) <= 99:
        year = '19' + year
    else:
        year = '20' + year
    datoliste[k] = datoliste[k][0:6] + year

x_date = [dt.datetime.strptime(d,'%d.%m.%Y').date() for d in datoliste] # convert dates to datetime.date format#


fig, ax = plt.subplots(figsize=(20,7))
ax.plot(x_date, Last.values)
fig.autofmt_xdate()
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax.set_xlabel('date',fontsize = 26)
ax.set_ylabel('OSEBX',fontsize = 26)
ax.grid()
ax.tick_params(axis='both',labelsize=14)
ax.set_title('Oslo Benchmark index',fontsize = 26)
ax.set_xlim(min(x_date),max(x_date))



#%% Task 2.a

import random
import matplotlib.pyplot as plt
w = [random.gauss(0, 1) for i in range(500)]
plt.plot(w)
plt.show()




#%% TASK 2.b

#This model is a random walk with zero drift

import numpy as np
x = np.cumsum(w)
plt.plot(x)
plt.show()

# The expectation of random walk with zero drift is zero


#%% Task 2.c

# This stocastic process is called AR(auto regression model)


#%% Task 2.d

import random
import matplotlib.pyplot as plt
w = [random.gauss(0.2, 1) for i in range(500)]
plt.plot(w)
plt.show()

# Now the expectation is 0.2


#%% Task 4

import numpy as np
import random
import matplotlib.pyplot as plt
import pandas as pd

w = [random.gauss(0.2, 1) for i in range(200)]

x = np.cumsum(w)
plt.plot(x)
plt.title('Random Walk',fontsize = 30)
plt.show()

df = pd.DataFrame(pd.read_csv('osebx.csv'))
y = np.array(df['Last'])[-200:]


plt.plot(y)
plt.title('OSEBX',fontsize = 30)
plt.show()


# Transform
stationary_transform_OSEBX = np.log(y[1:])-np.log(y[:-1])
 

fig, ax = plt.subplots()
ax.plot(x_date[-199:], stationary_transform_OSEBX)
fig.autofmt_xdate()
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d-%Y'))
# ax.set_xlabel('date',fontsize = 26)
#ax.set_ylabel('OSEBX',fontsize = 26)
ax.grid()
ax.tick_params(axis='both', labelsize=14)
ax.set_title('Increments OSEBX',fontsize = 26)
#ax.set_xlim(min(x_date), max(x_date))
plt.show()

# Plot difference logged OSEBX data
# ax.plot(stationary_transform_OSEBX)
# ax.title('Increments',fontsize = 30)
# plt.show()

# Plot white noise
plt.plot(w)
plt.title('WhiteNoise',fontsize = 30)
plt.show()

#%% TASK 5

import matplotlib.pyplot as plt
import random
import numpy as np 
random.seed(100)

# 5.a
w_noise = [random.gauss(0,1) for i in range(0,100)]
x = np.zeros(100)
for i in range(3, 100):
    x[i] = -0.9*x[i-2] + w_noise[i]
# Moving avarage
v = [((x[i]+x[i-1] + x[i-2] + x[i-3])/4) for i in range(2, 100)]
plt.figure(figsize = (20,10))
plt.plot(x)
plt.plot(v, '--', label = 'MA')
plt.title('5.A',fontsize = 30)
plt.legend(loc = 'best', prop={'size': 50})
plt.xlim(20,100)
plt.show()


#%%
#######################
#5.b
random.seed(100)
t = np.linspace(0,100,100)
x = np.cos(2*np.pi*t/4)

# Moving avarage
v = np.array([((x[i]+x[i-1] + x[i-2] + x[i - 3])/4) for i in range(2, 100)])
plt.figure(figsize = (20,10))
plt.plot(x)
plt.plot(v, '--', label = 'MA')
plt.title('5.B',fontsize = 30)
plt.legend(loc = 'best', prop={'size': 50})
#plt.xlim(50,100)
plt.show()

#%%

# 5.c
random.seed(100)
t = np.linspace(0,100,100)
x = np.cos(2*np.pi*t/4)+w_noise
# Moving avarage
v = np.array([((x[i]+x[i-1] + x[i-2] + x[i-3])/4) for i in range(2, 100)])
plt.figure(figsize = (20,10))
plt.plot(x)
plt.plot(v, '--', label = 'MA')
plt.title('5.C',fontsize = 30)
plt.legend(loc = 'best', prop={'size': 50})
#plt.xlim(50,100)
plt.show()


#%%
