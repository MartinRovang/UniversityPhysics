
"""
 █     █░ ▄▄▄       ██▓     ██▓        ▄████▄   ██▓    ▄▄▄        ██████   ██████ 
▓█░ █ ░█░▒████▄    ▓██▒    ▓██▒       ▒██▀ ▀█  ▓██▒   ▒████▄    ▒██    ▒ ▒██    ▒ 
▒█░ █ ░█ ▒██  ▀█▄  ▒██░    ▒██░       ▒▓█    ▄ ▒██░   ▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄   
░█░ █ ░█ ░██▄▄▄▄██ ▒██░    ▒██░       ▒▓▓▄ ▄██▒▒██░   ░██▄▄▄▄██   ▒   ██▒  ▒   ██▒
░░██▒██▓  ▓█   ▓██▒░██████▒░██████▒   ▒ ▓███▀ ░░██████▒▓█   ▓██▒▒██████▒▒▒██████▒▒
░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒░▓  ░░ ▒░▓  ░   ░ ░▒ ▒  ░░ ▒░▓  ░▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░
  ▒ ░ ░    ▒   ▒▒ ░░ ░ ▒  ░░ ░ ▒  ░     ░  ▒   ░ ░ ▒  ░ ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░
  ░   ░    ░   ▒     ░ ░     ░ ░      ░          ░ ░    ░   ▒   ░  ░  ░  ░  ░  ░  
    ░          ░  ░    ░  ░    ░  ░   ░ ░          ░  ░     ░  ░      ░        ░  
                                      ░                                           
This is the wall class file, contains the structure of the walls.
"""


import pygame
from Files.config import *




class Wall(pygame.sprite.Sprite):
    """
    Walls that players and bullets can crash with.
    """
    def __init__(self, x, y, x1, y1, Image = None):
        """Arguments give the coordinates and size of rectangle."""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((x1, y1))
        self.image.fill((WHITE))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


