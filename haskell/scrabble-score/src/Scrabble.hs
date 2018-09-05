module Scrabble (scoreLetter, scoreWord) where
import Data.Char (toUpper)

scoreLetter :: Char -> Integer
scoreLetter letter
  | capitalizedLetter `elem` "AEIOULNRST" = 1
  | capitalizedLetter `elem` "DG" = 2
  | capitalizedLetter `elem` "BCMP" = 3
  | capitalizedLetter `elem` "FHVWY" = 4
  | capitalizedLetter `elem` "K" = 5
  | capitalizedLetter `elem` "JX" = 8
  | capitalizedLetter `elem` "QZ" = 10
  | otherwise = 0
  where capitalizedLetter = toUpper letter

scoreWord :: String -> Integer
scoreWord word = foldl (\memo c -> memo + (scoreLetter c)) 0 word
