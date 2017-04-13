module Acronym (abbreviate) where

abbreviate :: String -> String
abbreviate xs = words xs

reduceWord :: String -> Char -> String
reduceWord word previousChar
