from cmath import sqrt, exp, sin, cos
from math import pi

class ComplexNumber(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        r = self.real * other.real - self.imaginary * other.imaginary
        i = self.real * other.imaginary + self.imaginary * other.real
        return ComplexNumber(r, i)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __truediv__(self, other):
        norminator = self * other.conjugate()
        denominator = other * other.conjugate()
        return ComplexNumber(norminator.real / denominator.real, norminator.imaginary / denominator.real)

    def __abs__(self):
        return sqrt(self.real**2 + self.imaginary**2)

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        ex = exp(self.real)
        if self.imaginary == pi:
            return ComplexNumber(ex * cos(self.imaginary), 0)
        return ComplexNumber(ex * cos(self.imaginary), ex * sin(self.imaginary))

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

    def __repr__(self):
        return f"{self.real} + {self.imaginary}i"
