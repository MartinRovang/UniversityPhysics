import pygame
import os
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
BLACK = (0, 0, 0)


#Game folder

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')

# Clock/Timers
clock = pygame.time.Clock() # Initiate clock object



# class SpriteSheet():
#     def __init__(self, cols, rows):
#         self.sheet = pygame.image.load(os.path.join(img_folder, 'spritetest.png')).convert_alpha()
#         self.cols = cols
#         self.rows = rows
#         self.total_cell_count = cols * rows
#         self.rect = self.sheet.get_rect()
#         self.cells = [(0 + i*self.rect.width/2, 0, self.rect.width/self.total_cell_count + i*self.rect.width/self.total_cell_count, self.rect.height) for i in range(self.total_cell_count)]

    

#     def draw(self, i):
#         # change = (0, 0, x, y)
#         SCREEN.blit(self.sheet, (50, 50), self.cells[i])



class Player(pygame.sprite.Sprite):
    # Sprite for the player
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.rect((50, 50))
        self.image = pygame.image.load(os.path.join(img_folder, 'test.png')).convert_alpha()
        #self.image.set_colorkey(BLACK)
        # self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH_SCREEN/2, HEIGHT_SCREEN/2)


    def update(self, time_passed_seconds):
        self.rect.x += np.ceil(50*time_passed_seconds)
        self.rect.y += np.ceil(20*time_passed_seconds)



all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

while True:
    #Checks for events and if pressed the X in the corner the program will quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    time_passed = clock.tick(60)
    time_passed_seconds = time_passed/1000.0


    SCREEN.fill(BLACK)
    all_sprites.update(time_passed_seconds)
    all_sprites.draw(SCREEN)
    pygame.display.update()


# S = SpriteSheet(2, 1)
# i = 0
# while True:
#     #Checks for events and if pressed the X in the corner the program will quit
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
    
#     time_passed = clock.tick(1)
#     time_passed_seconds = time_passed/1000.0



#     SCREEN.fill(BLACK)

#     if i < (len(S.cells)-1):
#         i += 1
#     else:
#         i = 0
        
#     S.draw(i)

#     pygame.display.update()