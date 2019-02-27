
import pygame
from math import cos, sin, radians, sqrt
from Files.config import *
import random
import numpy as np



class Obstacle():
    """
    Summary:
        When called creates an obstacle object.

    Args:
    x: x-position.

    y: y-position.

    Methods:
    draw: Draws the obstacle object on the screen.

    avoid_obstacles(moving_objects): Takes a list and sends the objects away from the obstacle border.

    """


    def __init__(self, x, y):
        """
        x: int
        y: int
        """
        self.x = x
        self.y = y
        self.width = OBSTACLE_WIDTH
        self.height = OBSTACLE_HEIGHT

    def collision(self, moving_object):
        """
        Checks for collision between the obstacle and the moving objects.\n
        Returns True
        """
        object_x = moving_object.x
        object_y = moving_object.y
        object_radius = moving_object.radius
        if (object_x  + object_radius) > self.x and (object_y + object_radius) > self.y\
             and (object_x - object_radius) < (self.x + self.width) and (object_y-object_radius) < (self.y + self.height):
             collisionx = moving_object.x
             collisiony = moving_object.y
             return True
             
        
    def avoid_obstacles(self, moving_objects):
        """
        Makes boids and hawks avoid the obstacle.\n
            moving_objects: list
        """
        for moving_object in moving_objects:
            if moving_object.distance(self) < WALL_DISTANCE_AVOID_VALUE:
                moving_object.velx -= (self.x - moving_object.x)
                moving_object.vely -= (self.y - moving_object.y)
            if self.collision(moving_object):
                moving_object.velx = -(self.x - moving_object.x)
                moving_object.vely = -(self.y - moving_object.y)

    def draw(self):
        """Draws the obstacle to the program window."""
        pygame.draw.rect(SCREEN, BLUE, [int(self.x), int(self.y), self.width, self.height], OBSTACLE_BORDER_THICKNESS)


