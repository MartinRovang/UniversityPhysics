

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

plt.stem(freq, np.abs(F))
plt.show()
plt.stem(freq, Fshift)
plt.show()
plt.stem(phase)
plt.show()



#%%
f0 = np.pad(f, (50,50), mode = 'constant') # can see that it turns into sinc function the more zeroes on the sides the better resolution.
F0 = np.fft.fft(f0)
Fshift0 = np.fft.fftshift(F0)
freq0 = np.fft.fftfreq(len(F0))
phase0 = np.angle(F0, deg=True)
phasefreq = np.fft.fftfreq(len(phase0))


plt.stem(f)
plt.show()
plt.stem(freq0, np.abs(F0))
plt.show()
plt.stem(freq0, Fshift0)
plt.show()
plt.stem(phasefreq, phase0)
plt.show()

#%%
f = [0,0,0,1,1,1,1,1,1,1,1,1,0,0,0]
F = np.fft.fft(f)
Fshift_pad = np.pad(F, (5,5), mode = 'constant')
freq_pad = np.fft.fftfreq(len(Fshift_pad))

plt.stem(freq_pad, Fshift_pad)
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
fft = image.fft() # 2d Boxcar in spacial/time domain

fftlog = np.log(fft+1)

plt.imshow(np.abs(fftlog))
plt.show()
phase = np.angle(fft, deg=True)
plt.imshow(phase)
plt.show()

#%%
image = dip('Fig0425(a)(translated_rectangle).tif')


image.plot()
plt.show()
#%%
fft = image.fft()
fftlog = np.log(fft+1)
plt.imshow(np.abs(fftlog))
plt.show()

phase = np.angle(fft, deg=True)
plt.imshow(phase)
plt.show()

#%%

image_rot = image.rotate(-45)
image_rot = dip(image_new = image_rot)

image_rot.plot()
plt.show()

fft = image_rot.fft()
fft = np.log(fft+1)

plt.imshow(np.abs(fft))
plt.show()
phase = np.angle(fft, deg=True)
plt.imshow(phase, cmap = 'gray')
plt.show()

