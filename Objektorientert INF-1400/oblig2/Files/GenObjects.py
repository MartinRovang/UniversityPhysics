import pygame
from math import cos, sin, radians
import random
from Files.config import *


class MovingObject(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velx = 1
        self.vely = 1
        self.radius = MOVING_OBJECT_RADIUS

    def move(self, TIME_PASSED_SECONDS):
        self.x += self.velx*TIME_PASSED_SECONDS*MOVEMENT_MAGNITUDE
        self.y += self.vely*TIME_PASSED_SECONDS*MOVEMENT_MAGNITUDE



    def get_pos(self):
        return self.x, self.y

    def set_pos(self, x, y):
        self.x = x
        self.y = y  

    def set_vel(self, x, y):
        self.velx = x
        self.vely = y    

    def get_vel(self):
        return self.velx, self.vely


    def crash_wall_check(self, TIME_PASSED_SECONDS):
        if self.x-self.radius < 0:
            self.x = 0 + self.radius
            self.velx *= -1
        if self.x+self.radius > WIDTH_SCREEN:
            self.x += -self.radius
            self.velx *= -1
        if self.y-self.radius < 0:
            self.y = 0 + self.radius
            self.vely *= -1
        if self.y+self.radius > HEIGHT_SCREEN:
            self.y += -self.radius
            self.vely *= -1



    def draw(self):
        raise Exception('Cant draw on moving object only allowed on a boid, hawk or obstacle')
    
        




    


        
    

        