module Sieve (primesUpTo) where

primesUpTo :: Integer -> [Integer]
primesUpTo k = 
  let compoundNumbers = [i * n | n <- [2..k], i <- [2..k]]
   in [i | i <- [2..k], not (elem i compoundNumbers)]
