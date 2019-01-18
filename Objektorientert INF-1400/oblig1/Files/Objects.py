import pygame 
from Files.config import *
import numpy as np



class Ball(object):
    """This class contains the structure of the ball object/s created."""

    def __init__(self):
        """
        self.x is the x position on the screen
        self.y is the y position on the screen
        self.velx is the velocity in the x direction
        self.vely is the velocity in the y direction
        self.radius is the radius of the ball
        self.magnitude is the total speed the ball always will have
        self.game_status is the current state of the game (this chooses which menu to be shown/ or if it is active play)
        """
        self.x = 250
        self.y = 250
        self.velx = 0
        self.vely = 6
        self.radius = 5
        self.magnitude = 100
        self.game_status = 'Ongoing'

    def update(self):
        """
        Updates the position of the ball by how much velocity the ball has. 
        It also checks if it is close to border, if it is close enough it will bounce away in the same angle.
        """
        # Bounce ball if ball hits the sides of the gaming screen
        if self.x < 0+self.radius or self.x > WIDTH_SCREEN-self.radius:
            self.velx *= -1

        # Bounce ball if ball hits the top of the gaming screen
        if self.y < 0+self.radius:
            self.vely *= -1

        # Lose if ball gets below the gaming screen
        if self.y > HEIGHT_SCREEN:
            self.game_status = 'lost'
        

        # Normalize the speed and scale with magnitude in order to maintain the speed at the magnitude
        self.x += self.magnitude*self.velx/np.sqrt(self.velx**2+self.vely**2)*TIME_PASSED_SECONDS
        self.y += self.magnitude*self.vely/np.sqrt(self.velx**2+self.vely**2)*TIME_PASSED_SECONDS

        
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.radius)

    def reset_ball(self):
        """Resets the ball position to original position."""
        self.x = 250
        self.y = 250
        self.velx = 0
        self.vely = 14









class Player(object):
    """This class contains the structure of the player objects / platform """

    def __init__(self):
        """
        self.x is the x position on the screen
        self.y is the y position on the screen
        self.height is the height of the rectangle
        self.width is the width of the rectangle
        """
        self.x = 200
        self.y = 700
        self.height = 25
        self.width = 150

    def update(self):
        """Updates the position of the platform"""
        pygame.draw.rect(screen, GREY, (self.x, self.y, self.width, self.height))









class Bricks(object):

    """This class contains the structure of the bricks objects to be destroyed by the player"""

    def __init__(self, x, y, health = 1):
        """        
        self.x is the x position on the screen
        self.y is the y position on the screen
        self.height is the height of the rectangle
        self.width is the width of the rectangle
        self.health is the health of the bricks which defines how many hits needed to destroy the bricks
        """
        self.x = x
        self.y = y
        self.height = 25
        self.width = 50
        self.health = health

    
    def update(self):
        
        """Method whichs assigns the colors of the bricks"""
        if self.health == 1:
            pygame.draw.rect(screen, GREY, (self.x, self.y, self.width, self.height))
        if self.health == 2:
            pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))
        if self.health == 3:
            pygame.draw.rect(screen, GREEN, (self.x, self.y, self.width, self.height))
        if self.health == 4:
            pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))
