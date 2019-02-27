
import pygame
import numpy as np
from Files.config import *
from Files import Player1, Player2, FuelBarrel, Wall
import os
import time


class Game:
    """
    Starts the game when instancing.
    """
    def __init__(self):
        """Starts the gameloop when initiated."""
        self.gameloop()


    def background(self, Background):
        SCREEN.blit(Background, (0, 0))

    def point_assigner_loss(self, group, player_sprites):
        """
        Assigns loss points to the player if collision has happened and respawn them.
        """
        if group != {}:
            for player in group:
                points = player.points
                newplayer = type(player)()
                newplayer.points = points - 1
                player_sprites.add(newplayer)


    def point_assigner_win(self, group, player_sprites):
        """
        Assigns win points to the player if player collide with bullet.
        """
        if group != {}:
            for player in player_sprites:
                player.points += 1

    def gameloop(self):
        """The game loop"""

        #Game folder
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, 'img')
        Background = pygame.image.load(os.path.join('Files', img_folder, 'background.jpg'))

        # Clock/Timers
        clock = pygame.time.Clock() # Initiate clock object                

        # Assign object sprite groups.
        fuel_sprites = pygame.sprite.Group()
        player_sprites = pygame.sprite.Group()
        bullet_sprites = pygame.sprite.Group()
        wall_sprites = pygame.sprite.Group()

        # Instancing players.
        player1 = Player1()
        player2 = Player2()

        # Instancing walls
        L_wall = Wall(5, HEIGHT_SCREEN/2, 10, HEIGHT_SCREEN)
        R_wall = Wall(WIDTH_SCREEN-5, HEIGHT_SCREEN/2, 10, HEIGHT_SCREEN)
        T_wall = Wall(WIDTH_SCREEN/2, 5, WIDTH_SCREEN, 10)
        B_wall = Wall(WIDTH_SCREEN/2,HEIGHT_SCREEN-5, WIDTH_SCREEN, 10)
        Mid_wall = Wall(WIDTH_SCREEN/2,HEIGHT_SCREEN/2, 10, HEIGHT_SCREEN/4)
        
        # add to sprite groups
        player_sprites.add(player1, player2)
        wall_sprites.add(L_wall, R_wall, T_wall, B_wall, Mid_wall)

        # Initiate timer for the fuel spawn
        fueltimer = time.time()

        # Start the loop
        while True:
            #Checks for events and if pressed the X in the corner the program will quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            
            # Lock fps
            time_passed = clock.tick(FPS)
            time_passed_seconds = time_passed/1000.0
            
            # Spawn fuel barrels
            timer = time.time()
            if fueltimer < timer:
                fueltimer += FUEL_TIMER
                fuel_sprites.add(FuelBarrel())


            # Set background
            self.background(Background)

            # Check for collisions between sprites.
            collide = pygame.sprite.groupcollide(player_sprites, fuel_sprites, 0 , 1)
            collide_wall = pygame.sprite.groupcollide(player_sprites, wall_sprites, 1 , 0)
            collide_wall_bullets = pygame.sprite.groupcollide(bullet_sprites, wall_sprites, 1 , 0)
            collide_players_bullets = pygame.sprite.groupcollide(player_sprites, bullet_sprites ,1 , 1)
            collide_players_players = pygame.sprite.groupcollide(player_sprites, player_sprites ,0 , 0)

            # Assign negative points to both players if colliding
            for player in collide_players_players:
                if player != collide_players_players[player][0]:
                    pygame.sprite.groupcollide(player_sprites, player_sprites ,1 , 1)
                    self.point_assigner_loss(collide_players_players, player_sprites)
                    
            # Assign negative points for wall collision and if hit by player bullets
            self.point_assigner_loss(collide_wall, player_sprites)
            self.point_assigner_loss(collide_players_bullets, player_sprites)

            # Assign Positive points to player which hit the other player
            self.point_assigner_win(collide_players_bullets, player_sprites)

            # Update all the sprites
            player_sprites.update(collide, bullet_sprites)
            player_sprites.draw(SCREEN)
            fuel_sprites.update()
            fuel_sprites.draw(SCREEN)
            bullet_sprites.update()
            bullet_sprites.draw(SCREEN)
            wall_sprites.update()
            wall_sprites.draw(SCREEN)
            
            # Update screen
            pygame.display.update()




if __name__ == "__main__":
    Game()




