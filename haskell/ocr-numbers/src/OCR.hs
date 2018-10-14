module OCR (convert) where

import Data.List.Split (chunksOf)

m :: [(Int, [String])]
m =  [('0', [" _ ", "| |", "|_|"]), ('1', ["   ", "  |", "  |"]), ('2', [" _ ", " _|", "|_ "]), 
         ('3', [" _ ", " _|", " _|"]), ('4', ["   ", "|_|", "  |"]), ('5', [" _ ", "|_ ", " _|"]), 
         ('6', [" _ ", "|_ ", "|_|"]), ('7', [" _ ", "  |", "  |"]), ('8', [" _ ", "|_|", "|_|"]), 
         ('9', [" _ ", "|_|", " _|"])]

matchNumber :: [String] -> Char
matchNumber rows =
  let compareBitmap (number, bitmaps) = all (\(row, bitmap) -> row == bitmap) (zip rows bitmaps)
      matched = filter compareBitmap m
   in case matched of
        [] -> "?"
        (number, _):_ -> show number

convert :: String -> String
convert input =
  let xs = lines input
      map (\rows -> [chunksOf 3 row | row <- rows]) (chunksOf 4 xs)
   in matchedNumber
