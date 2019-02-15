from os import environ
import pygame
import numpy as np
import math
from Files import Boid, Obstacle, Hawk
from Files.config import *


class Simulation:
    def __init__(self):
        self.boids_list = []
        self.hawk_list = []
        self.obstacle_list = []
        self.simloop()


    def reset_screen(self):
        SCREEN.fill((0, 0, 0))

    def spawn_boids(self):
        if pygame.mouse.get_pressed()[0] == 1:
            # Get mouse position
            x, y = pygame.mouse.get_pos()
            # Add boids to list
            self.boids_list.append(Boid(x, y))


    def simloop(self):
        """This is the gameloop and will run until you exit the program"""

        # Initiate boids list to containt the boids
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
                        self.obstacle_list.append(Obstacle(x, y))

                # Make hawks
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        self.hawk_list.append(Hawk(x, y))
                
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
            self.spawn_boids()
            
            # Remove old drawings / fill with black
            self.reset_screen()

            # Make all actions
            for i in self.boids_list:
                i.noisy_movement()
                i.avoid_hawk(self.hawk_list)
                i.move(TIME_PASSED_SECONDS)
                i.flocking(self.boids_list)
                i.avoid_crash(self.boids_list)
                i.match_speed(self.boids_list)
                i.crash_wall_check(wall_lock)
                i.draw()

            for i in self.obstacle_list:
                i.avoid_obstacles(self.boids_list)
                i.avoid_obstacles(self.hawk_list)
                i.draw()

            for i in self.hawk_list:
                i.noisy_movement()
                i.move(TIME_PASSED_SECONDS)
                i.flocking(self.hawk_list)
                i.match_speed(self.hawk_list)
                i.crash_wall_check(wall_lock)
                i.attack(self.boids_list)
                i.avoid_crash(self.hawk_list)
                i.draw()

            # render text if walls are disabled
            if wall_lock == 1:
                wall_text = win_text.render('Walls disabled', False, RED)
                SCREEN.blit(wall_text,(0,700))
            # Draw new placements
            pygame.display.update()


if __name__ == "__main__":
    Simulation()