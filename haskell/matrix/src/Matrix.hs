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

import qualified Data.Vector (Vector, fromList, empty, toList)
import Data.List.Split (chunksOf)
import Debug.Trace (trace)

data Matrix a = M [[a]] deriving (Eq, Show)

cols :: Matrix a -> Int
cols (M []) = 0
cols (M (row:xs)) = length row

column :: Show a => Int -> Matrix a -> Data.Vector.Vector a
column 0 matrix =
  let (_, col) = firstColumn matrix
  in Data.Vector.fromList col
column x matrix =
  let (rest, _) = firstColumn matrix
  in column (x - 1) rest

flatten :: Matrix a -> Data.Vector.Vector a
flatten (M xss) = Data.Vector.fromList $ foldl (++) [] xss

fromList :: [[a]] -> Matrix a
fromList xss = M xss

fromString :: Read a => String -> Matrix a
fromString "" = M []
fromString xs = fromList $ map convertRow (lines xs)
  where convertRow row = map read (words row)

reshape :: (Int, Int) -> Matrix a -> Matrix a
reshape (r, c) matrix = fromList $ chunksOf c ((Data.Vector.toList . flatten) matrix)

row :: Int -> Matrix a -> Data.Vector.Vector a
row 0 (M (r:xss))  = Data.Vector.fromList r
row x (M (r:xss)) = row (x - 1) (M xss)

rows :: Matrix a -> Int
rows (M xss) = length xss

shape :: Matrix a -> (Int, Int)
shape (M []) = (0,0)
shape (M xss@(row:xs)) = (length xss, length row)

transpose :: Show a => Matrix a -> Matrix a
transpose (M []) = M []
transpose matrix =
  let (rest, col) = firstColumn matrix
      M r = transpose rest
  in if (null col) then (M []) else M (col : r)

firstColumn :: Show a => Matrix a -> (Matrix a, [a])
firstColumn (M []) = (M [], [])
firstColumn (M ([]:xss)) = (M [], [])
firstColumn (M ((cell:row):xss)) =
  let (M rest, col) = firstColumn (M xss)
  in (M (row:rest), cell:col)
