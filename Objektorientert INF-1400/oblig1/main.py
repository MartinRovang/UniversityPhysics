from os import environ
import pygame
import numpy as np
import csv
from Files.initiate import nickname, highscore
from Files.Objects import Ball, Player, Bricks
from Files.config import *



    

class Game(object):
    """To create one instance of the game"""
    def __init__(self):
        """
        self.player is a player object, in this case the game is hardcoded for just one player
        self.player_ball is the ball object
        self.bricks_list is the list which will contain all the bricks to be destroyed by the player
        self.points is the amount of points the player has
        self.amount is the the lvl/hp of bricks (amount of times to be hit before destroyed)
        """
        self.player = Player()
        self.player_ball = Ball()
        self.bricks_list = []
        self.points = 0
        self.amount = 0


    # The events loop method
    def Events(self):
        """Checks for events and if pressed the X in the corner the program will quit"""
        # Closing the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        # Controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.player.x > 0:
                self.player.x -= PLATFORM_SPEED*TIME_PASSED_SECONDS

        if keys[pygame.K_RIGHT]:
            if self.player.x < (800-self.player.width):
                self.player.x += PLATFORM_SPEED*TIME_PASSED_SECONDS


    def initiate_Bricks(self, rows):
        """Puts the bricks out in the game"""
        for j in range(rows):
            for i in range(13):
                self.bricks_list.append(Bricks(i*50 + i*10+10, (j+1)*50+50 , j+1))

    
    def hit_detection(self, x, y, r, bricks):
        """Method for hit detection with the ball and bricks"""
        hit =  (x+r) > bricks.x and (x-r) < bricks.x+bricks.width\
             and (y < bricks.y+bricks.height) and (y+r) > bricks.y
        return hit


    def update_bricks(self):
        """Checks if ball hits the bricks, if bricks are hit they lose 1 hp and reflect the ball"""

        bricks_list = self.bricks_list
        for bricks in bricks_list:
            hit = self.hit_detection(self.player_ball.x, self.player_ball.y, self.player_ball.radius, bricks)

            if hit:
                self.player_ball.velx *= -1
                self.player_ball.vely *= -1
                # Bump the ball a bit away such that the if test only happens once per hit (sign to bumb it away according to hit direction)
                self.player_ball.y += np.sign(self.player_ball.vely)*10
                bricks.health -= 1
                self.points += 1

            if bricks.health <= 0:
                bricks_list.remove(bricks)
            
            # Update to change the color when hp is lost.
            bricks.update()
            
            # If the amount of bricks left is zero player will win
            if len(bricks_list) == 0:
                self.player_ball.game_status = 'won'


    def reset_bricks(self):
        """Resets bricks/ empties the bricks list"""
        self.bricks_list = []

    
    def game_menu(self):
        """The menu with levels and highscore"""
        # Load menu images
        menu_background = pygame.image.load('menu.png')
        menu_hover1 = pygame.image.load('menu_hover1.png')
        menu_hover2 = pygame.image.load('menu_hover2.png')
        menu_hover3 = pygame.image.load('menu_hover3.png')
        menu_hover4 = pygame.image.load('menu_hover4.png')
        # Reset points
        self.points = 0
        while True:
            # Run events to avoid crashing when exiting
            self.Events()

            # Get mouse position
            mousepos_x, mousepos_y = pygame.mouse.get_pos()
            
            # Hovering effects in menu
            if mousepos_x > 213 and mousepos_x < 410:
                if mousepos_y > 175 and mousepos_y < 218:
                    screen.blit(menu_hover1, (0,0))
                    if pygame.mouse.get_pressed()[0] == 1:
                        self.amount = 1
                        break
                if mousepos_y > 333 and mousepos_y < 374:
                    screen.blit(menu_hover2, (0,0))
                    if pygame.mouse.get_pressed()[0] == 1:
                        self.amount = 2
                        break
                if mousepos_y > 487 and mousepos_y < 529:
                    screen.blit(menu_hover3, (0,0))
                    if pygame.mouse.get_pressed()[0] == 1:
                        self.amount = 3
                        break

            # Open highscore menu
            elif mousepos_x > 513 and mousepos_x < 768 and mousepos_y > 308 and mousepos_y < 363:
                screen.blit(menu_hover4, (0,0))
                if pygame.mouse.get_pressed()[0] == 1:
                    # Read highscore
                    with open('highscore.txt','r') as csvfile:
                        highscore = eval(csvfile.read())
                    while True:
                        mousepos_x, mousepos_y = pygame.mouse.get_pos()
                        # Allow for exiting program without crashing
                        self.Events()

                        # Highscore text
                        screen.fill((0,0,0))
                        wintext = win_text.render('{}  {}      {}'.format('Place' ,'Nickname', 'Score'), False, GREY)
                        screen.blit(wintext,(150,10))

                        # Exit highscore button
                        if mousepos_x > 600 and mousepos_x < 663 and mousepos_y > 55 and mousepos_y < 86:
                            exit_button = win_text.render('Exit', False, RED)
                            screen.blit(exit_button,(600,50))
                            if pygame.mouse.get_pressed()[0] == 1:
                                break
                            
                        else:
                            exit_button = win_text.render('Exit', False, GREY)
                            screen.blit(exit_button,(600,50))

                        # Sort for highest score and print on screen, the highscore is a type dict.
                        for i, nicknames in enumerate(sorted(highscore, key=highscore.get, reverse=True)):
                            wintext = win_text.render('{}. {}      {}'.format(i+1 ,nicknames, highscore[nicknames]), False, GREY)
                            screen.blit(wintext,(200,50+i*50))

                            # Only print top 10
                            if i > 9:
                                break
                        pygame.display.update()
            
            # If no hovering display regular menu
            else:
                screen.blit(menu_background, (0,0))

            # Update screen
            pygame.display.update()


        
    
    def Gameloop(self):
        """The game loop method, this is looped to hold the game window open and runs the game in general"""

        # Starts menu and gets the level(self.amount)
        self.game_menu()
        # Starts the initate bricks function to create bricks with the given amount which is chosen in the menu
        self.initiate_Bricks(self.amount)
        player = self.player
        player_ball = self.player_ball
        # Coordinate change for where ball hit on the circle and add the corresponding x velocity according to angle
        theta = np.linspace(np.pi, 0 , player.width)
        radius_player = player.width/2
        # Loops while the game is ongoing
        while self.player_ball.game_status == 'Ongoing':
            TIME_PASSED = clock.tick(60)
            TIME_PASSED_SECONDS = TIME_PASSED/1000.0

            # Bounce ball when hitting the platform
            if player_ball.x > player.x and player_ball.x < (player.x+player.width) and (player_ball.y+player_ball.radius) > (player.y) and (player_ball.y+player_ball.radius) < (player.y+player.height):
                player_ball.y -= 10
                player_ball.vely *= -1

                ball_hit = (player_ball.x-player.x)
                # Set angle by the speed of the ball in x direction by where on the platform it hits (middle = 0 x speed)
                player_ball.velx = 14*np.cos(theta[int(ball_hit)])

                
            #Fills the screen with black to remove the old position of the drawn objects
            screen.fill((0,0,0))
            
            # Update functions for updating positions etc for all the objects in the game
            player.update()
            player_ball.update()
            self.update_bricks()

            # Keeps the events loop going
            self.Events()

            # Text that shows how much points the player currently has
            point_text = win_text.render('Points: %d'%self.points, False, GREY)

            # Prints text on screen with position x = 30 and y = 50
            screen.blit(point_text,(30,50))

            # Updates the screen
            pygame.display.update()
        
        # If win
        while self.player_ball.game_status == 'won':
            # Get mouse position
            mousepos_x, mousepos_y = pygame.mouse.get_pos()
            # Save points to highscore if higher then before
            if highscore[nickname] < self.points:
                highscore[nickname] = self.points
                with open('highscore.txt','w') as csvfile:
                    csvfile.write('%s'%highscore)
            self.Events()
            wintext = win_text.render('YOU WON!!', False, (100, 100, 100))
            screen.blit(wintext,(int(WIDTH_SCREEN/2),int(HEIGHT_SCREEN/2)))

            # Exit win screen button when hovered over button it turns red.
            if mousepos_x > 600 and mousepos_x < 663 and mousepos_y > 705 and mousepos_y < 737:
                exit_button = win_text.render('Exit', False, RED)
                screen.blit(exit_button,(600,700))
                if pygame.mouse.get_pressed()[0] == 1:
                    # Start gameloop again
                    self.player_ball.game_status = 'Ongoing'
                    player_ball.reset_ball()
                    player.reset_player()
                    self.reset_bricks()
                    start_game.Gameloop()
                
            else:
                # If not hovering over show white colored exit button.
                exit_button = win_text.render('Exit', False, GREY)
                screen.blit(exit_button,(600,700))

            # Updates the screen
            pygame.display.update()

        # If lost
        while self.player_ball.game_status == 'lost':
            # Get mouse position
            mousepos_x, mousepos_y = pygame.mouse.get_pos()
            # Save points to highscore if higher then before
            if highscore[nickname] < self.points:
                highscore[nickname] = self.points
                with open('highscore.txt','w') as csvfile:
                    csvfile.write('%s'%highscore)

            self.Events()
            wintext = win_text.render('YOU LOST!!', False, (100, 100, 100))
            screen.blit(wintext,(int(WIDTH_SCREEN/2),int(HEIGHT_SCREEN/2)))

            # Exit lost screen button
            if mousepos_x > 600 and mousepos_x < 663 and mousepos_y > 705 and mousepos_y < 737:
                exit_button = win_text.render('Exit', False, RED)
                screen.blit(exit_button,(600,700))
                if pygame.mouse.get_pressed()[0] == 1:
                    # Start gameloop again
                    self.player_ball.game_status = 'Ongoing'
                    player_ball.reset_ball()
                    player.reset_player()
                    self.reset_bricks()
                    start_game.Gameloop()
                
            else:
                exit_button = win_text.render('Exit', False, GREY)
                screen.blit(exit_button,(600,700))

            # Update screen
            pygame.display.update()


            

# Make game object
start_game = Game()

# Initiates the gameloop
start_game.Gameloop()

