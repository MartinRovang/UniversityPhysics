
import pygame
from math import cos, sin, radians, sqrt
from Files.config import *
import random




class Obstacle(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
 
        pygame.draw.rect(SCREEN, BLUE, [int(self.x), int(self.y), OBSTACLE_WIDTH, OBSTACLE_HEIGHT], 1)
