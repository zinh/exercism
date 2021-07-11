module Palindromes (largestPalindrome, smallestPalindrome) where

import Data.Ord (comparing)
import Data.Foldable (maximumBy)

largestPalindrome :: Integer -> Integer -> (Integer, [(Integer, Integer)])
largestPalindrome minFactor maxFactor = (p, factor p minFactor maxFactor)
  where upper = maxFactor * maxFactor
        lower = minFactor * minFactor
        p = (head . (filter isPalindrome)) [i | i <- [upper, (upper - 1)..lower]]

smallestPalindrome :: Integer -> Integer -> (Integer, [(Integer, Integer)])
smallestPalindrome minFactor maxFactor = (p, factor p minFactor maxFactor)
  where upper = maxFactor * maxFactor
        lower = minFactor * minFactor
        p = (head . (filter isPalindrome)) [i | i <- [lower..upper]]

isPalindrome :: Integer -> Bool
isPalindrome n = show n == (reverse . show) n

factor :: Integer -> Integer -> Integer -> [(Integer, Integer)]
factor n lower upper = [(i, j) | i <- [realLower..realUpper], j <- [i..realUpper], i * j == n]
  where realLower = n `div` upper
        realUpper = n `div` lower
