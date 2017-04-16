module Hamming (distance) where

distance :: String -> String -> Maybe Int
distance xs ys
  | length xs /= length ys = Nothing
  | otherwise = Just $ foldr f 0 (zip xs ys)
      where f (a,b) memo
              | a == b = memo
              | otherwise = memo + 1
