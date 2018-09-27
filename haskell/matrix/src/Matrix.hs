module Matrix
    ( Matrix
    , cols
    , column
    , flatten
    , fromList
    , fromString
    , reshape
    , row
    , rows
    , shape
    , transpose
    ) where

import qualified Data.Vector (Vector, fromList, empty)

data Matrix a = M [[a]] deriving (Eq, Show)

cols :: Matrix a -> Int
cols (M []) = 0
cols (M (row:xs)) = length row

column :: Int -> Matrix a -> Data.Vector.Vector a
column x matrix = error "You need to implement this function."

flatten :: Matrix a -> Data.Vector.Vector a
flatten (M xss) = Data.Vector.fromList $ foldl (++) [] xss

fromList :: [[a]] -> Matrix a
fromList xss = M xss

fromString :: Read a => String -> Matrix a
fromString xs = fromList $ map convertRow (lines xs)
  where convertRow row = map (\x -> (read x)) (words row)

reshape :: (Int, Int) -> Matrix a -> Matrix a
reshape dimensions matrix = error "You need to implement this function."

row :: Int -> Matrix a -> Data.Vector.Vector a
row x matrix = error "You need to implement this function."

rows :: Matrix a -> Int
rows (M xss) = length xss

shape :: Matrix a -> (Int, Int)
shape (M xss@(row:xs)) = (length xss, length row)

transpose :: Matrix a -> Matrix a
transpose matrix = error "You need to implement this function."
