import numpy as np
from numpy.linalg import inv

A = np.array([[0], [2], [2], [4]])
B = np.array(
[[0,0,0*0,1],
[0,1,0*1,1],
[1,0,1*0,1],
[1,1,1*1,1]])


res = inv(B)@A

print(res)

