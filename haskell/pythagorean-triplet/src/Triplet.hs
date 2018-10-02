module Triplet (isPythagorean, mkTriplet, pythagoreanTriplets) where
import Data.List (sort)

isPythagorean :: (Int, Int, Int) -> Bool
isPythagorean (a, b, c) =
  let (a1:b2:c1:_)  = sort [a, b, c]
  in c1*c1 == a1*a1 + b2*b2

mkTriplet :: Int -> Int -> Int -> (Int, Int, Int)
mkTriplet a b c = (a, b, c)

pythagoreanTriplets :: Int -> Int -> [(Int, Int, Int)]
pythagoreanTriplets minFactor maxFactor = [(a, b, c) | a <- [minFactor..maxFactor], b <- [a..maxFactor], c <- [b..maxFactor], a*a + b*b == c*c]
