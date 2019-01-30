import pygame


# SCREEN
#######################################
# Set gamescreen size
WIDTH_SCREEN = 800
HEIGHT_SCREEN = 800
SCREENSIZE = (WIDTH_SCREEN, HEIGHT_SCREEN)
screen = pygame.display.set_mode(SCREENSIZE)




# GENERAL SETTINGS
###########################################


# COLORS
RED =   (255,   0,   0)
GREEN = (  0, 255,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREY = (240,248,255)

# # Timer
clock = pygame.time.Clock() # Initiate clock object
# TIME_PASSED = clock.tick(60)
# TIME_PASSED_SECONDS = TIME_PASSED/1000.0




# BALL SETTINGS
##########################################
BALL_SPEED = 700
BALL_START_POS_X = 250
BALL_START_POS_Y = 350
BALL_RADIUS = 5




# PLATFORM SETTINGS
#########################################
PLATFORM_SPEED = 500
ANGLE_MAGNITUDE = 2


# BRICKS SETTINGS
#########################################
YDISTANCE_BETWEEN_BLOCKS = 70
XSHIFT_BLOCKS = 10
XDISTANCE_BETWEEN_BLOCKS = 50
NUMBER_OF_BLOCK_HORIZONTAL = 15
YSHIFT_BLOCKS = 37

