from os import environ
import pygame
import numpy as np
from time import sleep
import csv

# Set gamescreen size
width_screen = 800
height_screen = 800

SCREENSIZE = (width_screen, height_screen)

# Set gamescreen to middle
environ['SDL_VIDEO_CENTERED'] = '1'
# Initialize pygame
pygame.init()

# Set screen object
screen = pygame.display.set_mode(SCREENSIZE)



class boink(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velx = 1
        self.vely = 0.5
        #self.img = pygame.draw.rect(screen,(100,100,100), (20,20,20,20))

    def Update(self, groups):
        # groups = {0:[mean distance x,mean distance y, mean vel x, mean vel y, [bird1, bird2....]]}
        distance = 0
        for murder in groups:
            if distance < (np.sqrt(groups[murder][0]**2+groups[murder][1]**2)-np.sqrt(self.x**2 + self.y**2)):
                distance = (np.sqrt(groups[murder][0]**2+groups[murder][1]**2)-np.sqrt(self.x**2 + self.y**2))
                group_assigned = murder
            if self in groups[murder][4]:
                groups[murder][4].remove(self)

        groups[murder][4].append(self)
        self.velx = groups[group_assigned][2]
        self.vely = groups[group_assigned][3]

        self.x += self.velx
        self.y += self.vely

        pygame.draw.rect(screen,(100,100,100), (self.x,self.y,20,20))







class simulation(object):
    
    def __init__(self):
        self.groups = {}







while True:
