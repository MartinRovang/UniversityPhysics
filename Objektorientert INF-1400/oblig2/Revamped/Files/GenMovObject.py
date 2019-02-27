import pygame
from math import cos, sin, radians
import random
from Files.config import *
import numpy as np


class MovingObject():

    """
    Summary:
        When called creates a moving object

    Args:
    x: x-position

    y: y-position   

    __init__:\n
        
    velx: int
    
    vely: int
        
    radius: int --> MOVING_OBJECT_RADIUS| See config

    Methods:
    move(): Places the moving object according to its speed and magnitude.

    distance(object): returns distance to object. 

    crash_wall_check(): Checks if the object is colliding with the walls of the screen

    draw: Draws the obstacle object on the screen.

    """

    def __init__(self, x, y):
        """
        x: int
        y: int
        velx: int
        vely: int
        radius: int --> MOVING_OBJECT_RADIUS| See config
        """
        self.x = x
        self.y = y
        self.velx = np.random.randint(1,5)
        self.vely = np.random.randint(1,5)
        self.radius = MOVING_OBJECT_RADIUS

    def move(self):
        """
        Moves the object according to the velocity vector and MOVEMENT_MAGNITUDE scalar value from config.
        """
        # Normalization using (v/||v||)
        self.x += (self.velx/np.sqrt(self.velx**2+self.vely**2))*MOVEMENT_MAGNITUDE
        self.y += (self.vely/np.sqrt(self.velx**2+self.vely**2))*MOVEMENT_MAGNITUDE


    def distance(self, objecct):
        """
        Returns the distance to the object\n
            objecct: class
            """
        return np.sqrt((objecct.x - self.x)**2 + (objecct.y - self.y)**2)


    def crash_wall_check(self):
        """Changes the direction the boids if they collide with the wall."""
        if self.x - self.radius < 0:
            self.x = self.radius
            self.velx *=  WALL_REFLECT

        if self.y - self.radius < 0:
            self.y = self.radius
            self.vely *= WALL_REFLECT

        if self.x + self.radius > WIDTH_SCREEN:
            self.x = (WIDTH_SCREEN - self.radius)
            self.velx *= WALL_REFLECT

        if self.y + self.radius > HEIGHT_SCREEN:
            self.y = (HEIGHT_SCREEN - self.radius)
            self.vely *= WALL_REFLECT



    def draw(self):
        raise Exception('Cant draw on moving object only allowed on a boid, hawk or obstacle')
    
        

