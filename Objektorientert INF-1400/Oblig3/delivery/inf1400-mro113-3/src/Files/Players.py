

"""
 ██▓███   ██▓    ▄▄▄     ▓██   ██▓▓█████  ██▀███      ▄████▄   ██▓    ▄▄▄        ██████   ██████ 
▓██░  ██▒▓██▒   ▒████▄    ▒██  ██▒▓█   ▀ ▓██ ▒ ██▒   ▒██▀ ▀█  ▓██▒   ▒████▄    ▒██    ▒ ▒██    ▒ 
▓██░ ██▓▒▒██░   ▒██  ▀█▄   ▒██ ██░▒███   ▓██ ░▄█ ▒   ▒▓█    ▄ ▒██░   ▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄   
▒██▄█▓▒ ▒▒██░   ░██▄▄▄▄██  ░ ▐██▓░▒▓█  ▄ ▒██▀▀█▄     ▒▓▓▄ ▄██▒▒██░   ░██▄▄▄▄██   ▒   ██▒  ▒   ██▒
▒██▒ ░  ░░██████▒▓█   ▓██▒ ░ ██▒▓░░▒████▒░██▓ ▒██▒   ▒ ▓███▀ ░░██████▒▓█   ▓██▒▒██████▒▒▒██████▒▒
▒▓▒░ ░  ░░ ▒░▓  ░▒▒   ▓▒█░  ██▒▒▒ ░░ ▒░ ░░ ▒▓ ░▒▓░   ░ ░▒ ▒  ░░ ▒░▓  ░▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░
░▒ ░     ░ ░ ▒  ░ ▒   ▒▒ ░▓██ ░▒░  ░ ░  ░  ░▒ ░ ▒░     ░  ▒   ░ ░ ▒  ░ ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░
░░         ░ ░    ░   ▒   ▒ ▒ ░░     ░     ░░   ░    ░          ░ ░    ░   ▒   ░  ░  ░  ░  ░  ░  
             ░  ░     ░  ░░ ░        ░  ░   ░        ░ ░          ░  ░     ░  ░      ░        ░  
                          ░ ░                        ░                                                            
This is the player class file, contains the player structure, and how to handle controls.
"""



import pygame
from Files.config import *
from Files.Bullets import Bullets
from Files.Diagnostics.timing import Profiler
import numpy as np
import os

#Game folder
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')


class Player1(pygame.sprite.Sprite):
    """Class for player 1"""
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.velx = 0
        self.vely = 0
        self.angle = 0
        self.engine = 'off'
        self.fuel = PLAYER_START_FUEL
        self.points = 0
        self.rocket1image = pygame.image.load(os.path.join(img_folder, 'rocket111.png')).convert_alpha()
        self.rocket2image = pygame.image.load(os.path.join(img_folder, 'rocket112.png')).convert_alpha()
        self.image = self.rocket1image
        self.rect = self.image.get_rect() # Returns a new rectangle covering the entire surface. This rectangle will always start at 0, 0 with a width. and height the same size as the image.
        self.rect.center = (WIDTH_SCREEN/4, HEIGHT_SCREEN/4)
        self.fuelinfo_x = 10
        self.fuelinfo_y = 50
        self.pointsinfo_x = 10
        self.pointsinfo_y = 100

    def reset(self):
        """Reset player stats and withdraw points"""
        self.points -= 1
        self.velx = 0
        self.vely = 0
        self.angle = 0
        self.engine = 'off'
        self.fuel = PLAYER_START_FUEL
        self.rect.center = (WIDTH_SCREEN/4, HEIGHT_SCREEN/4)
    

    def controls(self, bullet_sprites):
        """
        Controls for the player see --> PLAYER1 controls in config.\n
            bullet_sprites -> pygame sprite group
        """
        # Controls
        keys = pygame.key.get_pressed()
        if keys[eval(f'pygame.K_{PLAYER_1_LEFT_MOVEMENT}')]:
            self.angle += 2

        if keys[eval(f'pygame.K_{PLAYER_1_RIGHT_MOVEMENT}')]:
            self.angle -= 2

        if keys[eval(f'pygame.K_{PLAYER_1_FIRE}')]:
            bullet_sprites.add(Bullets(self))

        if keys[eval(f'pygame.K_{PLAYER_1_BOOST}')]:
            if self.fuel > 0:
                self.engine = 'on'
                self.vely = -np.sin(self.angle*np.pi/180 + np.pi/2)*ENGINETHRUST
                self.velx = np.cos(self.angle*np.pi/180 + np.pi/2)*ENGINETHRUST
                self.fuel -= 0.1
                return True
            else:
                self.engine = 'off'
        else:
            self.engine = 'off'

    def image_direction(self):
        """
        Changes the direction of the player sprite image.
        """
        if self.engine == 'off':
            self.image = self.rocket1image
            self.image = pygame.transform.rotate(self.image, self.angle)
        if self.engine == 'on':
            self.image = self.rocket2image
            self.image = pygame.transform.rotate(self.image, self.angle)

        

    def update(self, collide, bullet_sprites):
        """
        Updates the state of the player sprite image.\n
            bullet_sprites -> pygame sprite group
        """
        self.image_direction()
        controls = self.controls(bullet_sprites)
        if self.engine == 'off':
            self.vely += GRAVITY
        self.rect.x += self.velx
        self.rect.y += self.vely

        for player in collide:
            barrel = collide[player][0]
            player.fuel = barrel.fuel_amount


        fuel_text = win_text.render('Fuel: %.1f'%self.fuel, False, GRAY)
        points_text = win_text.render('Points: %.1f'%self.points, False, GRAY)

        SCREEN.blit(fuel_text,(self.fuelinfo_x, self.fuelinfo_y))
        SCREEN.blit(points_text,(self.pointsinfo_x, self.pointsinfo_y))




class Player2(Player1):
    """This is the class for the second player"""
    def __init__(self):
        Player1.__init__(self)
        self.rect.center = (WIDTH_SCREEN - WIDTH_SCREEN/4, HEIGHT_SCREEN/4)
        self.fuelinfo_x = WIDTH_SCREEN-250
        self.fuelinfo_y = 50
        self.pointsinfo_x = WIDTH_SCREEN-250
        self.pointsinfo_y = 100


    def reset(self):
        """Reset player stats and withdraw points"""
        self.points -= 1
        self.velx = 0
        self.vely = 0
        self.angle = 0
        self.engine = 'off'
        self.fuel = PLAYER_START_FUEL
        self.rect.center = (WIDTH_SCREEN - WIDTH_SCREEN/4, HEIGHT_SCREEN/4)

    def controls(self, bullet_sprites):
        """
        Controls for the player see --> PLAYER2 controls in config.\n
            bullet_sprites -> pygame sprite group
        """
        # Controls
        keys = pygame.key.get_pressed()
        if keys[eval(f'pygame.K_{PLAYER_2_LEFT_MOVEMENT}')]:
            self.angle += 2

        if keys[eval(f'pygame.K_{PLAYER_2_RIGHT_MOVEMENT}')]:
            self.angle -= 2

        if keys[eval(f'pygame.K_{PLAYER_2_FIRE}')]:
            bullet_sprites.add(Bullets(self))

        if keys[eval(f'pygame.K_{PLAYER_2_BOOST}')]:
            if self.fuel > 0:
                self.engine = 'on'
                self.vely = -np.sin(self.angle*np.pi/180 + np.pi/2)*ENGINETHRUST
                self.velx = np.cos(self.angle*np.pi/180 + np.pi/2)*ENGINETHRUST
                self.fuel -= 0.1
                return True
            else:
                self.engine = 'off'
        else:
            self.engine = 'off'
