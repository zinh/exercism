module OCR (convert) where

import Data.List.Split (chunksOf)
import Data.List (intercalate)

m :: [(Char, [String])]
m =  [('0', [" _ ", "| |", "|_|"]), ('1', ["   ", "  |", "  |"]), ('2', [" _ ", " _|", "|_ "]), 
         ('3', [" _ ", " _|", " _|"]), ('4', ["   ", "|_|", "  |"]), ('5', [" _ ", "|_ ", " _|"]), 
         ('6', [" _ ", "|_ ", "|_|"]), ('7', [" _ ", "  |", "  |"]), ('8', [" _ ", "|_|", "|_|"]), 
         ('9', [" _ ", "|_|", " _|"])]

matchNumber :: [String] -> Char
matchNumber rows =
  let compareBitmap (number, bitmaps) = all (\(row, bitmap) -> row == bitmap) (zip rows bitmaps)
      matched = filter compareBitmap m
   in case matched of
        [] -> '?'
        (number, _):_ -> number

convert :: String -> String
--convert xs = error "Not implemented"
convert input =
  let xs = lines input
      matchedNumber = intercalate "," $ map (cutRows matchNumber) (chunksOf 4 xs)
   in matchedNumber

cutRows :: ([[a]] -> b) -> [[a]] -> [b]
cutRows _ rows
  | all null rows = []
cutRows f rows = f (map (take 3) rows) : cutRows f (map (drop 3) rows)
