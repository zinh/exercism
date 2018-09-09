from __future__ import division
from math import gcd


class Rational(object):
    def __init__(self, numer, denom):
        d = gcd(numer, denom)
        if denom < 0:
            self.numer = -numer // d
            self.denom = -denom // d
        else:
            self.numer = numer // d
            self.denom = denom // d

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return Rational(self.numer * other.denom + self.denom * other.numer, self.denom * other.denom)
        self.denom = n.denom()
        self.numer = n.numer()

    def __sub__(self, other):
        return Rational(self.numer * other.denom - self.denom * other.numer, self.denom * other.denom)

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return Rational(self.numer * other.denom, self.denom * other.numer)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        return Rational(self.numer ** power, self.denom ** power)

    def __rpow__(self, base):
        return base ** (self.numer / self.denom)

print(Rational(-1, 2) - Rational(-2, 3))
