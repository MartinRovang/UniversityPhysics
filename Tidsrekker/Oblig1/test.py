
#%%
import matplotlib.pyplot as plt
import numpy as np

n = 100
h = np.arange(0, n, 1)
#H = np.linspace(-1, 1, 100)
H = 0.4

acf = (1/2)*(np.abs(h + 1)**(2*H) + np.abs(h - 1)**(2*H) - 2*np.abs(h)**(2*H))
derivative = H*(2*H - 1)*h**(2*(H - 1))
fig, ax = plt.subplots(2, 1, figsize = [15,10])

ax[0].plot(h, acf, color = 'white')
#ax[0].set_ylim([-1,1])
ax[0].set_title('ACF  H = %s'%H, fontsize = 30)
ax[0].set_xlabel('h', fontsize = 30 )
ax[1].plot(h, derivative, color = 'white')
#ax[1].set_ylim([-1,1])
ax[1].set_title('Asymptotisk lik H = %s'%H, fontsize = 30)
ax[1].set_xlabel('h', fontsize = 30 )
plt.tight_layout()
plt.savefig('Plots.jpg')
plt.show()
print(acf[-1] - derivative[-1])