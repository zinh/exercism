from math import sin, cos, pi
# Globals for the bearings
# Change the values as you see fit
EAST = -pi/2
NORTH = 0
WEST = pi/2
SOUTH = pi


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.x = x
        self.y = y
        self.rotate_matrix = [
                [int(cos(self.bearing)), -int(sin(self.bearing))],
                [int(sin(self.bearing)), int(cos(self.bearing))]]
        print(self.rotate_matrix)

    @property
    def coordinates(self):
        return (self.rotate_matrix[0][0] * self.x + self.rotate_matrix[0][1] * self.y,
        self.rotate_matrix[1][0] * self.x + self.rotate_matrix[1][1] * self.y)

    def turn_right(self):
        self.x = self.x + 1

    def turn_left(self):
        self.x = self.x - 1

    def advance(self):
        self.y = self.y + 1

    def simulate(self, path):
        for direction in path:
            if direction == 'L':
                self.turn_left()
            elif direction == 'R':
                self.turn_right()
            elif direction == 'A':
                self.advance()
