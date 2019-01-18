import pygame
from math import cos, sin, radians, sqrt
from Files.config import *
from Files.GenObjects import MovingObject
import random

class Boid(MovingObject):

    def __init__(self, x , y):
        super().__init__(x, y)
        self.flocked = 0

    def noisy_movement(self):
        if self.flocked == 0:
            #Make white noise movement
            self.velx += random.gauss(BOID_MEAN_NOISY_X, BOID_VARIANCE_NOISY_X)
            self.vely += random.gauss(BOID_MEAN_NOISY_Y, BOID_VARIANCE_NOISY_Y)
            self.x += self.velx*TIME_PASSED_SECONDS
            self.y += self.vely*TIME_PASSED_SECONDS

        if self.flocked != 0:
            self.move()


    def flocking(self, boids): 
        flock = []
        x = 0
        y = 0
        i = 0
        mean_pos_x = 0
        mean_pos_y = 0
        for boid in boids:
            if boid != self:
                distance = sqrt((boid.x-self.x)**2 + (boid.y-self.y)**2)
                if distance <= BOID_DISTANCE_FLOCKING_RADIUS and boid not in flock:
                    flock.append(boid)
                    x += boid.x 
                    y += boid.y
                    i += 1

                if distance > BOID_DISTANCE_FLOCKING_RADIUS and boid in flock:
                    flock.remove(boid)
                    x -= boid.x
                    y -= boid.y
                    i -= 1
        try:
            mean_pos_x = (x/i) - self.x
            mean_pos_y = (y/i) - self.y
        except ZeroDivisionError:
            pass
        
        if i > 0:
            self.flocked = 1
            self.velx = mean_pos_x
            self.vely = mean_pos_y
        else:
            self.flocked = 0

    
    def avoid_crash(self, boids):
        #pass
        for boid in boids:
            if boid != self:
                distance = sqrt((boid.x-self.x)**2 + (boid.y-self.y)**2)
                if distance < BOIDS_AVOID_CRASH_DISTANCE:
                    boid.x += (boid.x - self.x)*TIME_PASSED_SECONDS*10
                    boid.y += (boid.y - self.y)*TIME_PASSED_SECONDS*10
                if distance < 1:
                    boid.x += 1*TIME_PASSED_SECONDS
                    boid.y += 1*TIME_PASSED_SECONDS





                
            




    
        