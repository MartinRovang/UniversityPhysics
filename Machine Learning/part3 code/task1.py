

import machinepy as ml
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

B = np.genfromtxt('city-inner-sweden.csv') # this is NXN
names = pd.read_csv('city-names-sweden.csv', header=None)
names = np.array(names)

Z = ml.feature_reduction(B)



for x,y in zip(names, Z):
    plt.plot(y[1], y[0],'^',markersize = 10 , markeredgecolor= 'black') # y is the MDS output
    plt.annotate(x[0], ([y[1],y[0]]))
plt.show()

