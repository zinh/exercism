from math import sin, cos, pi
# Globals for the bearings
# Change the values as you see fit
EAST = (1, 0)
NORTH = (0, 1)
WEST = (-1, 0)
SOUTH = (0, -1)


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.x = x
        self.y = y

    @property
    def coordinates(self):
        return (self.x, self.y)

    def turn_right(self):
        r = self.rotate(-pi/2)
        bearing = self.bearing
        self.bearing = self.mul(r, bearing)

    def turn_left(self):
        r = self.rotate(pi/2)
        bearing = self.bearing
        self.bearing = self.mul(r, bearing)

    def advance(self):
        self.x = self.x + self.bearing[0]
        self.y = self.y + self.bearing[1]

    def rotate(self, deg):
        return ([int(cos(deg)), -int(sin(deg))], [int(sin(deg)), int(cos(deg))])

    def mul(self, r, v):
        return (r[0][0] * v[0] + r[0][1] * v[1], r[1][0] * v[0] + r[1][1] * v[1])

    def simulate(self, path):
        for direction in path:
            if direction == 'L':
                self.turn_left()
            elif direction == 'R':
                self.turn_right()
            elif direction == 'A':
                self.advance()
