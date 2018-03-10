import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as poly



SMALL_SIZE = 8
MEDIUM_SIZE = 8
BIGGER_SIZE = 12

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=BIGGER_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title



# example data
Current = np.array([3.2, 4.9, 9.9, 32.6, 49.0, 96.8, 800, 4400])*10**(-6)  #minus 6
Voltage = np.array([4.0, 6.0, 12.0, 39.5, 59.3, 117.2, 1100, 5500])*10**(-3) #minus 3

Current2 = np.array([0.2, 0.4, 0.9, 3.1, 4.6, 9.3, 78.0, 288.9])*10**(-6)  #minus 6
Voltage2 = np.array([0.4, 0.6, 1.1, 3.8, 5.7, 11.3, 94.5, 349.5])*10**(-3) #minus 3


# including upper and lower limits
xerr = np.around([3.2*0.002 + 0.4, 4.9*0.002 + 0.4, 9.9*0.002 + 0.4, 32.6*0.002 + 0.4, 49.0*0.002 + 0.4, 96.8*0.002 + 0.4, 800*0.002 + 200, 4400*0.002 + 200], decimals=2)*10**(-6)
yerr = np.around([4.0*0.003 + 0.2, 6.0*0.003 + 0.2, 12.0*0.003 + 0.2, 39.5*0.003 + 0.2, 59.3*0.003 + 0.2, 117.2*0.003 + 0.2, 1100*0.005 + 200, 5500*0.005 + 200], decimals=1)*10**(-3)


xerr2 = (Current2*0.002) + 0.2*10**(-6)
yerr2 = (Voltage2*0.001) + 0.1*10**(-3)



Current3 = np.concatenate((Current2, Current), axis=0)
Voltage3 = np.concatenate((Voltage2, Voltage), axis=0)

Current3error = np.concatenate((xerr2, xerr), axis=0)
Voltage3error = np.concatenate((yerr2, yerr), axis=0)

coefs,cov = np.polyfit(Current3, Voltage3,1,cov=True)
ffit = poly.polyval(Current3, coefs)

errormotstand , errorkonstantledd = (np.sqrt(np.diag(cov)))
print("Usikkerhet Motstand:" ,errormotstand)
print(errorkonstantledd)



print("STRØMFEIL: " ,xerr2)
print("SPENNINGSFEIL: ", yerr2)


plt.figure(figsize=(10,5))
ax = plt.subplot(111)
ax.set_yscale('log')
ax.set_xscale('log')
plt.errorbar(Current3, Voltage3, xerr=Current3error,yerr=Voltage3error, capsize = 2,label='Forsøk')
plt.plot(Current3, coefs[0]*Current3 ,color='red', label='Lineær Regresjon')

plt.legend(loc='upper left')
plt.xlabel('Strøm [A]')
plt.ylabel('Spenning [V]')
plt.savefig('example.pdf')

plt.show()


from scipy import stats
import sys


# This reads in the weight and mortality data to two arrays.
Weight = Current3
Mortality = Voltage3

# This calculates the regression equation.
slope, intercept, r_value, p_value, std_err = stats.linregress(x=Weight,y=Mortality)

# This calculates the predicted value for each observed value
obs_values = Mortality
pred_values = slope * Weight + intercept

# This prints the residual for each pair of observations
Residual = obs_values - pred_values
print(coefs)
print("RESIDUALS: %s" %Residual)


# ax = plt.subplot(111)
# ax.set_yscale('log')
# ax.set_xscale('log')
#
# plt.legend(loc='upper left')
# plt.ylabel('Residualer')


# Lineær regresjonsfunksjon.
def basic_linear_regression(x, y):
    length = len(x)
    sum_x = sum(x)
    sum_y = sum(y)

    sum_x_squared = sum(map(lambda a: a * a, x))
    sum_of_products = sum([x[i] * y[i] for i in range(length)])

    a = (sum_of_products - (sum_x * sum_y) / length) / (sum_x_squared - ((sum_x ** 2) / length))
    b = (sum_y - a * sum_x) / length
    return a, b

print(basic_linear_regression(Current3,Voltage3))

plt.show()
# create data
x = Current3
y = Voltage3/Current3



plt.show()
