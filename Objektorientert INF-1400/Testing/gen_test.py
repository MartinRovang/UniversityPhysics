"""
This application calculates pi using a monte carlo method,
and visualizes the results compared to the constant in the
math library
"""

from random import random
from math import sqrt
from math import pi
from collections import deque
from time import clock

import pygame


def calculate_pi():
    """
    Calculates pi using a monte carlo method, returns pi
    As the are of a circle is pi * r ^ 2, and the area of
    a square is (2 * r) ^ 2, we can calculate pi by estimating
    the ratio between points inside a circle and a square where
    the circle fits perfectly inside the square.
    When this ratio is multiplied by 4, the result is pi.
    Arguments:
    iterations -- the number of random points generated
    """
    # TODO: Replace with an iterator?
    points_inside_circle = 0
    iterr = 0
    while True:
        iterr += 1
        # Generate a random point between (-0.5, -0.5) and (0.5, 0.5)
        x_position = random() - 0.5
        y_position = random() - 0.5
        # Check if point is inside the circle
        if sqrt(x_position**2 + y_position**2) <= 0.5:
            points_inside_circle += 1
            estimated_pi = 4 * points_inside_circle / iterr
            yield estimated_pi



class PiEstimation:
    """
    Class for visualizing and calculating pi
    """
    # pylint: disable=too-many-instance-attributes
    def __init__(self):
        """
        Sets up pygame, and variables used for visualization
        DO NOT MODIFY
        """
        # Pygame initialization
        pygame.init()
        self._screen_size = 800
        self._screen = pygame.display.set_mode((self._screen_size,
                                                self._screen_size))
        self._point = pygame.Surface((1, 5))
        self._point.fill((0, 255, 0))

        # Variables used for visualization
        self._accumulated_error = 0
        self._values = deque(maxlen=self._screen_size)
        self._time_iteration = clock()
        self.print_interval = 100
        self.draw_interval = 2

        # Calculated pi for the current number of iterations
        self.current_iterations = 100
        self.current_pi = 0


    def mainloop(self):
        """
        Continously calculates a more correct value for pi
        and draws this on screen, loops forever.
        """
        # TODO: Change to use an iterator?
        g = calculate_pi()
        while True:
            self.current_pi = next(g)
            self.current_iterations += 1
            self._visualize_results()


    def _visualize_results(self):
        """
        Accumulate errors and values, draw the screen and print statistics
        DO NOT MODIFY
        """
        # Accumulate errors
        self._accumulated_error += abs(self.current_pi - pi)
        # Add most recent pi calculation to the drawing list
        self._values.append(self._pi2y(self.current_pi))

        # Draw results to screen every 2nd iteration
        if self.current_iterations % self.draw_interval == 0:
            self._update_screen()

        # Print statistics every 100 iterations
        if self.current_iterations % self.print_interval == 0:
            self._print_statistics()


    def _update_screen(self):
        """
        Draws the last 800 estimated values for pi, as well as
        the reference from math.pi
        DO NOT MODIFY
        """
        self._screen.fill((0, 0, 0))
        # Draw all estimates on the screen
        for x_position, y_position in enumerate(self._values):
            self._screen.blit(self._point, (x_position, y_position))

        # Draw the reference pi value on the screen
        pygame.draw.line(self._screen,
                         (255, 0, 0),
                         (self._screen_size - 50, self._pi2y(pi)),
                         (self._screen_size, self._pi2y(pi)),
                         5)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                final_str = "Final value for pi: {}"
                print(final_str.format(self.current_pi))
                pygame.quit()
                exit()


    def _print_statistics(self):
        """
        Print statistics to stdout for values between this call
        and the previous call to this method.
        DO NOT MODIFY
        """
        time_passed = clock() - self._time_iteration
        output = "At iteration {:>6}, pi is {:>6.5}, average error is {:<8.5}, " \
                 "done in {:<4.2} seconds ({} iterations per second)"
        print(output.format(self.current_iterations,
                            self.current_pi,
                            self._accumulated_error/self.print_interval,
                            time_passed,
                            int(self.print_interval/time_passed)))
        self._accumulated_error = 0
        self._time_iteration = clock()


    def _pi2y(self, value):
        # Do not modify this method
        return int((value - 2.5) * (self._screen_size * 0.75))



if __name__ == "__main__":
    PiEstimation().mainloop()