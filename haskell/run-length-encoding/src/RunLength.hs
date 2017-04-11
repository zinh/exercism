module RunLength (decode, encode) where

import Data.Char

decode :: String -> String
decode encodedText = decode' encodedText 0 []

decode' :: String -> Int -> String -> String
decode' [] _ result = result
decode' (x:xs) n result
  | isNumber x = decode' xs (n * 10 + digitToInt x) result
  | n == 0 = decode' xs 0 (result ++ [x])
  | otherwise = decode' xs 0 (result ++ replicate n x)

encode :: String -> String
encode [] = []
encode (x:xs) = encode' xs x 1 []

encode' :: String -> Char -> Int -> String -> String
encode' [] currentChar currentCount result
  | currentCount == 1 = result ++ [currentChar]
  | otherwise = result ++ show currentCount ++ [currentChar]
encode' (x:xs) currentChar currentCount result
  | x == currentChar = encode' xs currentChar (currentCount + 1) result
  | currentCount == 1 = encode' xs x 1 (result ++ [currentChar])
  | otherwise = encode' xs x 1 (result ++ show currentCount ++ [currentChar])
