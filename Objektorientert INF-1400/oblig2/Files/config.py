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
GREY = (240,248,255)

# Clock/Timers
clock = pygame.time.Clock() # Initiate clock object



#BOIDS SETTINGS
#############################
BOID_DISTANCE_FLOCKING_RADIUS = 50
BOID_VARIANCE_NOISY_X = 1
BOID_VARIANCE_NOISY_Y = 1
BOID_VARIANCE_NOISY_X_ALERTED = 20
BOID_VARIANCE_NOISY_Y_ALERTED = 20
BOID_MEAN_NOISY_X = 0
BOID_MEAN_NOISY_Y = 0
BOID_MEAN_NOISY_X_ALERTED = 0
BOID_MEAN_NOISY_Y_ALERTED = 0
BOIDS_AVOID_CRASH_DISTANCE = 15
MOVEMENT_MAGNITUDE = 5



#MOVING OBJECT SETTINGS
################################
MOVING_OBJECT_RADIUS = 2



# HAWK SETTINGS
##############################
HAWK_ATTACK_SPEED_MULTIPLIER = 20
HAWK_RADIUS_START_VALUE = 5
HAWK_TRIGGER_BOID_DISTANCE = 30


#OBSTACLE SETTTINGS
#############################
OBSTACLE_WIDTH = 40
OBSTACLE_HEIGHT = 40
OBSTACLE_BORDER_THICKNESS = 0 # 0 to fill it