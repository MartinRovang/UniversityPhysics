import pygame



# SCREEN
#######################################
# Set gamescreen size
WIDTH_SCREEN = 800
HEIGHT_SCREEN = 800
SCREENSIZE = (WIDTH_SCREEN, HEIGHT_SCREEN)
# Initialize pygame
pygame.init()
# Set the pygame window name 
pygame.display.set_caption('Boids Sim') 
# Set screen object
SCREEN = pygame.display.set_mode(SCREENSIZE)


# FONTS
###########################################
pygame.font.init() # module for adding text
win_text = pygame.font.SysFont('Comic Sans MS', 30)


# GENERAL SETTINGS
###############################################################

# COLORS
RED =   (255,   0,   0)
GREEN = (  0, 255,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GRAY = (240, 248, 255)

# Clock/Timers
clock = pygame.time.Clock() # Initiate clock object



#BOIDS SETTINGS
#############################
BOIDS_RADIUS = 5
BOID_DISTANCE_FLOCKING_RADIUS = 70
BOIDS_AVOID_CRASH_DISTANCE = 5


#MOVING OBJECT SETTINGS
################################
MOVEMENT_MAGNITUDE = 100
MOVING_OBJECT_RADIUS = 2
MAX_NOISE_SPEED_X = 25
MAX_NOISE_SPEED_Y = 25



# HAWK SETTINGS
##############################


#OBSTACLE SETTTINGS
#############################
