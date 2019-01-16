import pygame


# Set gamescreen size
width_screen = 800
height_screen = 800

SCREENSIZE = (width_screen, height_screen)

# Set screen object
screen = pygame.display.set_mode(SCREENSIZE)




class Ball(object):
    """This class contains the structure of the ball object/s created."""

    def __init__(self):
        """
        self.x is the x position on the screen
        self.y is the y position on the screen
        self.velx is the velocity in the x direction
        self.vely is the velocity in the y direction
        self.radius is the radius of the ball
        """
        self.x = 250
        self.y = 250
        self.velx = 0
        self.vely = 14
        self.radius = 5
    def update(self):
        """
        Updates the position of the ball by how much velocity the ball has. 
        It also checks if it is close to border, if it is close enough it will bounce away in the same angle.
        """
        if self.x < 0+self.radius or self.x > width_screen-self.radius:
            self.velx *= -1

        if self.y < 0+self.radius:
            self.vely *= -1

        if self.y > height_screen:
            start_game.Game_status = 'lost'
        
        self.x += self.velx
        self.y += self.vely
        
        pygame.draw.circle(screen, (100,100,100), (int(self.x), int(self.y)), self.radius)

    def reset_ball(self):
        """Resets the ball position to original position."""
        self.x = 250
        self.y = 250
        self.velx = 0
        self.vely = 14
        self.radius = 5
        
