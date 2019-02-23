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
BLACK = (0, 0, 0)

# Clock/Timers
clock = pygame.time.Clock() # Initiate clock object



#BOIDS SETTINGS
#############################
BOIDS_RADIUS = 2
BOID_DISTANCE_FLOCKING_RADIUS = 200
BOIDS_AVOID_CRASH_DISTANCE = 10
BOIDS_COHESIAN_RADIUS = 40
BOID_AVOID_HAWK_MAGNITUDE = 1


#MOVING OBJECT SETTINGS
################################
MOVEMENT_MAGNITUDE = 2
MOVING_OBJECT_RADIUS = 2
MAX_NOISE_SPEED_X = 25
MAX_NOISE_SPEED_Y = 25
WALL_REFLECT = -0.2


# HAWK SETTINGS
##############################
HAWK_ATTACK_SPEED_MULTIPLIER = 3
HAWK_RADIUS_START_VALUE = 2
HAWK_TRIGGER_BOID_DISTANCE = 40


#OBSTACLE SETTTINGS
#############################
OBSTACLE_WIDTH = 40
OBSTACLE_HEIGHT = 40
OBSTACLE_BORDER_THICKNESS = 0 # 0 to fill it
WALL_DISTANCE_AVOID_VALUE = 65