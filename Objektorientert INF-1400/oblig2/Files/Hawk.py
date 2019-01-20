
import pygame
from math import cos, sin, radians, sqrt
from Files.config import *
from Files.Boid import Boid
import random
import numpy as np

class Hawk(Boid):

    def __init__(self, x , y):
        super().__init__(x, y)
        self.radius = HAWK_RADIUS_START_VALUE
        self.nomsound = pygame.mixer.Sound('nomnom.ogg')
    def attack(self, boids):
        min_distance = 1000
        for boid in boids:
            distance = sqrt((boid.x-self.x)**2 + (boid.y-self.y)**2)
            if distance < min_distance:
                min_distance = distance
                x = boid.x 
                y = boid.y
                meanx = boid.velx
                meany = boid.vely
            if distance < self.radius:
                boids.remove(boid)
                #self.radius += 1
                pygame.mixer.Sound.play(self.nomsound)

        if len(boids) > 0:
            self.velx = ((x-self.x)/np.sqrt((x-self.x)**2 + (y-self.y)**2))*HAWK_ATTACK_SPEED_MULTIPLIER
            self.vely = ((y-self.y)/np.sqrt((x-self.x)**2 + (y-self.y)**2))*HAWK_ATTACK_SPEED_MULTIPLIER

    
    def avoid_obstacles(self, obstacles):
        for obstacle in obstacles:
            if self.x+self.radius > obstacle.x and self.x-self.radius < obstacle.x+OBSTACLE_WIDTH\
             and self.y+self.radius > obstacle.y and self.y-self.radius < obstacle.y+OBSTACLE_HEIGHT:
                
                if self.x+self.radius > obstacle.x and self.x-self.radius < obstacle.x+OBSTACLE_WIDTH:
            
                    if self.velx > 0:
                        self.x -= 10
                    if self.vely < 0:
                        self.x += 10

                if self.y+self.radius > obstacle.y and self.y-self.radius < obstacle.y+OBSTACLE_HEIGHT:

                    if self.vely > 0:
                        self.y -= 10
                    if self.vely < 0:
                        self.y += 10


    def draw(self):
        pygame.draw.circle(SCREEN, RED, [int(self.x), int(self.y)], self.radius)




