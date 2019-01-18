from os import environ
import pygame
import numpy as np
import math
from Files import Boid, Obstacle
from Files.config import *



def sim_loop():
    # Initiate boids list to containt the boids
    boids_list = []
    obstacle_list = []
    while True:

        
        # Get mouse position
        x, y = pygame.mouse.get_pos()

        #Checks for events and if pressed the X in the corner the program will quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    obstacle_list.append(Obstacle(x, y))
                
            
        # Make boids
        if pygame.mouse.get_pressed()[0] == 1:
            boids_list.append(Boid(x, y))
        

        # Screen updates
        SCREEN.fill((0,0,0))



    
        for i in boids_list:
            i.noisy_movement()
            i.avoid_crash(boids_list)
            i.flocking(boids_list)
            i.crash_wall_check()
            i.avoid_obstacles(obstacle_list)
            i.draw()

        for i in obstacle_list:
            i.draw()
        
        pygame.display.update()






if __name__ == "__main__":
    sim_loop()