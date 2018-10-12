module Luhn (isValid) where

import Data.Char (ord, isDigit)

isValid :: String -> Bool
isValid n =
  let filteredDigit = filter isDigit n
      total = snd $ foldr parse (0, 0) filteredDigit
  in case filteredDigit of
       (x:[]) -> False
       otherwise -> total `mod` 10 == 0

parse :: Char -> (Int, Int) -> (Int, Int)
parse c (pos, total) =
  if pos `mod` 2 == 0 then
    (pos + 1, total + num)
  else
    (pos + 1, total + (double num))
  where double number = if number <= 4 then number * 2 else number * 2 - 9
        num = (ord c) - (ord '0')
