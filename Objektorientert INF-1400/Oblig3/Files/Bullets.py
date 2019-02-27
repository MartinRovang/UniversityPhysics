import pygame
from Files.config import *
import numpy as np
import os

#Game folder
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')



class Bullets(pygame.sprite.Sprite):
    """
    The bullet class for shooting other players.
    """
    
    def __init__(self, player):
        """
        Initiates the bullet\n
        player -> pygame sprite.   
            """
        pygame.sprite.Sprite.__init__(self)

        self.velx = np.cos(player.angle*np.pi/180 + np.pi/2)
        self.vely = -np.sin(player.angle*np.pi/180 + np.pi/2)
        self.fuel_amount = FUEL_AMOUNT
        self.image = pygame.image.load(os.path.join(img_folder, 'bullet.png')).convert_alpha()
        self.image = pygame.transform.rotate(self.image, player.angle - 90)
        self.rect = self.image.get_rect()
        self.rect.midtop = (player.rect.midtop[0] + np.cos(player.angle*np.pi/180 + np.pi/2)*90, player.rect.midtop[1] - np.sin(player.angle*np.pi/180 + np.pi/2)*100)
        

    def update(self):
        """
        Updates the bullet position.
        """
        self.rect.x += self.velx*BULLET_SPEED
        self.rect.y += self.vely*BULLET_SPEED

