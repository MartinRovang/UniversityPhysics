import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.animation as animation

cap = cv2.VideoCapture('VIDEOHERE.wmv')
fgbg = cv2.createBackgroundSubtractorMOG2(varThreshold=35, detectShadows=False)

x_len = 60
y_range = [-2, 15]

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
xs = list(range(0,60))
ys = [0] * x_len
ax.set_ylim(y_range)

line, = ax.plot(xs, ys)

plt.title('Movement over Time')
plt.show()


def animate(i, ys):
    ys.append(average)
    ys = ys[-x_len:]
    line.set_ydata(ys)
    return line,

ani = animation.FuncAnimation(fig, animate, fargs=(ys,), interval=60, blit=False)

while True:
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    cv2.imshow('Original', frame)
    cv2.imshow('Masked', fgmask)

    average = (np.average(fgmask))
    print(average)


    plt.pause(.0001)


    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()