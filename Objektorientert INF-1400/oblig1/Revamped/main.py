#################################################
#
#
#               BREAKOUT-CLONE
#            MANDATORY ASSIGNMENT 1
#             MARTIN SORIA RØVANG
#
#
##################################################



import pygame
from Files.Objects import Ball, Platform, Bricks
from Files.config import *
import time
import matplotlib.pyplot as plt


def Event():
    """Runs the event so that you can press the X in the window and close the game."""
    # Closing the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()



def FPS_CHECK(time1, frames):
    """Prints out the FPS"""

    time2 = time.clock()
    if (time2 - time1) > 1:
        print('FPS', frames)
        frames = 0
        time1 = time.clock()
        return time1, frames
    else:
        frames += 1
        return time1, frames



def main():
    """Runs the overall gameloop"""
    # Initiate clock object
    clock = pygame.time.Clock()

    # Initialize pygame
    pygame.init()

    # set the pygame window name 
    pygame.display.set_caption('Breakout') 

    # FONTS
    pygame.font.init() # module for adding text
    win_text = pygame.font.SysFont('Comic Sans MS', 30)

    # Initiate the objects used in the game
    Game_ball = Ball()
    Player = Platform()
    # Spawns bricks on top of screen
    Bricks.initiate_bricks(AMOUNT_OF_BRICKS)

    # Set start value to playing
    Game = 'Playing'

    # Make timer and frames for FPS
    time1 = time.clock()
    frames = 0

    # Start the playing game loop
    while Game == 'Playing':
        Event()

        # Limit to 60FPS this is to contain the speed of the ball on all computers (unless their FPS will stagnate below 60)
        TIME_PASSED = clock.tick(60)
        # Time in seconds
        TIME_PASSED_SECONDS = TIME_PASSED/1000.0

        Game_ball.move()
        Player.move()
        Game_ball.check_platform_collision(Player)
        Lost_check = Game_ball.check_wall_collisions()
        Bricks.update_bricks(Game_ball)

    
        # Update screen
        SCREEN.fill(BLACK)
        for bricks in Bricks.bricks_list:
            bricks.draw()

        # Draw objects to screen
        Game_ball.draw()
        Player.draw()
        pygame.display.update()

        # Check if won on lost game.
        if len(Bricks.bricks_list) == 0:
            Game = 'Won'

        if Lost_check:
            Game = 'Lost'

        # FPS logic
        time1, frames = FPS_CHECK(time1, frames)

        
    # Print text on screen if won
    while Game == 'Won':
        Event()
        won_text = win_text.render('You won!', False, GRAY)
        SCREEN.blit(won_text,(600,700))
        pygame.display.update()
    
    # Print text on screen if lost
    while Game == 'Lost':
        Event()
        lost_text = win_text.render('You Lost!', False, GRAY)
        SCREEN.blit(lost_text,(600,700))
        pygame.display.update()



# Only run code if run without being imported
if __name__ == "__main__":
    main()