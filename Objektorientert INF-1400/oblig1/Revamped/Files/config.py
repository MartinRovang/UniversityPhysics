#################################################
#
#
#       CONFIG FILE FOR BREAKOUT-CLONE
#            MANDATORY ASSIGNMENT 1
#             MARTIN SORIA RØVANG
#
##################################################





import pygame




# GENERAL SETTINGS
###########################################
# COLORS
RED =   (255,   0,   0)
GREEN = (  0, 255,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GRAY = (240, 248, 255)
BLACK = (0, 0, 0)


# SCREEN
#######################################
# Set gamescreen size
WIDTH_SCREEN = 800
HEIGHT_SCREEN = 800
SCREENSIZE = (WIDTH_SCREEN, HEIGHT_SCREEN)
SCREEN = pygame.display.set_mode(SCREENSIZE)



# BALL SETTINGS
##########################################
BALL_SPEED = 800
BALL_START_POS_X = 250
BALL_START_POS_Y = 350
BALL_START_VELY = 10
BALL_START_VELX = 0
BALL_RADIUS = 10


# BRICKS SETTINGS
#########################################
YDISTANCE_BETWEEN_BLOCKS = 70
XSHIFT_BLOCKS = 50
XDISTANCE_BETWEEN_BLOCKS = 50
NUMBER_OF_BLOCK_HORIZONTAL = 13
YSHIFT_BLOCKS = 37
BRICKS_HEIGHT = 25
BRICKS_WIDTH = 50
AMOUNT_OF_BRICKS = 3



# PLATFORM SETTINGS
##########################################
PLATFORM_SPEED = 600
PLATFORM_START_POS_X = 200
PLATFORM_START_POS_Y = 700
PLATFORM_WIDTH = 100
PLATFORM_HEIGHT = 15
ANGLE_MAGNITUDE = 5


