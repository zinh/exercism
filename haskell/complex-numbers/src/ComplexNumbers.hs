module ComplexNumbers
(Complex,
 conjugate,
 abs,
 real,
 imaginary,
 mul,
 add,
 sub,
 div,
 complex) where

import Prelude hiding (div, abs)

-- Data definition -------------------------------------------------------------
data Complex a = Complex a a deriving(Eq, Show)

complex :: (a, a) -> Complex a
complex (r, m) = Complex r m

-- unary operators -------------------------------------------------------------
conjugate :: Num a => Complex a -> Complex a
conjugate (Complex a b) = Complex a (-b)

abs :: Floating a => Complex a -> a
abs (Complex r i) = sqrt $ r ^ 2 + i ^ 2

real :: Num a => Complex a -> a
real (Complex r _) = r

imaginary :: Num a => Complex a -> a
imaginary (Complex _ i) = i

-- binary operators ------------------------------------------------------------
mul :: Num a => Complex a -> Complex a -> Complex a
mul (Complex a b) (Complex c d) = Complex (a * c - b * d) (b * c + a * d)

add :: Num a => Complex a -> Complex a -> Complex a
add (Complex a b) (Complex c d) = Complex (a + c) (b + d)

sub :: Num a => Complex a -> Complex a -> Complex a
sub (Complex a b) (Complex c d) = Complex (a - c) (b - d)

div :: Fractional a => Complex a -> Complex a -> Complex a
div (Complex a b) f@(Complex c d) = Complex r i
  where l1 = c^2 + d^2
        r = (a * c + b * d) / l1
        i = (b * c - a * d) / l1
