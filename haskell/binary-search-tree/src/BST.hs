module BST
    ( BST
    , bstLeft
    , bstRight
    , bstValue
    , empty
    , fromList
    , insert
    , singleton
    , toList
    ) where

data BST a = Empty | Tree a (BST a) (BST a) deriving (Eq, Show)

bstLeft :: BST a -> Maybe (BST a)
bstLeft (Tree _ Empty _) = Nothing
bstLeft (Tree _ left _) = Just left

bstRight :: BST a -> Maybe (BST a)
bstRight (Tree _ _ Empty) = Nothing
bstRight (Tree _ _ right) = Just right

bstValue :: BST a -> Maybe a
bstValue Empty = Nothing
bstValue (Tree value _ _) = Just value

empty :: BST a
empty = Empty

fromList :: Ord a => [a] -> BST a
fromList = foldl (\t x -> insert x t) Empty

insert :: Ord a => a -> BST a -> BST a
insert x Empty = Tree x Empty Empty
insert x t@(Tree value left right)
  | x <= value = Tree value (insert x left) right
  | otherwise = Tree value left (insert x right)

singleton :: a -> BST a
singleton x = Tree x Empty Empty

toList :: BST a -> [a]
toList Empty = []
toList (Tree value left right) = (toList left) ++ [value] ++ (toList right)
