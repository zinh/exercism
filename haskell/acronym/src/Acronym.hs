module Acronym (abbreviate) where
import Data.Char

abbreviate :: String -> String
abbreviate xs = foldl f [] (words xs)
  where f memo x = memo ++ reduceOrFirst(x)

reduceWord :: String -> String
reduceWord [] = []
reduceWord (x:xs) 
  | isUpper x = x : (reduceWord xs)
  | otherwise = reduceWord xs

reduceOrFirst :: String -> String
reduceOrFirst [] = []
reduceOrFirst s@(x:xs)
  | isCap s = [x]
  | reduce == [] = [toUpper x]
  | otherwise = reduce
  where reduce = reduceWord s

isCap :: [Char] -> Bool
isCap [] = True
isCap (x:xs)
  | x >= 'a' && x <= 'z' = False
  | otherwise = isCap xs

splitStr :: String -> Char -> [String]
splitStr str delim = foldr f [""] str
  where f x m@(y:ys) = case x of
          ' ' ->  "" : m
          delim -> "" : m
          _ -> (x:y):ys
