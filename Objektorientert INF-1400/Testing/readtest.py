
import csv


class Reader:
    def __init__(self):
        self.filereader = csv.writer(open("lol.txt", 'a'))
    
    def put_in(self, stringed):
        # stringed on the form larve-hest-mann
        self.filereader.writerow([stringed])
        print('Wrote to file %s'%stringed.split('-'))





import numpy as np 
import matplotlib.pyplot as plt


xx, yy = np.arange(-10, 10, 0.2), np.arange(-10, 10, 0.2)
X, Y = np.meshgrid(xx, yy)
 
r, theta = np.sqrt(X**2 + Y**2), np.arctan2(Y,X)


g = 1/(r**2+1)


plt.imshow(theta, cmap = 'inferno')
plt.colorbar()
plt.show()