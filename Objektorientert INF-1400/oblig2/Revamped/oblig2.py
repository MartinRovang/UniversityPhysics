import pygame
import numpy as np
import math
from Files import Boid, Hawk, Obstacle
from Files.config import *


class Simulation():
    """Creates the simulation object and runs it."""
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



            # Limit to 60FPS this is to contain the speed of the ball on all computers (unless their FPS will stagnate below 60)
            TIME_PASSED = clock.tick(60)
            # Time in seconds
            TIME_PASSED_SECONDS = TIME_PASSED/1000.0
            self.spawn_boids()
            self.reset_screen()


            for boid in self.boids_list:
                boid.find_flock(self.boids_list)
                boid.rule1()
                boid.rule2()
                boid.rule3()
                boid.crash_wall_check()
                boid.avoid_hawk(self.hawk_list)
                boid.move()
                boid.draw()

            for hawk in self.hawk_list:
                hawk.find_flock(self.hawk_list)
                hawk.rule1()
                hawk.rule2()
                hawk.rule3()
                hawk.crash_wall_check()
                hawk.attack(self.boids_list)
                hawk.move()
                hawk.draw()


            for obstacle in self.obstacle_list:
                obstacle.avoid_obstacles(self.boids_list)
                obstacle.avoid_obstacles(self.hawk_list)
                obstacle.draw()

            # Draw new placements
            pygame.display.update()



if __name__ == "__main__":
    Simulation()