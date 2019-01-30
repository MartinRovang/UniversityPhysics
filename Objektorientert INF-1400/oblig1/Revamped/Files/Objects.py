import pygame
from Files.config import *


class Ball():
    def __init__(self):
        self.x = BALL_START_POS_X
        self.y = BALL_START_POS_Y
        self.radius = BALL_RADIUS
    

    def draw():
        pygame.draw.circle(SCREEN, GRAY, (self.x, self.y)), self.radius)



class Platform():
    def __init__(self):
        self.x = PLATFORM_START_POS_X
        self.y = PLATFORM_START_POS_Y
        self.width = PLATFORM_WIDTH
        self.height = PLATFORM_HEIGHT
    

    def draw():
        pygame.draw.rect(SCREEN, GRAY, (self.x, self.y, self.width, self.height))



class Bricks():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.height = BRICKS_HEIGHT
        self.width = BRICKS_WIDTH

    def draw():
        pygame.draw.rect(SCREEN, GRAY, (self.x, self.y, self.width, self.height))

    

    