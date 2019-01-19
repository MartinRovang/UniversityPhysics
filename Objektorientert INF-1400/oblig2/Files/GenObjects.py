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


    def avoid_obstacles(self, obstacles):
        for obstacle in obstacles:
            if self.x+MOVING_OBJECT_RADIUS > obstacle.x and self.x-MOVING_OBJECT_RADIUS < obstacle.x+OBSTACLE_WIDTH\
             and self.y+MOVING_OBJECT_RADIUS > obstacle.y and self.y-MOVING_OBJECT_RADIUS < obstacle.y+OBSTACLE_HEIGHT:
                
                if self.x+MOVING_OBJECT_RADIUS > obstacle.x and self.x-MOVING_OBJECT_RADIUS < obstacle.x+OBSTACLE_WIDTH:
            
                    if self.velx > 0:
                        self.x -= 10
                    if self.vely < 0:
                        self.x += 10

                if self.y+MOVING_OBJECT_RADIUS > obstacle.y and self.y-MOVING_OBJECT_RADIUS < obstacle.y+OBSTACLE_HEIGHT:

                    if self.vely > 0:
                        self.y -= 10
                    if self.vely < 0:
                        self.y += 10


    def crash_wall_check(self, TIME_PASSED_SECONDS):
        if self.x < 0:
            self.x = 0 + MOVING_OBJECT_RADIUS
        if self.x > WIDTH_SCREEN:
            self.x = WIDTH_SCREEN - MOVING_OBJECT_RADIUS
        if self.y < 0:
            self.y = 0 + MOVING_OBJECT_RADIUS
        if self.y > HEIGHT_SCREEN:
            self.y = HEIGHT_SCREEN-MOVING_OBJECT_RADIUS



    def draw(self):
        raise Exception('Cant draw on moving object only allowed on a boid, hawk or obstacle')
    
        




    


        
    

        