module Pangram (isPangram) where

import Data.Char

isPangram :: String -> Bool
isPangram text = 
  let result = foldr (\c lst -> filter (toLower(c)/=) lst) ['a'..'z'] text
  in length(result) == 0
