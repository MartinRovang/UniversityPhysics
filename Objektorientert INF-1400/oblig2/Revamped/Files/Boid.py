import pygame
from math import cos, sin, radians, sqrt
from Files.config import *
from Files.GenMovObject import MovingObject


class Boid(MovingObject):
    """
    Summary:
        When called creates a boid object. Inherits from MovingObject class

    Args:
    x: x-position

    y: y-position

    __init__:\n
    
    self.flock = []
    
    self.radius = BOIDS_RADIUS | See config


    Methods:
    move(): Places the moving object according to its speed and magnitude.

    find_flock(boids): assigns boids to a boids flock.

    rule1(): Activates first rule of the boid, moves the boid to percieved center of local flockmates.

    rule2(): Activates second rule of the boid, makes the boid avoid eachother when they get to close.

    rule3(): Activates third rule of the boid, boid wants to match velocity the boids in their vicinity.

    avoid_hawk(hawks): If the Hawks/Hoiks gets to close they will try to avoid it. 

    draw: Draws the object on the screen.

    """
    
    def __init__(self, x, y):
        """
        Initate attributes for the boid\n
            x: int
            y: int
            flock: list
            radius: int ---> BOIDS_RADIUS | See config
        """
        super().__init__(x, y)
        self.flock = []
        self.radius = BOIDS_RADIUS

    def find_flock(self, boids):
        """
        Puts the boids which belongs to a boid flock into flock list.\n
        boids: list
        """
        flock = self.flock
        for boid in boids:
            if (self.distance(boid) < BOID_DISTANCE_FLOCKING_RADIUS) and boid not in flock and boid != self:
                self.flock.append(boid)
            elif boid in flock:
                self.flock.remove(boid)


    def rule1(self):
        """Activates first rule of the boid, moves the boid to percieved center of local flockmates."""
        flock = self.flock
        x, y = (0,0)
        for boid in flock:
            x += boid.x
            y += boid.y

        if len(flock) > 0:
            mean_x = x/len(flock)
            mean_y = y/len(flock)
            mean_velx = (mean_x - self.x)/100 # 1% of total to avoid massive numbers
            mean_vely = (mean_y - self.y)/100 # 1% of total to avoid massive numbers
            self.velx += mean_velx; self.vely += mean_vely


    def rule2(self):
        """Activates second rule of the boid, makes the boid avoid eachother when they get to close."""
        flock = self.flock
        velx = 0
        vely = 0
        for boid in flock:
            if (self.distance(boid) < BOIDS_AVOID_CRASH_DISTANCE):
                velx += -(boid.x - self.x)
                vely += -(boid.y - self.y)
        self.velx += velx; self.vely += vely;


    def rule3(self):
        """Activates third rule of the boid, boid wants to match velocity the boids in their vicinity."""
        flock = self.flock
        velx = 0
        vely = 0
        COESIAN_NUMBER = 0
        for boid in flock:
            distance = self.distance(boid)
            if distance < BOIDS_COHESIAN_RADIUS:
                velx += boid.velx
                vely += boid.vely
                COESIAN_NUMBER += 1

        if COESIAN_NUMBER > 0:
            mean_velx = velx/COESIAN_NUMBER
            mean_vely = vely/COESIAN_NUMBER
            mean_velx = (mean_velx - self.velx)/8 # 8 of total
            mean_vely = (mean_vely - self.vely)/8 # 8 of total
            self.velx += mean_velx; self.vely += mean_vely


    def avoid_hawk(self, hawks):
        """
        If the Hawks/Hoiks gets to close they will try to avoid it. \n
            hawks: list
        """
        for hawk in hawks:
            distance = self.distance(hawk)
            if distance < HAWK_TRIGGER_BOID_DISTANCE:
                self.velx += (hawk.vely - self.vely)/100  #1% of total to avoid massive numbers
                self.vely += (hawk.velx - self.velx)/100  #1% of total to avoid massive numbers
        
        
    def draw(self):
        """Draws the object on the screen."""
        pygame.draw.circle(SCREEN, GRAY, (int(self.x), int(self.y)), self.radius)




