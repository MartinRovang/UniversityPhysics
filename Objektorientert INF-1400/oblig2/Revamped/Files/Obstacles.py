
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

    def draw(self):
        """Draws the obstacle to the program window."""
        pygame.draw.rect(SCREEN, BLUE, [int(self.x), int(self.y), OBSTACLE_WIDTH, OBSTACLE_HEIGHT], OBSTACLE_BORDER_THICKNESS)


    def avoid_obstacles(self, moving_objects):
        """
        Makes boids and hawks avoid the obstacle.\n
            moving_objects: list
        """
        for moving_object in moving_objects:
            if moving_object.distance(self) < WALL_DISTANCE_AVOID_VALUE:
                moving_object.velx -= (self.x - moving_object.x)*30
                moving_object.velx -= (self.x - moving_object.x)*30
