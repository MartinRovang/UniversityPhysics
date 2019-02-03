from os import environ
import pygame
import numpy as np
import math
from Files import Boid, Obstacle, Hawk
from Files.config import *



def sim_loop():
    """This is the gameloop and will run until you exit the program"""

    # Initiate boids list to containt the boids
    boids_list = []
    hawk_list = []
    obstacle_list = []
    wall_lock = 0
    
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
            
            # Disable/enable walls
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    if wall_lock == 0:
                        wall_lock = 1
                    else:
                        wall_lock = 0


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
            i.noisy_movement()
            i.avoid_hawk(hawk_list)
            i.move()
            i.flocking(boids_list)
            i.avoid_crash(boids_list)
            i.match_speed(boids_list)
            i.crash_wall_check(wall_lock)
            i.draw()

        for i in obstacle_list:
            i.avoid_obstacles(boids_list)
            i.avoid_obstacles(hawk_list)
            i.draw()

        for i in hawk_list:
            i.noisy_movement()
            i.move()
            i.flocking(hawk_list)
            i.match_speed(hawk_list)
            i.crash_wall_check(wall_lock)
            i.attack(boids_list)
            i.avoid_crash(hawk_list)
            i.draw()

        # render text if walls are disabled
        if wall_lock == 1:
            wall_text = win_text.render('Walls disabled', False, RED)
            SCREEN.blit(wall_text,(0,700))
        # Draw new placements
        pygame.display.update()






if __name__ == "__main__":
    sim_loop()