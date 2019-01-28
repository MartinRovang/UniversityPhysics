import pygame



class Ball():
    def __init__(self):
        self.x = BALL_START_POS_X
        self.y = BALL_START_POS_Y
        self.radius = BALL_RADIUS
    

    def draw():
        pygame.draw.circle(SCREEN, GRAY, (self.x, self.y)), self.radius)




class Bricks():
    def __init__(self):
        self.x = BALL_START_POS_X
        self.y = BALL_START_POS_Y
        self.height = BRICKS_HEIGHT
        self.width = BRICKS_WIDTH

    