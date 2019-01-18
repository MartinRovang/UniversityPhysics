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
###############################################################

# COLORS
RED =   (255,   0,   0)
GREEN = (  0, 255,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREY = (240,248,255)

# TIMERS
clock = pygame.time.Clock() # Initiate clock object
# Limit to 60FPS this is to contain the speed of the ball on all computers (unless their FPS will stagnate below 60)
TIME_PASSED = clock.tick(60)
# Time in seconds
TIME_PASSED_SECONDS = TIME_PASSED/1000.0



#BOIDS SETTINGS
#############################
BOID_DISTANCE_FLOCKING_RADIUS = 100
BOID_VARIANCE_NOISY_X = 50
BOID_VARIANCE_NOISY_Y = 50
BOID_MEAN_NOISY_X = 0
BOID_MEAN_NOISY_Y = 0
BOIDS_AVOID_CRASH_DISTANCE = 15



#MOVING OBJECT SETTINGS
################################
MOVING_OBJECT_RADIUS = 5


#OBSTACLE SETTTINGS
#############################
OBSTACLE_WIDTH = 80
OBSTACLE_HEIGHT = 80