module RotationalCipher (rotate) where

import Data.Char (isAlpha, isAscii, ord, chr)

rotate :: Int -> String -> String
rotate n str = map (encrypt n) str

encrypt :: Int -> Char -> Char
encrypt n c
  | c >= 'a' && c <= 'z' = chr $ ord 'a' + ((ord c) - (ord 'a') + n) `mod` 26
  | c >= 'A' && c <= 'Z' = chr $ ord 'A' + ((ord c) - (ord 'A') + n) `mod` 26
  | otherwise = c
