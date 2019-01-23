import pygame
from math import cos, sin, radians, sqrt
from Files.config import *
from Files.GenObjects import MovingObject
import random

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

    crash_wall_check(TIME_PASSED_SECONDS, wall_lock): Checks if the object is colliding with the walls of the screen, and bounce them off if wall_lock == 1 else they go to the other side.

    noisy_movement(TIME_PASSED_SECONDS): Makes the noisy movement to the boid.

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

    def noisy_movement(self, TIME_PASSED_SECONDS):
        if self.flocked == 0:
            #Make white noise movement
            self.velx += random.gauss(BOID_MEAN_NOISY_X, BOID_VARIANCE_NOISY_X)
            self.vely += random.gauss(BOID_MEAN_NOISY_Y, BOID_VARIANCE_NOISY_Y)
            if abs(self.velx) > MAX_NOISE_SPEED_X:
                self.velx = MAX_NOISE_SPEED_X
            if abs(self.vely) > MAX_NOISE_SPEED_Y:
                self.vely = MAX_NOISE_SPEED_Y


    def flocking(self, boids): 
        flock = self.flock
        x = 0
        y = 0
        i = 0
        mean_pos_x = 0
        mean_pos_y = 0
        velx = 0
        vely = 0
        for boid in boids:
            if boid != self:
                distance = sqrt((boid.x-self.x)**2 + (boid.y-self.y)**2)
                if distance <= BOID_DISTANCE_FLOCKING_RADIUS and boid not in flock:
                    flock.append(boid)
                    x += boid.x 
                    y += boid.y

                    i += 1

                if distance > BOID_DISTANCE_FLOCKING_RADIUS and boid in flock:
                    flock.remove(boid)
                    x -= boid.x
                    y -= boid.y

                    i -= 1
        try:
            mean_pos_x = (x/i) - self.x
            mean_pos_y = (y/i) - self.y

        except ZeroDivisionError:
            pass
        
        if i > 0:
            self.flocked = 1
            self.velx = mean_pos_x
            self.vely = mean_pos_y
        else:
            self.flocked = 0


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
                    boid.velx += (self.x - boid.x) 
                    boid.vely += (self.y - boid.y)
                    


    def draw(self):
        pygame.draw.circle(SCREEN, GREY, [int(self.x), int(self.y)], MOVING_OBJECT_RADIUS)


    
    def avoid_hawk(self, hawks):
        for hawk in hawks:
            distance = sqrt((hawk.x-self.x)**2 + (hawk.y-self.y)**2)
            if distance < HAWK_TRIGGER_BOID_DISTANCE + hawk.radius:
                # self.velx = (hawk.velx-self.velx)
                # self.vely = (hawk.vely-self.vely)
                self.vely += ((hawk.vely + self.vely) / sqrt(self.vely**2 + hawk.vely**2))*BOID_AVOID_HAWK_MAGNITUDE
                self.velx += ((hawk.velx + self.velx) / sqrt(self.vely**2 + hawk.vely**2))*BOID_AVOID_HAWK_MAGNITUDE


    
        