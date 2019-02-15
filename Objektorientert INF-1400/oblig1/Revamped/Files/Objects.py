import pygame
from Files.config import *
from math import sqrt, cos
import numpy as np

class Ball():
    """
    This class contains the structure of the ball object/s created.\n

    Methods:\n
        move(TIME_PASSED_SECONDS): Moves the object according to speed\n

        check_wall_collisions(): Checks if the object collides with wall\n

        check_platform_collision(platform): Chekcs if the object collides with platform\n

        draw(self): Draws the object on screen
    """
    def __init__(self):
        """
        self.x is the x position on the screen
        self.y is the y position on the screen
        self.velx is the velocity in the x direction
        self.vely is the velocity in the y direction
        self.radius is the radius of the ball
        """
        self.x = BALL_START_POS_X
        self.y = BALL_START_POS_Y
        self.velx = BALL_START_VELX
        self.vely = BALL_START_VELY
        self.radius = BALL_RADIUS


    def move(self, TIME_PASSED_SECONDS):
        """Moves the ball on the screen by the given ball speed, see config."""
        try:
            # To avoid time_passed_seconds being too high in the beginning.
            if TIME_PASSED_SECONDS > 0.020:
                TIME_PASSED_SECONDS = 0.017
            self.x += self.velx/(sqrt(self.velx**2 + self.vely**2))*BALL_SPEED*TIME_PASSED_SECONDS
            self.y += self.vely/(sqrt(self.velx**2 + self.vely**2))*BALL_SPEED*TIME_PASSED_SECONDS
        except ZeroDivisionError:
            self.x += 0.001
            self.y += 0.001


    def check_wall_collisions(self):
        """Check if the ball collides with the walls, if the ball is lost below the screen the method return True."""
        # Bounce ball if ball hits the sides of the gaming screen
        if (self.x < 0 + self.radius) or self.x > (WIDTH_SCREEN - self.radius):
            self.velx *= -1
            return False

        # Bounce ball if ball hits the top of the gaming screen
        if self.y < 0 + self.radius:
            self.vely *= -1
            return False

        # Lose if ball gets below the gaming screen
        if self.y > HEIGHT_SCREEN:
            return True

    

    def check_platform_collision(self, platform):
        """
        Checks if the ball collides with the platform and bounces the ball back\n
        platform -> Object.
        """
        # Coordinate change for where ball hit on the circle and add the corresponding x velocity according to angle
        theta = np.linspace(np.pi, 0 , platform.width)

        # Bounce ball when hitting the platform
        if self.x > platform.x and self.x < (platform.x + platform.width) \
        and (self.y + self.radius) > (platform.y)\
            and (self.y + self.radius) < (platform.y + platform.height):
            self.y -= 10
            self.vely *= -1
            ball_hit = (self.x - platform.x)
            # Set angle by the speed of the ball in x direction by where on the platform it hits (middle = 0 x speed)
            self.velx = ANGLE_MAGNITUDE*cos(theta[int(ball_hit)])



    def draw(self):
        """Draw the ball on the screen"""
        pygame.draw.circle(SCREEN, GRAY, (int(self.x), int(self.y)), self.radius)





class Platform():
    """This class contains the structure of the player objects / platform """

    def __init__(self):
        """
        self.x is the x position on the screen
        self.y is the y position on the screen
        self.height is the height of the rectangle
        self.width is the width of the rectangle
        """
        self.x = PLATFORM_START_POS_X
        self.y = PLATFORM_START_POS_Y
        self.width = PLATFORM_WIDTH
        self.height = PLATFORM_HEIGHT



    def move(self, TIME_PASSED_SECONDS):
        """Moves the platform"""

        # Closing the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        # Controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.x > 0:
                self.x -= PLATFORM_SPEED*TIME_PASSED_SECONDS

        if keys[pygame.K_RIGHT]:
            if self.x < (WIDTH_SCREEN-self.width):
                self.x += PLATFORM_SPEED*TIME_PASSED_SECONDS

    def draw(self):
        """Draw the platform on the screen"""
        pygame.draw.rect(SCREEN, GRAY, (self.x, self.y, self.width, self.height))




class Bricks():
    """
    This class contains the structure of the bricks objects to be destroyed by the player\n
    
    Contains class attribute -> bricks_list -> list\n

    Methods:\n
    
    @staticmethod
    hit_detection(Ball, bricks): Checks if ball collides with bricks\n
    
    @staticmethod
    update_bricks(Ball): Checks if ball hits the bricks, if bricks are hit they lose 1 hp and reflect the ball\n

    @staticmethod
    initiate_bricks(rows): Puts the bricks out in the game\n
    
    draw(self): Draws the object on screen
    """
    

    
    bricks_list = []

    def __init__(self,x ,y):
        """        
        self.x is the x position on the screen
        self.y is the y position on the screen
        self.height is the height of the rectangle
        self.width is the width of the rectangle
        self.health is the health of the bricks which defines how many hits needed to destroy the bricks
        """
        self.x = x
        self.y = y
        self.height = BRICKS_HEIGHT
        self.width = BRICKS_WIDTH
        self.health = 1


    @staticmethod
    def hit_detection(Ball, bricks):
        """Method for hit detection with the ball and bricks"""
        hit =  (Ball.x+Ball.radius) > bricks.x and (Ball.x-Ball.radius) < bricks.x+bricks.width\
             and (Ball.y < bricks.y+bricks.height) and (Ball.y+Ball.radius) > bricks.y
        return hit



    @staticmethod
    def update_bricks(Ball):
        """Checks if ball hits the bricks, if bricks are hit they lose 1 hp and reflect the ball"""

        bricks_list = Bricks.bricks_list

        for bricks in bricks_list:
            hit = Bricks.hit_detection(Ball, bricks)

            if hit:
                Ball.vely *= -1
                # Bump the ball a bit away such that the if test only happens once per hit (sign to bumb it away according to hit direction)
                Ball.y += np.sign(Ball.vely)*10
                bricks.health -= 1

            # Remove bricks when health is below 0
            if bricks.health <= 0:
                bricks_list.remove(bricks)



    @staticmethod
    def initiate_bricks(rows):
        """Puts the bricks out in the game"""
        bricks_list = Bricks.bricks_list
        for j in range(rows):
            for i in range(NUMBER_OF_BLOCK_HORIZONTAL):
                bricks_list.append(
                Bricks(i*XDISTANCE_BETWEEN_BLOCKS + i + XSHIFT_BLOCKS,
                    (j+1)*YDISTANCE_BETWEEN_BLOCKS + YSHIFT_BLOCKS)
                    )
        

    def draw(self):
        """Method to draw the bricks"""
        pygame.draw.rect(SCREEN, GRAY, (self.x, self.y, self.width, self.height))


    

    