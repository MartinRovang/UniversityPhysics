

"""
  █████▒█    ██ ▓█████  ██▓        ▄████▄   ██▓    ▄▄▄        ██████   ██████ 
▓██   ▒ ██  ▓██▒▓█   ▀ ▓██▒       ▒██▀ ▀█  ▓██▒   ▒████▄    ▒██    ▒ ▒██    ▒ 
▒████ ░▓██  ▒██░▒███   ▒██░       ▒▓█    ▄ ▒██░   ▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄   
░▓█▒  ░▓▓█  ░██░▒▓█  ▄ ▒██░       ▒▓▓▄ ▄██▒▒██░   ░██▄▄▄▄██   ▒   ██▒  ▒   ██▒
░▒█░   ▒▒█████▓ ░▒████▒░██████▒   ▒ ▓███▀ ░░██████▒▓█   ▓██▒▒██████▒▒▒██████▒▒
 ▒ ░   ░▒▓▒ ▒ ▒ ░░ ▒░ ░░ ▒░▓  ░   ░ ░▒ ▒  ░░ ▒░▓  ░▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░
 ░     ░░▒░ ░ ░  ░ ░  ░░ ░ ▒  ░     ░  ▒   ░ ░ ▒  ░ ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░
 ░ ░    ░░░ ░ ░    ░     ░ ░      ░          ░ ░    ░   ▒   ░  ░  ░  ░  ░  ░  
          ░        ░  ░    ░  ░   ░ ░          ░  ░     ░  ░      ░        ░  
                                  ░                                           
This is the fuel class file, contains the fuel image and sprite information.
"""


import pygame
from Files.config import *
import numpy as np
import os

#Game folder
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')



class FuelBarrel(pygame.sprite.Sprite):
    """
    Fuel for the players to refuel their ship.
    """
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.fuel_amount = FUEL_AMOUNT
        self.image = pygame.image.load(os.path.join(img_folder, 'fuelbarrel.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (np.random.randint(0, WIDTH_SCREEN),np.random.randint(0, HEIGHT_SCREEN))