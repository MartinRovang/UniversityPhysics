
#%%

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import datetime as dt
import random

data = np.genfromtxt('oslo_monthly.txt')
temp = data[:,2]
date = np.array(data[:,1],str)

new_date = []
for i,j in enumerate(date):
	if i%11 == 0:
		new_date.append(j)
	else:
		new_date.append('')


x = [x for x in range(len(temp))]


plt.xticks(x[-120:], new_date[-120:], rotation=45)
plt.plot(x[-120:], temp[-120:])
plt.show()


plt.xticks(x[:47][::-1], new_date[:47][::-1], rotation=45)
plt.plot(x[:47][::-1], temp[:47][::-1])
plt.show()
#print(new_date[:56])

#%%

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
plt.plot(timearray[-120:],data[-120:],linewidth=2,color = "white") # siste 10 år
ax.set_xlabel('Year',fontsize = 18)
ax.set_title('Monthly mean temperature Oslo',fontsize = 18)
ax.grid()
#ax.set_xlim(min(timearray),max(timearray))
#ax.set_ylim(-12,20)
ax.tick_params(axis='both',labelsize=22)
plt.show()


#%%

# Plot every 12
u_k = []
for i,el in enumerate(data):
	if int((i+1) % 12) == int(0):
		u_k.append(el)


plt.plot(u_k)
plt.show()








def get_monthly_mean(temp,j):
	u_k = []
	for i,el in enumerate(temp):
		if int((i+1) % j) == int(0):
			u_k.append(el)
	
	return np.mean(u_k)


for i in range(1,13):
	print('Mean in month %s is : %f'%(i, get_monthly_mean(data, i)))


#%%

#F

b = 1
t = np.linspace(0,11,10000)
phi = 0
white_noise = [random.gauss(0,1) for i in range(len(t))]


s = b*np.sin(2*np.pi*t/12 + phi)

x = s + white_noise

r = x - s

plt.plot(s)
plt.show()
plt.plot(x)
plt.show()
plt.plot(r)
plt.show()
#%%     


data = np.copy(temp)

first30months = np.copy(data)[:30*12*30]
last30months = np.copy(data)[::-1][:30*12*30]



def climatology(temp, months, residuals = False):
	mean_months = []
	residuals_array = []
	for k in range(1, months+1):
		u_k = []
		for i,el in enumerate(temp):
			if int((i+1) % k) == int(0):
				u_k.append(el)
		
		mean_months.append(np.mean(u_k))

	if residuals == True:
		temp = np.array(temp)
		for i in mean_months:
			residuals_array.append(temp-i)
		
		return mean_months, residuals_array
			
	return mean_months



plt.plot(climatology(first30months, 12), '--')
plt.plot(climatology(last30months, 12))
plt.show()

# for i in range(0,12):
# 	plt.stem(climatology(last30months, 12, residuals= True)[1][i][:100])
# 	plt.show()
#%%
