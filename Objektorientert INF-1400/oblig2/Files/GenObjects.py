import pygame
from math import cos, sin, radians
import random
from Files.config import *


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

    def set_vel(self, velx, vely):
        self.velx = velx
        self.vely = vely    

    def get_vel(self):
        return self.velx, self.vely


    def crash_wall_check(self, TIME_PASSED_SECONDS, wall_lock):
        if wall_lock == 1:
            if self.x - self.radius < 0:
                self.x = 0 - self.radius + WIDTH_SCREEN
                #self.velx *= -1

            if self.y - self.radius < 0:
                self.y = 0 - self.radius + HEIGHT_SCREEN
                #self.vely *= -1

            if self.x + self.radius > WIDTH_SCREEN:
                self.x = self.radius
                #self.velx *= -1

            if self.y + self.radius > HEIGHT_SCREEN:
                self.y = self.radius
                #self.vely *= -1
        else:

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
    
        




    


        
    

        