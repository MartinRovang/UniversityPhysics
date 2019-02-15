import pygame
from math import cos, sin, radians
import random
from Files.config import *
import numpy as np



class MovingObject(object):

    """
    Summary:
        When called creates a moving object

    Args:
    x: x-position

    y: y-position   

    Methods:
    move(TIME_PASSED_SECONDS): Places the moving object according to its speed and magnitude.

    get_pos: Returns the position (x, y).

    set_pos(x,y): Sets the position to x, y.

    set_vel(velx,vely): Sets the velocity to (velx, vely).

    get_vel: Returns the velocity (velx, vely).

    crash_wall_check(TIME_PASSED_SECONDS, wall_lock): Checks if the object is colliding with the walls of the screen, and bounce them off if wall_lock == 1 else they go to the other side.

    draw: Draws the obstacle object on the screen.

    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velx = np.random.randint(1,5)
        self.vely = 0
        self.radius = MOVING_OBJECT_RADIUS

    def move(self, TIME_PASSED_SECONDS):
        self.x += (self.velx/np.sqrt(self.velx**2+self.vely**2))*MOVEMENT_MAGNITUDE*TIME_PASSED_SECONDS
        self.y += (self.vely/np.sqrt(self.velx**2+self.vely**2))*MOVEMENT_MAGNITUDE*TIME_PASSED_SECONDS


    def crash_wall_check(self):

        if self.x - self.radius < 0:
            self.x = 0 + self.radius
            self.velx *= -1

        if self.y - self.radius < 0:
            self.y = 0 + self.radius
            self.vely *= -1

        if self.x + self.radius > WIDTH_SCREEN:
            self.x = WIDTH_SCREEN - self.radius
            self.velx *= -1

        if self.y + self.radius > HEIGHT_SCREEN:
            self.y = HEIGHT_SCREEN - self.radius
            self.vely *= -1



    def draw(self):
        raise Exception('Cant draw on moving object only allowed on a boid, hawk or obstacle')
    
        

