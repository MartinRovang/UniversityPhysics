
import pygame
from Files.Objects import Ball, Platform, Bricks
from Files.config import *




def main():
    
    # Clock/Timers
    clock = pygame.time.Clock() # Initiate clock object
    # Initialize pygame
    pygame.init()
    # set the pygame window name 
    pygame.display.set_caption('Breakout') 
    # FONTS
    ###########################################
    pygame.font.init() # module for adding text
    win_text = pygame.font.SysFont('Comic Sans MS', 30)

    Game_ball = Ball()
    Player = Platform()
    
    Bricks.initiate_bricks(AMOUNT_OF_BRICKS)

    while True:
        # Closing the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        # Limit to 60FPS this is to contain the speed of the ball on all computers (unless their FPS will stagnate below 60)
        TIME_PASSED = clock.tick(60)
        # Time in seconds
        TIME_PASSED_SECONDS = TIME_PASSED/1000.0

        Game_ball.move(TIME_PASSED_SECONDS)
        Player.move(TIME_PASSED_SECONDS)
        Game_ball.check_platform_collision(Player)
        Game_ball.check_wall_collisions()
        Bricks.update_bricks(Game_ball)

    
        # Update screen
        SCREEN.fill(BLACK)
        for bricks in Bricks.bricks_list:
            bricks.draw()

        Game_ball.draw()
        Player.draw()
        pygame.display.update()








if __name__ == "__main__":

    main()