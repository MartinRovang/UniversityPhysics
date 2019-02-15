import pygame
from math import cos, sin, radians, sqrt
from Files.config import *
from Files.GenObjects import MovingObject
import random
import numpy as np

class Boid(MovingObject):
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

    crash_wall_check(wall_lock): Checks if the object is colliding with the walls of the screen, and bounce them off if wall_lock == 1 else they go to the other side.

    noisy_movement(): Makes the noisy movement to the boid.

    flocking(boids): Takes the list of boids and makes the boids flock together to their percieved center.

    match_speed(boids): Takes the list of boids and sets the avarage heading of the flock.

    avoid_crash(boids): Takes the list of boids and makes them avoid eachother.

    avoid_hawk(hawks): Takes the list of hawks and makes the boids avoid the hawks.

    draw: draws the obstacle object on the screen
    """

    def __init__(self, x , y):
        super().__init__(x, y)
        self.flocked = 0
        self.flock = []
        self.radius = BOID_RADIUS

    def noisy_movement(self):
        if self.flocked == 0:
            #Make white noise movement
            self.velx += random.gauss(BOID_MEAN_NOISY_X, BOID_VARIANCE_NOISY_X)
            self.vely += random.gauss(BOID_MEAN_NOISY_Y, BOID_VARIANCE_NOISY_Y)
            if abs(self.velx) > MAX_NOISE_SPEED_X:
                self.velx = MAX_NOISE_SPEED_X
            if abs(self.vely) > MAX_NOISE_SPEED_Y:
                self.vely = MAX_NOISE_SPEED_Y


    def flocking(self, boids): 
        mean_x = []
        mean_y = []
        flock = self.flock
        mean_pos_x = 0
        mean_pos_y = 0

        for boid in boids:
            if boid != self:
                distance = sqrt((boid.x - self.x)**2 + (boid.y - self.y)**2)
                if distance <= BOID_DISTANCE_FLOCKING_RADIUS and boid not in flock:
                    mean_x.append(boid.x)
                    mean_y.append(boid.y)
                    flock.append(boid)
                if distance > BOID_DISTANCE_FLOCKING_RADIUS and boid in flock:
                    flock.remove(boid)


        if len(flock) > 0:
            mean_pos_x = np.mean(mean_x)
            mean_pos_y = np.mean(mean_y)
            self.velx = mean_pos_x
            self.vely = mean_pos_y



    def match_speed(self, boids):
        flock = self.flock
        velx = 0
        vely = 0
        if len(flock) > 0:
            for boid in flock:
                velx += boid.velx
                vely += boid.vely
        
            self.velx = velx/len(flock)
            self.vely = vely/len(flock)


    def avoid_crash(self, boids):
        for boid in boids:
            if boid != self:
                distance = sqrt((boid.x-self.x)**2 + (boid.y-self.y)**2)
                if distance < BOIDS_AVOID_CRASH_DISTANCE + boid.radius:
                    boid.velx = (boid.x - self.x)
                    boid.vely = (boid.y - self.y)
                if distance < 1:
                    boid.velx = (self.x - boid.x) 
                    boid.vely = (self.y - boid.y)
                    


    def draw(self):
        try:
            pygame.draw.circle(SCREEN, GREY, [int(self.x), int(self.y)], MOVING_OBJECT_RADIUS)
        except:
            self.x, self.y = (20,20)
            print('Error in coordinates, pushing boid back to (20,20)')


    
    def avoid_hawk(self, hawks):
        for hawk in hawks:
            distance = sqrt((hawk.x-self.x)**2 + (hawk.y-self.y)**2)
            if distance < HAWK_TRIGGER_BOID_DISTANCE:
                self.vely = ((hawk.vely + self.vely) / sqrt(self.vely**2 + hawk.vely**2))*BOID_AVOID_HAWK_MAGNITUDE
                self.velx = ((hawk.velx + self.velx) / sqrt(self.vely**2 + hawk.vely**2))*BOID_AVOID_HAWK_MAGNITUDE


    
        