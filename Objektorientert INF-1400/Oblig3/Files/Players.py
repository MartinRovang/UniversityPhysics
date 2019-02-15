import pygame
from Files.config import *
from Files.Bullets import Bullets
from math import sqrt, cos
import numpy as np
import os

#Game folder
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')


class Player1(pygame.sprite.Sprite):
    # Sprite for the player
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.velx = 0
        self.vely = 0
        self.angle = 0
        self.engine = 'off'
        self.fuel = 100
        self.points = 0
        self.image = pygame.image.load(os.path.join(img_folder, 'rocket1.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH_SCREEN/4, HEIGHT_SCREEN/4)


    def controls(self, bullet_sprites):
        """Moves the platform"""
        # Controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.angle += 2
            self.velx = np.cos(self.angle*np.pi/180 + np.pi/2)*SPEED

        if keys[pygame.K_d]:
            self.angle -= 2
            self.velx = np.cos(self.angle*np.pi/180 + np.pi/2)*SPEED

        if keys[pygame.K_e]:
            bullet_sprites.add(Bullets(self))

        if keys[pygame.K_w]:
            if self.fuel > 0:
                self.engine = 'on'
                self.vely = -np.sin(self.angle*np.pi/180 + np.pi/2)*SPEED + GRAVITY
                self.fuel -= 0.1
                return True
            else:
                self.engine = 'off'
        else:
            self.engine = 'off'


    def image_direction(self):
        if self.engine == 'off':
            self.image = pygame.image.load(os.path.join(img_folder, 'rocket1.png')).convert_alpha()
            self.image = pygame.transform.rotate(self.image, self.angle)
        if self.engine == 'on':
            self.image = pygame.image.load(os.path.join(img_folder, 'rocket2.png')).convert_alpha()
            self.image = pygame.transform.rotate(self.image, self.angle)

        

    def update(self, collide, bullet_sprites):
        self.image_direction()
        controls = self.controls(bullet_sprites)
        if self.engine == 'off':
            self.vely = GRAVITY

        self.rect.x += self.velx/np.sqrt(self.velx**2 + self.vely**2)*SPEED
        self.rect.y += self.vely/np.sqrt(self.velx**2 + self.vely**2)*SPEED

        for player in collide:
            barrel = collide[player][0]
            player.fuel = barrel.fuel_amount


        fuel_text = win_text.render('Fuel: %.1f'%self.fuel, False, GRAY)
        SCREEN.blit(fuel_text,(10,50))





class Player2(Player1):
    def __init__(self):
        Player1.__init__(self)
        self.rect.center = (WIDTH_SCREEN-200, HEIGHT_SCREEN-200)


    def controls(self, bullet_sprites):
        """Moves the platform"""
        # Controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.angle += 2
            self.velx = np.cos(self.angle*np.pi/180 + np.pi/2)*SPEED

        if keys[pygame.K_RIGHT]:
            self.angle -= 2
            self.velx = np.cos(self.angle*np.pi/180 + np.pi/2)*SPEED

        if keys[pygame.K_SPACE]:
            bullet_sprites.add(Bullets(self))

        if keys[pygame.K_UP]:
            if self.fuel > 0:
                self.engine = 'on'
                self.vely = -np.sin(self.angle*np.pi/180 + np.pi/2)*SPEED + GRAVITY
                self.fuel -= 0.1
                return True
            else:
                self.engine = 'off'
        else:
            self.engine = 'off'



    def update(self, collide, bullet_sprites):
        self.image_direction()
        controls = self.controls(bullet_sprites)
        if self.engine == 'off':
            self.vely = GRAVITY

        self.rect.x += self.velx/np.sqrt(self.velx**2 + self.vely**2)*SPEED
        self.rect.y += self.vely/np.sqrt(self.velx**2 + self.vely**2)*SPEED

        for player in collide:
            barrel = collide[player][0]
            player.fuel = barrel.fuel_amount
            

        fuel_text = win_text.render('Fuel: %.1f'%self.fuel, False, GRAY)
        SCREEN.blit(fuel_text,(WIDTH_SCREEN-250,50))