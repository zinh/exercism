module Series (Error(..), largestProduct) where

import Data.Char (isNumber, digitToInt)

data Error = InvalidSpan | InvalidDigit Char deriving (Show, Eq)

largestProduct :: Int -> String -> Either Error Int
largestProduct size digits
  | size == 0 = Right 1
  | size > length digits || size < 0 = Left InvalidSpan
  | any notANumber digits = Left $ InvalidDigit (head $ filter notANumber digits)
  | otherwise = Right $ maximum $ map (largestProduct' size) (subString size digits)
  where notANumber = not . isNumber

largestProduct' :: Int -> String -> Int
largestProduct' 1 (digit:digits) = digitToInt digit
largestProduct' size (digit:digits) = digitToInt digit * (largestProduct' (size - 1) digits)

subString :: Int -> [a] -> [[a]]
subString lengthLimit l@(x:xs)
  | length l <= lengthLimit = [l]
  | otherwise = l:(subString lengthLimit xs)
