from DIPpack import DiPpackage as dip
import matplotlib.pyplot as plt

image = dip('Fig0237(a)(characters test pattern)_POST.tif')

new = image.gaussian_lp(60)
new2 = image.gaussian_hp(60)

plt.imshow(new,cmap = 'gray')
plt.show()
plt.imshow(new2,cmap = 'gray')
plt.show()