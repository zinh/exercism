module Palindromes (largestPalindrome, smallestPalindrome) where

import Data.Ord (comparing)
import Data.Foldable (maximumBy)

largestPalindrome :: Integer -> Integer -> (Integer, [(Integer, Integer)])
largestPalindrome minFactor maxFactor = 
  let p = maximumBy (comparing fst) (filter (isPalindrome . fst) [(i * j, (i, j)) | i <- [maxFactor, (maxFactor - 1)..minFactor], j <- [i, (i - 1)..minFactor]])
   in (fst p, [snd p])

smallestPalindrome :: Integer -> Integer -> (Integer, [(Integer, Integer)])
smallestPalindrome minFactor maxFactor = 
  let p = head (filter (isPalindrome . fst) [(i * j, (i, j)) | i <- [minFactor..maxFactor], j <- [minFactor..i]])
   in (fst p, [snd p])

isPalindrome :: Integer -> Bool
isPalindrome n = show n == (reverse . show) n
