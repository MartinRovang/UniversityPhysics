
#%%

# 2b
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf
import pandas as pd 
import datetime as dt
import matplotlib.dates as mdates


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
plt.show()



P = np.array(Last.values)
Y = np.log(P)
r = Y[1:] - Y[:-1]
fig, ax = plt.subplots(figsize=(20,7))
ax.plot(x_date[:-1],r)
ax.xaxis.set_major_locator(mdates.YearLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
fig.autofmt_xdate()
ax.set_xlim(min(x_date),max(x_date))
ax.set_xlabel('date',fontsize = 26)
ax.set_ylabel('OSEBX',fontsize = 26)
ax.grid()
ax.tick_params(axis='both',labelsize=14)
ax.set_title('Oslo Benchmark index',fontsize = 26)
plt.show()


#%%

# 2c

plt.stem(acf(r))
plt.show()

# looks like white noise

#%%

# 2d
plt.stem(acf(np.abs(r)))
plt.show()


# now the the points are correlated atleast up to 40 lags

#%%
# 2e

white_noise = np.random.normal(0,1, len(r))

plt.hist(white_noise, density= True, bins = 100)
plt.show()

plt.hist(r, density= True, bins = 100)
plt.show()


from statsmodels.graphics.gofplots import qqplot

qqplot(r)
plt.show()

# Not completely normal

#%% 
# 2f
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf
import pandas as pd 
import datetime as dt
import matplotlib.dates as mdates


df = pd.DataFrame(pd.read_csv('DJI.csv'))

data = df['Adj Close'][700:]


plt.plot(data)
plt.show()

P = np.array(data)
Y = np.log(P)
r = Y[1:] - Y[:-1]

plt.plot(r)
plt.show()



plt.stem(acf(r))
plt.show()

plt.stem(acf(np.abs(r)))
plt.show()


plt.hist(r, density= True, bins = 100)
plt.show()


from statsmodels.graphics.gofplots import qqplot

qqplot(r)
plt.show()


# Dette ser veldig likt ut som OSEBX


#%%
#2a
import numpy as np
from statsmodels.tsa.stattools import acf,acovf
n = 500

w = np.random.normal(0,1,n)

x = np.zeros(n)

for i in range(1,n):
    x[i] = (1/2)*(w[i-1] + w[i])

plt.plot(x)
plt.show()

plt.stem(acovf(x))
plt.show()

plt.stem(acf(x))
plt.show()


# The more n, the closer to theoretical values
#%%
np.random.seed(100)

n = 1000
w = np.random.normal(0,1,n)
x = np.cumsum(w)

plt.plot(x)
plt.show()

plt.stem(acovf(x))
plt.show()

plt.stem(acf(x))
plt.show()

#%%
