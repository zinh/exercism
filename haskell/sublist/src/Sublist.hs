module Sublist (Sublist(..), sublist) where

data Sublist = Equal | Sublist | Superlist | Unequal deriving (Eq, Show)

sublist :: [a] -> [a] -> Sublist
sublist [] [] = Equal
sublist [] _ = Sublist
sublist _ [] = Superlist
sublist xs ys = error ""
sublist xss@(x:xs) yss@(y:ys)
  | x == y = sublist xs ys
  | otherwise = sublist xss ys
  where s1 = sublist xss ys
        s2 = sublist xs yss
