import numpy as np
import matplotlib.pyplot as plt


def histeq(img, L, prob = False, stairplot = False):
    """
    img -> np array
    L -> max intensity level i.e 256
    prob = True returns probability array, default = False
    stairplot = False -> plots staircase plot default = False

    Return result, probability
    or 
    Return result
    """
    M, N = img.shape
    hist, bins = np.histogram(img.flatten(),L,[0,L])
    probability = hist/(M*N)
    result = img.astype('float')
    stair = []

    for i in range(0, L):
        idx = np.where(img == i)
        result[idx] = (L-1)*np.sum(probability[0:i+1])
        stair.append((L-1)*np.sum(probability[0:i+1]))
    result = result.astype('uint8')

    if stairplot == True:
        return result, stair

    if prob == True:
        return result, probability
    else:
        return result



image = np.array([[0,0,0,0,0,0],[1,1,1,1,1,0],[1,2,2,2,1,0],[0,2,3,2,1,0],[0,2,1,1,1,0],[0,0,0,0,0,0]])


result = histeq(image,4)

fig, ax = plt.subplots(2,2)
ax[0,0].imshow(image, cmap = 'gray')
ax[1,0].imshow(result, cmap = 'gray')
ax[0,1].hist(image.flatten(),bins = 4, range = [0,4], align= 'left', rwidth = 0.1, color = 'black')
ax[1,1].hist(result.flatten(),bins = 4, range = [0,4], align = 'left', rwidth=0.1, color = 'black')
plt.show()