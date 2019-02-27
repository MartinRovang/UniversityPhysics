#################################################
#
#
#       CONFIG FILE FOR MAYHEM-CLONE
#            MANDATORY ASSIGNMENT 3
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
# OTHER
FPS = 60


# SCREEN
#######################################
# Set gamescreen size
WIDTH_SCREEN = 1582
HEIGHT_SCREEN = 654
SCREENSIZE = (WIDTH_SCREEN, HEIGHT_SCREEN)
SCREEN = pygame.display.set_mode(SCREENSIZE)


# FONTS
pygame.font.init() # module for adding text
win_text = pygame.font.SysFont('Comic Sans MS', 30)


# PLAYER GENERAL SETTINGS
##########################################
SPEED = 5
PLAYER_START_FUEL = 100

# PLAYER1 SETTINGS
##########################################
PLAYER_1_LEFT_MOVEMENT = 'a'
PLAYER_1_RIGHT_MOVEMENT = 'd'
PLAYER_1_FIRE = 'e'
PLAYER_1_BOOST = 'w'

# PLAYER2 SETTINGS
##########################################
PLAYER_2_LEFT_MOVEMENT = 'LEFT'
PLAYER_2_RIGHT_MOVEMENT = 'RIGHT'
PLAYER_2_FIRE = 'SPACE'
PLAYER_2_BOOST = 'UP'


# WORLD SETTINGS
#########################################
GRAVITY = 0.5
FUEL_TIMER = 40


# FUEL SETTINGS
#########################################
FUEL_AMOUNT = 100

# BULLET SETTINGS
#########################################
BULLET_SPEED = 20

# # PLATFORM SETTINGS
# ##########################################
# PLATFORM_SPEED = 600
# PLATFORM_START_POS_X = 200
# PLATFORM_START_POS_Y = 700
# PLATFORM_WIDTH = 100
# PLATFORM_HEIGHT = 15
# ANGLE_MAGNITUDE = 5


