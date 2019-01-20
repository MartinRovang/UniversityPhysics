from os import environ
import pygame
import numpy as np
import math
from Files import Boid, Obstacle, Hawk
from Files.config import *



def sim_loop():
    # Initiate boids list to containt the boids
    boids_list = []
    hawk_list = []
    obstacle_list = []
    while True:

        
        # Get mouse position
        x, y = pygame.mouse.get_pos()

        #Checks for events and if pressed the X in the corner the program will quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            # Make obstacle
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    obstacle_list.append(Obstacle(x, y))

            # Make hawks
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    hawk_list.append(Hawk(x, y))

        # Limit to 60FPS this is to contain the speed of the ball on all computers (unless their FPS will stagnate below 60)
        TIME_PASSED = clock.tick(60)
        # Time in seconds
        TIME_PASSED_SECONDS = TIME_PASSED/1000.0
                
            
        # Make boids
        if pygame.mouse.get_pressed()[0] == 1:
            boids_list.append(Boid(x, y))
        
        # Remove old drawings / fill with black
        SCREEN.fill((0,0,0))
        # Make all actions
        for i in boids_list:
            i.noisy_movement(TIME_PASSED_SECONDS)
            i.avoid_hawk(hawk_list)
            i.move(TIME_PASSED_SECONDS)
            i.flocking(boids_list)
            i.avoid_crash(boids_list)
            i.match_speed(boids_list)
            i.crash_wall_check(TIME_PASSED_SECONDS)
            i.draw()

        for i in obstacle_list:
            i.avoid_obstacles(boids_list)
            i.avoid_obstacles(hawk_list)
            i.draw()

        for i in hawk_list:
            i.noisy_movement(TIME_PASSED_SECONDS)
            i.move(TIME_PASSED_SECONDS)
            i.flocking(hawk_list)
            i.match_speed(hawk_list)
            i.crash_wall_check(TIME_PASSED_SECONDS)
            i.attack(boids_list)
            i.avoid_crash(hawk_list)
            i.draw()
        
        # Draw new placements
        pygame.display.update()






if __name__ == "__main__":
    sim_loop()