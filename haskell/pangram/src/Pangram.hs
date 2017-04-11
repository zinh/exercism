module Pangram (isPangram) where

import Data.Char

isPangram :: String -> Bool
isPangram = isPangram' . convertUpper

isPangram' :: String -> Bool
isPangram' text = 
  let result = foldr (\c lst -> filter (c/=) lst) ['a'..'z'] text
  in length(result) == 0

convertUpper :: String -> String
convertUpper = foldr f []
  where f c str
          | c >= 'A' && c <= 'Z' = (chr $ (ord 'a') + (ord c) - (ord 'A')) : str
          | otherwise = c:str
