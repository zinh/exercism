module SumOfMultiples (sumOfMultiples) where

sumOfMultiples :: [Integer] -> Integer -> Integer
sumOfMultiples factors limit = sum $ filter (`divisible` factors) [1..(limit - 1)]

divisible :: Integer -> [Integer] -> Bool
divisible num = any (\factor -> num `mod` factor == 0)
