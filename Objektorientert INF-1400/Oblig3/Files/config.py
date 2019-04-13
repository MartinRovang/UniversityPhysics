"""
 ▄████▄   ▒█████   ███▄    █   █████▒██▓  ▄████      █████▒██▓ ██▓    ▓█████ 
▒██▀ ▀█  ▒██▒  ██▒ ██ ▀█   █ ▓██   ▒▓██▒ ██▒ ▀█▒   ▓██   ▒▓██▒▓██▒    ▓█   ▀ 
▒▓█    ▄ ▒██░  ██▒▓██  ▀█ ██▒▒████ ░▒██▒▒██░▄▄▄░   ▒████ ░▒██▒▒██░    ▒███   
▒▓▓▄ ▄██▒▒██   ██░▓██▒  ▐▌██▒░▓█▒  ░░██░░▓█  ██▓   ░▓█▒  ░░██░▒██░    ▒▓█  ▄ 
▒ ▓███▀ ░░ ████▓▒░▒██░   ▓██░░▒█░   ░██░░▒▓███▀▒   ░▒█░   ░██░░██████▒░▒████▒
░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒  ▒ ░   ░▓   ░▒   ▒     ▒ ░   ░▓  ░ ▒░▓  ░░░ ▒░ ░
  ░  ▒     ░ ▒ ▒░ ░ ░░   ░ ▒░ ░      ▒ ░  ░   ░     ░      ▒ ░░ ░ ▒  ░ ░ ░  ░
░        ░ ░ ░ ▒     ░   ░ ░  ░ ░    ▒ ░░ ░   ░     ░ ░    ▒ ░  ░ ░      ░   
░ ░          ░ ░           ░         ░        ░            ░      ░  ░   ░  ░
░                                                                            

Contains the config file, here you can do changes to the game by altering the values.
"""



import pygame
# from win32api import GetSystemMetrics

# WIDTH_SCREEN = GetSystemMetrics(0)
# HEIGHT_SCREEN = GetSystemMetrics(0)

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
WIDTH_SCREEN = 1582 # Because i have chosen a background i would recommend not to change the width or height of the screen.
HEIGHT_SCREEN = 654
SCREENSIZE = (WIDTH_SCREEN, HEIGHT_SCREEN)
SCREEN = pygame.display.set_mode(SCREENSIZE)


# FONTS
pygame.font.init() # module for adding text
win_text = pygame.font.SysFont('Comic Sans MS', 30)


# PLAYER GENERAL SETTINGS
##########################################
ENGINETHRUST = 3
PLAYER_START_FUEL = 120

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
GRAVITY = 0.1
FUEL_TIMER = 40


# FUEL SETTINGS
#########################################
FUEL_AMOUNT = 120

# BULLET SETTINGS
#########################################
BULLET_SPEED = 20




