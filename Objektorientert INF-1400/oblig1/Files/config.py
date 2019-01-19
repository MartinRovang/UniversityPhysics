import pygame
import pygame.display


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
screen = pygame.display.set_mode(SCREENSIZE)
# FONTS
###########################################
pygame.font.init() # module for adding text
win_text = pygame.font.SysFont('Comic Sans MS', 30)


# General settings
###############################################################
# Load background music
pygame.mixer.music.load('lannis.ogg')
pygame.mixer.music.play(loops = 10, start = 40)


# COLORS
#--------------------------------------
RED =   (255,   0,   0)
GREEN = (  0, 255,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREY = (240,248,255)

# Timer
clock = pygame.time.Clock() # Initiate clock object
TIME_PASSED = clock.tick(60)
TIME_PASSED_SECONDS = TIME_PASSED/1000.0




# BALL SETTINGS
##########################################
BALL_SPEED = 900
BALL_START_POS_X = 250
BALL_START_POS_Y = 250




# PLATFORM SETTINGS
#########################################
PLATFORM_SPEED = 500