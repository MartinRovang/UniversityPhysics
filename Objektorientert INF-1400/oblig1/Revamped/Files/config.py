import pygame


# SCREEN
#######################################
# Set gamescreen size
WIDTH_SCREEN = 800
HEIGHT_SCREEN = 800
SCREENSIZE = (WIDTH_SCREEN, HEIGHT_SCREEN)
# Initialize pygame
pygame.init()
# set the pygame window name 
pygame.display.set_caption('Breakout') 
# Set screen object
SCREEN = pygame.display.set_mode(SCREENSIZE)
# FONTS
###########################################
pygame.font.init() # module for adding text
win_text = pygame.font.SysFont('Comic Sans MS', 30)


# GENERAL SETTINGS
###########################################


# COLORS
RED =   (255,   0,   0)
GREEN = (  0, 255,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GRAY = (240, 248, 255)






# BALL SETTINGS
##########################################
BALL_SPEED = 900
BALL_START_POS_X = 250
BALL_START_POS_Y = 350
BALL_RADIUS = 5


# BRICKS SETTINGS
##########################################
BRICKS_HEIGHT 



# PLATFORM SETTINGS
##########################################
BALL_SPEED = 900
BALL_START_POS_X = 250
BALL_START_POS_Y = 350
BALL_RADIUS = 5