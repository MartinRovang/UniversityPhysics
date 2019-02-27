

# Ex 1

#%%
from DIPpack import DiPpackage as dip 
import matplotlib.pyplot as plt
import numpy as np 
#%%

image = dip(image_path = 'Fig0335(a)(ckt_board_saltpep_prob_pt05).tif')

image.plot()
plt.show()

#%%
test = image.medianfilter(boxsize=7)


#%%
plt.hist(image.image.flatten(), bins = 256)
plt.show()
plt.hist(test.flatten(), bins = 256)
plt.show()




#%%
plt.figure(figsize = (10,10))
plt.imshow(test, cmap = 'gray', vmin = 0, vmax = 255)
plt.show()


# Ex 3
#%%

f = [0,0,0,1,1,1,1,1,1,1,1,1,0,0,0]

F = np.fft.fft(f)
Fshift = np.fft.fftshift(F)
freq = np.fft.fftfreq(len(F))
phase = np.fft.fftshift(np.angle(F, deg=True))

plt.stem(freq, np.abs(F)**2)
plt.show()
plt.stem(freq, np.abs(Fshift)**2)
plt.show()
plt.plot(phase)
plt.show()



#%%
f0 = np.pad(f, (5,5), mode = 'constant') # can see that it turns into sinc function the more zeroes on the sides the better resolution.
F0 = np.fft.fft(f0)
Fshift0 = np.fft.fftshift(F0)
freq0 = np.fft.fftfreq(len(F0))
phase0 = np.fft.fftshift(np.angle(F0, deg=True))

plt.stem(freq0, np.abs(F0)**2)
plt.show()
plt.stem(freq0, np.abs(Fshift0)**2)
plt.show()
plt.plot(phase0)
plt.show()

#%%
f = [0,0,0,1,1,1,1,1,1,1,1,1,0,0,0]
F = np.fft.fft(f)
Fshift_pad = np.pad(F, (5,5), mode = 'constant')
freq_pad = np.fft.fftfreq(len(Fshift_pad))

plt.stem(freq_pad, np.abs(Fshift_pad)**2)
plt.show()



# Ex 4
#%%
from DIPpack import DiPpackage as dip 
import matplotlib.pyplot as plt
import numpy as np 

image = dip('Fig0424(a)(rectangle).tif')


image.plot()
plt.show()
#%%
fft = image.fft()

fft = np.log(fft)

plt.imshow(np.abs(fft)**2, cmap = 'gray')
plt.show()
phase = np.angle(fft, deg=True)
plt.imshow(phase, cmap = 'gray')
plt.show()

#%%
image = dip('Fig0425(a)(translated_rectangle).tif')


image.plot()
plt.show()
#%%
fft = image.fft()

fft = 10*np.log10(fft+1)

plt.imshow(fft.real, cmap = 'gray', vmin = 0, vmax = 255)
plt.show()
phase = np.angle(fft, deg=True)
plt.imshow(phase, cmap = 'gray')
plt.show()

#%%

image_rot = image.rotate(-45)


image_rot = dip(image_new = image_rot)

image_rot.plot()
plt.show()

fft = image_rot.fft()

fft = 10*np.log10(fft+1)

plt.imshow(fft.real, cmap = 'gray', vmin = 0, vmax = 255)
plt.show()
phase = np.angle(fft, deg=True)
plt.imshow(phase, cmap = 'gray')
plt.show()


