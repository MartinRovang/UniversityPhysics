
import pygame
import numpy as np


# SCREEN
#######################################
# Set gamescreen size
WIDTH_SCREEN = 800
HEIGHT_SCREEN = 800
SCREENSIZE = (WIDTH_SCREEN, HEIGHT_SCREEN)
# Initialize pygame
pygame.init()
# Set the pygame window name 
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

# Clock/Timers
clock = pygame.time.Clock() # Initiate clock object



theta  = 0

while True:

    
    # Get mouse position
    x, y = pygame.mouse.get_pos()

    #Checks for events and if pressed the X in the corner the program will quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    

    theta += 0.01

    X = np.array([[100], [100], [0]])
    ROTMAT = np.array([[np.cos(theta),-np.sin(theta), 0], [np.sin(theta), np.cos(theta), 0], [0 , 0 ,1]])
    TRANSMAT = np.array([[1, 0, x], [0, 1, y], [0 , 0 , 1]])

    Y = ROTMAT@X


    SCREEN.fill((0, 0, 0))
    pygame.draw.circle(SCREEN, RED, (Y[0]+x, Y[1]+y), 5,0)
    pygame.display.update()
