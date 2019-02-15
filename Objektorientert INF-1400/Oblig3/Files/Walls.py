import pygame
from Files.config import *
from math import sqrt, cos
import numpy as np
import os

#Game folder
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')



class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, x1, y1):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((x1, y1))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


