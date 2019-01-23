
import pygame
from math import cos, sin, radians, sqrt
from Files.config import *
from Files.Boid import Boid
import random
import numpy as np

class Hawk(Boid):
    """
    Summary:
        Inherits from MovingObject, this class makes the boids object
        
    Args:
    x: x-position.

    y: y-position.   

    Methods:
    move(TIME_PASSED_SECONDS): Places the moving object according to its speed and magnitude.

    get_pos: Returns the position (x, y).

    set_pos(x,y): Sets the position to (x, y).

    set_vel(velx,vely): Sets the velocity to (velx, vely).

    get_vel: Returns the velocity (velx, vely).

    crash_wall_check(TIME_PASSED_SECONDS, wall_lock): Checks if the object is colliding with the walls of the screen, and bounce them off if wall_lock == 1 else they go to the other side.

    noisy_movement(TIME_PASSED_SECONDS): Makes the noisy movement to the hawks.

    flocking(hawks): Takes the list of hawks and makes the hawks flock together to their percieved center.

    match_speed(hawks): Takes the list of hawks and sets the avarage heading of the flock.

    avoid_crash(hawks): Takes the list of hawks and makes them avoid eachother.

    attack(boids): Takes the list of boids and sends the hawk to attack the nearest boid.

    draw: draws the obstacle object on the screen
    """

    def __init__(self, x , y):
        super().__init__(x, y)
        self.radius = HAWK_RADIUS_START_VALUE
        self.nomsound = pygame.mixer.Sound('nomnom.ogg')

    def attack(self, boids):
        min_distance = sqrt(WIDTH_SCREEN**2 + HEIGHT_SCREEN**2)
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

    def draw(self):
        pygame.draw.circle(SCREEN, RED, [int(self.x), int(self.y)], self.radius)




