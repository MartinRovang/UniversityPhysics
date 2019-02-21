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

    def find_flock(self, boids):
        flock = self.flock
        for boid in boids:
            if (self.distance(boid) < BOID_DISTANCE_FLOCKING_RADIUS) and boid not in flock and boid != self:
                self.flock.append(boid)
            elif boid in flock:
                self.flock.remove(boid)


    def rule1(self):
        flock = self.flock
        x = 0
        y = 0
        for boid in flock:
            x += boid.x
            y += boid.y

        if len(flock) > 0:
            mean_x = x/len(flock)
            mean_y = y/len(flock)
            mean_velx = (mean_x - self.x)/100 # 1% of total
            mean_vely = (mean_y - self.y)/100 # 1% of total
            self.velx += mean_velx; self.vely += mean_vely



    def rule2(self):
        flock = self.flock
        cx = 0
        cy = 0
        for boid in flock:
            if (self.distance(boid) < BOIDS_AVOID_CRASH_DISTANCE):
                cx += -(boid.x - self.x)
                cy += -(boid.y - self.y)

        self.velx += cx; self.vely += cy;


    def rule3(self):
        flock = self.flock
        velx = 0
        vely = 0
        COESIAN_NUMBER = 0
        for boid in flock:
            distance = self.distance(boid)
            if distance < BOIDS_COHESIAN_RADIUS:
                velx += boid.velx
                vely += boid.vely
                COESIAN_NUMBER += 1

        if COESIAN_NUMBER > 0:
            mean_velx = velx/COESIAN_NUMBER
            mean_vely = vely/COESIAN_NUMBER
            mean_velx = (mean_velx - self.velx)/8 # 8 of total
            mean_vely = (mean_vely - self.vely)/8 # 8 of total
            self.velx += mean_velx; self.vely += mean_vely


    def avoid_hawk(self, hawks):
        for hawk in hawks:
            distance = self.distance(hawk)
            if distance < HAWK_TRIGGER_BOID_DISTANCE:
                self.velx += (hawk.vely - self.vely)/100
                self.vely += (hawk.velx - self.velx)/100
        

    def draw(self):
        pygame.draw.circle(SCREEN, GRAY, (int(self.x), int(self.y)), self.radius)