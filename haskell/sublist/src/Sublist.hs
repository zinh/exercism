module Sublist (Sublist(..), sublist) where

data Sublist = Equal | Sublist | Superlist | Unequal deriving (Eq, Show)

sublist :: Eq a => [a] -> [a] -> Sublist
sublist [] [] = Equal
sublist [] _ = Sublist
sublist _ [] = Superlist
sublist xs ys
  | s1 && s2 = Equal
  | s1 = Sublist
  | s2 = Superlist
  | otherwise = Unequal
  where s1 = xs `sublistOf` ys
        s2 = ys `sublistOf` xs


sublistOf :: Eq a => [a] -> [a] -> Bool
sublistOf [] [] = True
sublistOf _ [] = False
sublistOf [] _ = False
sublistOf xs yss@(y:ys)
  | sublistOf' xs yss = True
  | otherwise = sublistOf xs ys

sublistOf' :: Eq a => [a] -> [a] -> Bool
sublistOf' [] [] = True
sublistOf' _ [] = False
sublistOf' [] _ = True
sublistOf' (x:xs) (y:ys)
  | x == y = sublistOf' xs ys
  | otherwise = False
