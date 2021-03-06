
#%%
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import datetime as dt
import random
import os
import statsmodels.api as sm

filedir = ''
filename = 'oslotemp_monthly.txt'

file = os.path.join(filedir, filename)

# load data
datatable = pd.read_table(file,sep='\s+',skiprows=14, skipfooter=20,engine='python',converters={'Month': lambda x: str(x)})
# Months are converted to strings to keep the leading 0's.
month=datatable.iloc[:,1].values
data=datatable.iloc[:,2].values

startyear = int(month[0][3:7])
endyear = int(month[-1][3:7])
time1 = startyear + int(month[0][0:2])/12
time2 = endyear + int(month[-1][0:2])/12
timearray = np.arange(time1,time2,1/12)

fig, ax = plt.subplots(figsize = [9,5])
#plt.plot(timearray,data,linewidth=2,color = "black")
plt.plot(timearray,data,linewidth=2,color = "white") # siste 10 år
ax.set_xlabel('Year',fontsize = 18)
ax.set_title('Monthly temperature Oslo',fontsize = 18)
ax.grid()
#ax.set_xlim(min(timearray),max(timearray))
#ax.set_ylim(-12,20)
ax.tick_params(axis='both',labelsize=22)
plt.show()

datareal = np.copy(data)

Y = data
X = timearray - timearray[0]

X = sm.add_constant(X)
model1 = sm.OLS(Y, X)
results1 = model1.fit()
results1.params
print(results1.summary())

# plot trend together with data
fig, ax = plt.subplots(figsize = [20,10])
ax.plot(timearray,data);
ax.plot(timearray,results1.fittedvalues, label = 'Linear fit')
ax.set_xlabel('Year',fontsize = 18)
ax.set_title('Monthly mean temperature Oslo',fontsize = 18)
ax.grid()
ax.tick_params(axis='both',labelsize=18)
ax.legend(loc = 'best')
plt.show()


plt.plot(remove_climate1)
plt.show()


from statsmodels.graphics.gofplots import qqplot
qqplot(remove_climate1)
plt.show()



# Residualene for lineær regresjon ser ut til å være normalfordelt støy
# Dette kan bety at modellen ikke gjør økende "feil" over tid.
#%%


#Som i Eq. (2.19-2.21) i boka:
# prediktorer:
Y = data
Z1 = timearray - timearray[0]  #Sånn at x-aksen start på 0 og oppover.
Z2 = Z1**2

X = np.column_stack((Z1, Z2))
X = sm.add_constant(X)

model2 = sm.OLS(Y,X)
results2 = model2.fit()
results2.params
print(results2.summary())

# plot trend together with data
fig, ax = plt.subplots(figsize = [20,10])
ax.plot(timearray, data)
ax.plot(timearray,results2.fittedvalues, label = 'Linear fit')
ax.set_xlabel('Year',fontsize = 18)
ax.set_title('Monthly mean temperature Oslo',fontsize = 18)
ax.grid()
ax.tick_params(axis='both', labelsize=18)
ax.legend(loc = 'best')
plt.show()
plt.plot(results2.fittedvalues)
plt.show()

#%%
def climatology(x,months,returnresidual=False,period='Normal'):
    # inputs: 
    # x: the dataset
    # months: strings on format mm.yyyy, e.g. 01.2019
    
    startyear = int(months[0][3:7])
    startmonth = int(months[0][0:2]) # 4 = april
    endyear = int(months[-1][3:7])
    endmonth = int(months[-1][0:2])

    # pad with NaN in beginning or end, such that element 0 corresponds to a january month,
    # and last element (-1) to a december month
    # This is just to make indexation easier
    n_pad_start = startmonth - 1 #number of months missing for time to start in january
    n_pad_end = 12 - endmonth #number of months missing for time to end in december
    x_pad = np.concatenate((np.full(n_pad_start, np.nan), x, np.full(n_pad_end, np.nan)))
    
    # compute climatology: mean january temp, mean february temp, etc.
    C = np.zeros(12)
    if period == 'All': # all values
        for m in range(0,12):
            C[m] = np.nanmean(x_pad[m::12])  # take out every 12th element, then compute mean (ignoring nan values)
    elif period == 'Normal':
        normalperiod_start = 1961; normalperiod_end = 1990
        startindex = (normalperiod_start - startyear - 1)*12 # starts in january
        endindex = (normalperiod_end - startyear)*12 - 1 # ends in december
        x_normalperiod = x_pad[startindex:endindex+1]
        for m in range(0,12):
            C[m] = np.nanmean(x_normalperiod[m::12]) # take out every 12th element, then compute mean
    
    if returnresidual == False:
        return C
    elif returnresidual == True:
        # repeat climatology to create a periodic signal of equal length as the dataset
        repC = np.tile(C,int(len(x_pad)/12))
        # compute residual (by subtracting periodic signal)
        residual = x_pad - repC
        # remove the padded nan-values again:
        if n_pad_end>0:
            residual = residual[n_pad_start:(-n_pad_end)]
        else:
            residual = residual[n_pad_start:]
        return [C,residual]



# fig, ax = plt.subplots(nrows=1,ncols=2,figsize = [15,5])
# ax[0].plot(climatology(Y,month, returnresidual = True,period = 'Normal'))
# ax[1].plot(climatology(Y,month, returnresidual = True,period = 'All'))

#%%
climate, res = climatology(datareal, month, returnresidual = True, period = 'All')

X = timearray
X = sm.add_constant(X)
model1 = sm.OLS(res, X)
results1 = model1.fit()


model1 = sm.OLS(res,X)
results1 = model1.fit()
results1.params

model_residual = res - results1.fittedvalues

qqplot(model_residual, fit = True, line = '45')
plt.show()
plt.hist(model_residual, bins = 50)
plt.show()


#%%
Z1 = timearray
Z2 = Z1**2
X = np.column_stack((Z1, Z2))
X = sm.add_constant(X)
model2 = sm.OLS(res, X)
results2 = model2.fit()


model2 = sm.OLS(res,X)
results2 = model2.fit()
results2.params

model_residual2 = res - results2.fittedvalues
qqplot(model_residual2, fit = True, line = '45')
plt.show()
plt.hist(model_residual2, bins = 50)
plt.show()

