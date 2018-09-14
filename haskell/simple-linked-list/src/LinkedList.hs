{-# LANGUAGE BangPatterns #-}
module LinkedList
    ( LinkedList
    , datum
    , fromList
    , isNil
    , new
    , next
    , nil
    , reverseLinkedList
    , toList
    ) where

import Prelude hiding (foldl')

data LinkedList a = Cons a (LinkedList a) | Empty deriving (Eq, Show)

datum :: LinkedList a -> a
datum (Cons head _) = head

fromList :: [a] -> LinkedList a
fromList xs = foldr (\x memo -> Cons x memo) Empty xs

isNil :: LinkedList a -> Bool
isNil Empty = True
isNil _ = False

new :: a -> LinkedList a -> LinkedList a
new x linkedList = Cons x linkedList

next :: LinkedList a -> LinkedList a
next (Cons _ tail) = tail
next Empty = Empty

nil :: LinkedList a
nil = Empty

foldl' :: (LinkedList a -> a -> LinkedList a) -> LinkedList a -> LinkedList a -> LinkedList a
foldl' _ z Empty = z
foldl' f !z (Cons x xs) = foldl' f (f z x) xs

reverseLinkedList :: LinkedList a -> LinkedList a
reverseLinkedList lst = foldl' (\memo x -> Cons x memo) Empty lst

toList :: LinkedList a -> [a]
toList (Cons h t) = h:(toList t)
toList Empty = []
