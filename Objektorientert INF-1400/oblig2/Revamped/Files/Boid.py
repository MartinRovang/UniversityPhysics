import pygame
from math import cos, sin, radians, sqrt
from Files.config import *
from Files.GenMovObject import MovingObject
import random
import numpy as np

class Boid(MovingObject):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.flocked = 0
        self.flock = []
        self.radius = BOIDS_RADIUS

    def rule1(self, boids): 
        mean_x = []
        mean_y = []
        flock = self.flock
        mean_pos_x = 0
        mean_pos_y = 0

        for boid in boids:
            if boid != self:
                distance = sqrt((boid.x - self.x)**2 + (boid.y - self.y)**2)
                if distance <= BOID_DISTANCE_FLOCKING_RADIUS and boid not in flock:
                    mean_x.append(boid.x)
                    mean_y.append(boid.y)
                    flock.append(boid)
                if distance > BOID_DISTANCE_FLOCKING_RADIUS and boid in flock:
                    flock.remove(boid)


        if len(flock) > 0:
            mean_pos_x = np.mean(mean_x)
            mean_pos_y = np.mean(mean_y)
            self.velx = mean_pos_x
            self.vely = mean_pos_y


    def rule2(self, boids):
        for boid in boids:
            if boid != self:
                distance = sqrt((boid.x-self.x)**2 + (boid.y-self.y)**2)
                if distance < BOIDS_AVOID_CRASH_DISTANCE + boid.radius:
                    boid.velx = (boid.x - self.x)
                    boid.vely = (boid.y - self.y)
                if distance < 1:
                    boid.velx = 5
                    boid.vely = 0



    def rule3(self, boids):
        flock = self.flock
        velx = 0
        vely = 0
        if len(flock) > 0:
            for boid in flock:
                velx += boid.velx
                vely += boid.vely
        
            self.velx = velx/len(flock)
            self.vely = vely/len(flock)


    def draw(self):
        pygame.draw.circle(SCREEN, GRAY, (int(self.x), int(self.y)), self.radius)