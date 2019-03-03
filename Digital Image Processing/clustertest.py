from sklearn import cluster
import numpy as np
import matplotlib.pyplot as plt
from DIPpack import DipPackage as dip


N = 8

x = dip('t3mu4.jpg')
x2 = dip('PgcAG.jpg')
x = x.interpolate(500,500, 'NEAREST')[:,:,1]
x2 = x2.interpolate(500,500, 'NEAREST')[:,:,1]

processed = x.flatten().reshape(-1,1)
processed2 = x2.flatten().reshape(-1,1)
processed3 = np.hstack((processed, processed2))

result = cluster.k_means(processed3, N)
print(result)
centroids = result[0].astype('uint8')

row, col = result[0].shape


processed = np.zeros(processed.shape)
idx = []
for values in range(row):
    idx.append(np.where(result[1] == values))

for counter, idxxes in enumerate(idx):
    processed[idxxes] = result[0][counter,1]


processed = processed.reshape(x.shape)

fig, ax = plt.subplots(1,3)

ax[0].imshow(x)
ax[0].set_title('Original 1')
ax[1].imshow(x2)
ax[1].set_title('Original 2')
ax[2].imshow(processed)
ax[2].set_title('Processed with N = %s'%N)
plt.tight_layout()
plt.show()

