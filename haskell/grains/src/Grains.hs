module Grains (square, total) where

square :: Integer -> Maybe Integer
square n
  | n >= 1 && n <= 64 = Just (2^(n - 1))
  | otherwise = Nothing

total :: Integer
total = foldr f 0 [0..63]
  where f n sum = sum + 2^n
