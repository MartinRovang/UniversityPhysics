
import numpy as np
import random

class MovingAvarage(object):
    def __init__(self, data, q):
        self.data = data
        self.q = q



    def values(self):
        q = self.q
        result = np.zeros(len(self.data) - q)
        for i in range(q, len(self.data) - q + 1):
            for j in range(-q , q + 1):
                result[-i] += self.data[-i -j]
            result[-i] /= 2*q + 1
        
        return result



class RandomWalk(object):
    def __init__(self, drift , length , var = 1):
        self.drift = drift
        self.length = length
        self.var = var


    def values(self):
        t = np.arange(0,self.length,1)
        w_noise = np.array([random.gauss(0,self.var) for i in range(self.length)])
        result = self.drift*t + np.cumsum(w_noise)

        return result