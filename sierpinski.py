"""A python module to make
a Sierpinski triangle using
random dots generated with the
help of Python's turtle
module (which uses Tkinter)
"""
import sys
import turtle
from random import choice

class Sierpinski:
    """Class with various helpful
    tools to create a customisable
    sierpinski shape
    """
    def __init__(self, length=200, sides=3, dotsize=5, speed=10):
        """Length of each side
        and number of sides
        """
        self.length = length
        self.sides = sides
        self.dotsize = dotsize

        # Set turtle speed
        turtle.speed(speed)

        # Coordinates for corners & previous dot placed
        self.corners = []
        self.previous_dot = 0

    def internal_angles(self):
        """Check if the sides of the shape
        are bigger than three and if so
        determine internal angles
        shape, e.g. triangle would be 60,
        square would be 90 etc...
        """
        if self.sides < 3:
            print("Shape must have more than 3 sides")
            sys.exit(1)

        return int(((self.sides-2)*180)/self.sides)

    def draw_between_points(self, point1, point2):
        """Finds the midpoint between
        two coordinates and draws a dot there
        """
        xcoord = (point1[0]+point2[0])/2
        ycoord = (point1[1]+point2[1])/2

        # Make this the "previous dot"
        self.previous_dot = [xcoord, ycoord]

        # Draw dot
        turtle.goto(xcoord, ycoord)
        turtle.pendown()
        turtle.dot(self.dotsize)
        turtle.penup()


    def setup_shape(self):
        """Draw initial corners of shape
        in red and add corner coordinates
        to self.corners list
        """
        turtle.pencolor("red")

        # Angle inside shape
        interior_angle = self.internal_angles()

        while self.sides > 0:
            turtle.pendown()
            turtle.dot(self.dotsize)

            # Add coordinates of corner to list
            self.corners.append(list(turtle.position()))

            turtle.left(180-interior_angle)
            turtle.penup()

            turtle.forward(self.length)

            # Subtract 1 from self.sides to eventually end loop
            self.sides += -1

        turtle.pencolor("black")

    def draw_sierpinski(self, iterations=10000):
        """Check if there's a previous point
        if not draw a dot between two adjacent corners.
        Pick a random corner and place a dot between
        that and the previous dot placed and repeat for x iterations
        """
        # Draw corners
        self.setup_shape()

        if self.previous_dot == 0:
            self.draw_between_points(self.corners[0], self.corners[1])

        while iterations > 0:
            # Pick a random corner
            corner = choice(self.corners)

            # Draw between corner and previous dot
            self.draw_between_points(corner, self.previous_dot)

            iterations += -1
