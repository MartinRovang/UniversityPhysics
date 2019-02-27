
import pygame
from math import cos, sin, radians, sqrt
from Files.config import *
from Files.Boid import Boid
import random
import numpy as np

class Hawk(Boid):
    """
    Summary:
        When called creates a hawk/hoik object. Inherits from Boid class

    Args:
    x: x-position

    y: y-position 

    __init__:\n

    flock: list

    self.radius = HAWK_RADIUS_START_VALUE  | See config

    Methods:
    move(): Places the moving object according to its speed and magnitude.

    find_flock(boids): assigns boids to a boids flock.

    rule1(): Activates first rule of the boid, moves the boid to percieved center of local flockmates.

    rule2(): Activates second rule of the boid, makes the boid avoid eachother when they get to close.

    rule3(): Activates third rule of the boid, boid wants to match velocity the boids in their vicinity.

    attack(boids): Finds the closest boid and tries to eat it.

    draw: Draws the  object on the screen.

    """

    def __init__(self, x , y):
        """
        Initate attributes for the hawk\n
            x: int
            y: int
            flock: list
            radius: int ---> HAWK_RADIUS_START_VALUE | See config
        """
        super().__init__(x, y)
        self.radius = HAWK_RADIUS_START_VALUE


    def attack(self, boids):
        """
        Finds the closest boid and attacks it, if the boid is within the radius it eats the boid(removes it from the boid list).\n
        boids: list
        """
        min_distance = sqrt(WIDTH_SCREEN**2 + HEIGHT_SCREEN**2)
        for boid in boids:
            distance = self.distance(boid)
            if distance < min_distance:
                min_distance = distance
                x = boid.x
                y = boid.y
                meanx = boid.velx
                meany = boid.vely
            if distance < self.radius:
                boids.remove(boid)
                #self.radius += 1
        if len(boids) > 0:
            self.velx += (x - self.x)
            self.vely += (y - self.y)

    def move(self):
        """
        Moves the hawk\n
            scalar --> HAWK_ATTACK_SPEED_MULTIPLIER | See config
         """

        # Normalization using (v/||v||)
        self.x += (self.velx/np.sqrt(self.velx**2 + self.vely**2))*HAWK_ATTACK_SPEED
        self.y += (self.vely/np.sqrt(self.velx**2 + self.vely**2))*HAWK_ATTACK_SPEED

    def draw(self):
        """Draws the hawk on the program window"""
        pygame.draw.circle(SCREEN, RED, [int(self.x), int(self.y)], self.radius)




