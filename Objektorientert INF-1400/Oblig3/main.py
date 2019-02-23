
import pygame
import numpy as np
from Files.config import *
from Files import Player1, Player2, FuelBarrel, Wall
import os
import time

#Game folder
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
Background = pygame.image.load(os.path.join('Files', img_folder, 'background.jpg'))


# Clock/Timers
clock = pygame.time.Clock() # Initiate clock object


def point_assigner_loss(group):
    if group != {}:
        for player in group:
            points = player.points
            newplayer = type(player)()
            newplayer.points = points - 1
            player_sprites.add(newplayer)


def point_assigner_win(group):
    if group != {}:
        for player in player_sprites:
            player.points += 1
            
class Game:
    pass

fuel_sprites = pygame.sprite.Group()
player_sprites = pygame.sprite.Group()
bullet_sprites = pygame.sprite.Group()
wall_sprites = pygame.sprite.Group()

player1 = Player1()
player2 = Player2()

player_sprites.add(player1, player2)

L_wall = Wall(5, HEIGHT_SCREEN/2, 10, HEIGHT_SCREEN)
R_wall = Wall(WIDTH_SCREEN-5, HEIGHT_SCREEN/2, 10, HEIGHT_SCREEN)
T_wall = Wall(WIDTH_SCREEN/2, 5, WIDTH_SCREEN, 10)
B_wall = Wall(WIDTH_SCREEN/2,HEIGHT_SCREEN-5, WIDTH_SCREEN, 10)
Mid_wall = Wall(WIDTH_SCREEN/2,HEIGHT_SCREEN/2, 10, HEIGHT_SCREEN/4)
wall_sprites.add(L_wall, R_wall, T_wall, B_wall, Mid_wall)


fueltimer = time.time()
while True:
    #Checks for events and if pressed the X in the corner the program will quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    time_passed = clock.tick(60)
    time_passed_seconds = time_passed/1000.0
    
    timer = time.time()
    if fueltimer < timer:
        fueltimer += 40
        fuel_sprites.add(FuelBarrel())



    SCREEN.blit(Background, (0, 0))
    collide = pygame.sprite.groupcollide(player_sprites, fuel_sprites, 0 , 1)
    collide_wall = pygame.sprite.groupcollide(player_sprites, wall_sprites, 1 , 0)
    collide_wall_bullets = pygame.sprite.groupcollide(bullet_sprites, wall_sprites, 1 , 0)
    collide_players_bullets = pygame.sprite.groupcollide(player_sprites, bullet_sprites ,1 , 1)
    collide_players_players = pygame.sprite.groupcollide(player_sprites, player_sprites ,0 , 0)

    for player in collide_players_players:
        if player != collide_players_players[player][0]:
            pygame.sprite.groupcollide(player_sprites, player_sprites ,1 , 1)
            point_assigner_loss(collide_players_players)
            

    point_assigner_loss(collide_wall)
    point_assigner_win(collide_players_bullets)
    point_assigner_loss(collide_players_bullets)

    player_sprites.update(collide, bullet_sprites)
    player_sprites.draw(SCREEN)
    fuel_sprites.update()
    fuel_sprites.draw(SCREEN)
    bullet_sprites.update()
    bullet_sprites.draw(SCREEN)
    wall_sprites.update()
    wall_sprites.draw(SCREEN)

    pygame.display.update()




# if __name__ == "__main__":
#     pass




