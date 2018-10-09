module CryptoSquare (encode) where

import Data.List (intercalate)
import Data.Char (isAlphaNum, toLower)
import Data.List.Split (chunksOf)

encode :: String -> String
encode "" = ""
encode xs =
  let xss = normalize xs
      (row, col) = (bound . length) xss
   in intercalate " " (reorder (breakLine row col xss))

normalize :: String -> String
normalize text = [toLower c | c <- text, isAlphaNum c ]

bound :: Int -> (Int, Int)
bound len = (head . (filter valid)) [(divCeil len col, col) | col <- [1..len]]
  where valid (r, c) = c - r >= 0 && c - r <= 1

breakLine :: Int -> Int -> String -> [String]
breakLine row col xs = chunksOf col xs

reorder :: [String] -> [String]
reorder xs
  | all null xs = []
reorder xs = [if null x then ' ' else head x | x <- xs] : reorder [if null x then [] else tail x | x <- xs]

divCeil :: Int -> Int -> Int
divCeil a b =
  let m = a `mod` b
   in if m > 0 then a `div` b + 1 else a `div` b
