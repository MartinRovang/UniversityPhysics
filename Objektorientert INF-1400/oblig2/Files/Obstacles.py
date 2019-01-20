
import pygame
from math import cos, sin, radians, sqrt
from Files.config import *
import random
import numpy as np



class Obstacle(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
 
        pygame.draw.rect(SCREEN, BLUE, [int(self.x), int(self.y), OBSTACLE_WIDTH, OBSTACLE_HEIGHT], OBSTACLE_BORDER_THICKNESS)


    def avoid_obstacles(self, moving_objects):
        for moving_object in moving_objects:
            if (moving_object.x + moving_object.radius) > self.x and (moving_object.x - moving_object.radius) < (self.x + OBSTACLE_WIDTH)\
            and  (moving_object.y + moving_object.radius) > self.y and (moving_object.y - moving_object.radius) < (self.y + OBSTACLE_HEIGHT) :
                
                moving_object.x += np.sign(moving_object.velx)*(-5)
                moving_object.y += np.sign(moving_object.vely)*(-5)
