module PrimeFactors (primeFactors) where

primeFactors :: Integer -> [Integer]
primeFactors 0 = []
primeFactors 1 = []
primeFactors n = 
  let factors = filter (\i -> n `mod` i == 0) [2..(round . sqrt . fromInteger) n]
  in case factors of
    [] -> [n]
    (x:xs) -> x : (primeFactors (n `div` x))
