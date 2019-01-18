import pygame
from math import cos, sin, radians
import random
from Files.config import *


class MovingObject(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velx = random.randint(-100,100)
        self.vely = random.randint(-100,100)

    def move(self):
        self.x += self.velx*TIME_PASSED_SECONDS
        self.y += self.vely*TIME_PASSED_SECONDS

    def draw(self):
        pygame.draw.circle(SCREEN, GREY, [int(self.x), int(self.y)], MOVING_OBJECT_RADIUS)


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


    def crash_wall_check(self):
        if self.x < 0:
            self.x += (10 + abs(self.velx))*TIME_PASSED_SECONDS
        if self.x > WIDTH_SCREEN:
            self.x += (-10 - abs(self.velx))*TIME_PASSED_SECONDS
        if self.y < 0:
            self.y += (10 + abs(self.vely))*TIME_PASSED_SECONDS
        if self.y > HEIGHT_SCREEN:
            self.y += -(10 - abs(self.vely))*TIME_PASSED_SECONDS
    
        




    


        
    

        