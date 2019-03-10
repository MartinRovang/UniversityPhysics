import numpy as np 
import matplotlib.pyplot as plt
from PIL import Image


image = plt.imread('profil.jpg')
w = plt.imread('pen.jpg')
image.setflags(write=1)

wtemp = np.zeros(image.shape)
wtemp[0:w.shape[0], 0:w.shape[1]] = w
w = wtemp.astype('uint8')
image = image.astype('uint8')

# bit2dec = np.vectorize(int)
# dec2bin = np.vectorize(bin)

# watermarked = 4*(np.copy(image)/4) + w/64
# watermarked = watermarked.astype('uint8')




def watermark(x, w):
    x = format(x, '#010b')
    w = format(w, '#010b')
    toadd = w[2:4]
    temp = x[:-2] + toadd
    result = int(temp, 2)
    #result = temp
    return result


def dewatermark(x):
    x = format(x, '#010b')
    first = '0b'
    mid = x[-2:]
    third = '000000'
    y = first + mid + third
    result = int(y, 2)
    return result

vecwatermark = np.vectorize(watermark)
vecdewatermark = np.vectorize(dewatermark)
test = vecwatermark(image, w)


#test = (4*(image/4) + w/64)
# rem = (test-image).astype('uint8')
# rem = test-image

rem = vecdewatermark(test)


fig, ax = plt.subplots(1,3)
ax[0].imshow(test, cmap = 'gray')
ax[0].set_title('Original image')
ax[1].imshow(test, cmap = 'gray')
ax[1].set_title('Watermarked image')
ax[2].imshow(rem, cmap = 'gray')
ax[2].set_title('Extracted watermark')
plt.tight_layout()
plt.show()

print(test.shape)
print(image.shape)


plt.figure()
plt.axis('off')
plt.imshow(test)
#plt.savefig('Watermarkedprofile.png', bbox_inches=extent)
plt.savefig('Watermarkedprofile.png',bbox_inches='tight',transparent=True, pad_inches=0)
plt.show()
plt.close()

# image = plt.imread('Watermarkedprofile.png')*255
# image = image.astype('uint8')
# newtest = vecdewatermark(image)
# print(np.unique(newtest))

# plt.imshow(newtest)
# plt.show()

# fig, ax = plt.subplots(1,3)
# ax[0].imshow(10*np.log10(np.abs(np.fft.fftshift(np.fft.fft(image)))), cmap = 'gray')
# ax[1].imshow(10*np.log10(np.abs(np.fft.fftshift(np.fft.fft(test)))), cmap = 'gray')
# ax[2].imshow(10*np.log10(np.abs(np.fft.fftshift(np.fft.fft(rem)))), cmap = 'gray')
# plt.tight_layout()
# plt.show()



# plt.imshow(test, cmap = 'gray')
# plt.show()


# def remove6MSB(x):
#     x = bin(x)
#     toadd = '000000'
#     temp = np.copy(x)[:2]
#     temp2 = np.copy(x)[-2:]
#     new = temp + temp2 + toadd
#     if new[0] != 0:
#         y =  '0' + temp
#         new = y
#     result = int(new, 2)
#     return result

# vecremove6MSB = np.vectorize(remove6MSB)

# new = vecremove6MSB(test)


# plt.imshow(new)
# plt.show()

# new = new.astype('uint8')

# plt.imshow(new, cmap = 'gray', vmin = 0, vmax = 255)
# plt.show()


# def scale(x):
#     g1 = x-np.min(x)
#     g = g1/np.max(g1)*255
#     g = g.astype('uint8')
#     return g

