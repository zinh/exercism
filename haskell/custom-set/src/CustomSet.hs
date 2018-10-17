module CustomSet
  ( delete
  , difference
  , empty
  , fromList
  , insert
  , intersection
  , isDisjointFrom
  , isSubsetOf
  , member
  , null
  , size
  , toList
  , union
  ) where

import Prelude hiding (null)

--data CustomSet a = Dummy deriving (Eq, Show)
newtype CustomSet a = L [a] deriving (Show)

instance Eq a => Eq (CustomSet a) where
  --(==) :: Eq a => CustomSet a -> CustomSet a -> Bool
  setA == setB = null (difference setA setB) && null (difference setB setA)

delete :: Eq a => a -> CustomSet a -> CustomSet a
delete _ (L []) = empty
delete x (L ys) = L (filter (\y -> y /= x) ys)

difference :: Eq a => CustomSet a -> CustomSet a -> CustomSet a
difference setA (L []) = setA
difference setA (L (y:ys)) = difference (delete y setA) (L ys)

empty :: CustomSet a
empty = L []

fromList :: Eq a => [a] -> CustomSet a
fromList xs = foldr insert empty xs

insert :: Eq a => a -> CustomSet a -> CustomSet a
insert x (L set)
  | x `elem` set = L set
  | otherwise = L (x:set)

intersection :: Eq a => CustomSet a -> CustomSet a -> CustomSet a
intersection setA setB = difference setA (difference setA setB)

isDisjointFrom :: Eq a => CustomSet a -> CustomSet a -> Bool
isDisjointFrom setA setB = null (intersection setA setB)

isSubsetOf :: Eq a => CustomSet a -> CustomSet a -> Bool
isSubsetOf setA setB = null (difference setA setB)

member :: Eq a => a -> CustomSet a -> Bool
member x (L set) = x `elem` set

null :: CustomSet a -> Bool
null (L set) = 
  case set of [] -> True
              otherwise -> False

size :: CustomSet a -> Int
size (L set) = length set

toList :: CustomSet a -> [a]
toList (L set) = set

union :: Eq a => CustomSet a -> CustomSet a -> CustomSet a
union setA (L setB) = foldr insert setA setB
