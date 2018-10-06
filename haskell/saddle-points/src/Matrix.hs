module Matrix (saddlePoints) where

import Data.Array (Array, bounds, (!))

saddlePoints :: Ord e => Array (Int, Int) e -> [(Int, Int)]
saddlePoints matrix = [(row, col) | row <- [0..rows], col <- [0..cols], isSaddle row col matrix]
  where (_, (rows, cols)) = bounds matrix

isSaddle :: Ord e => Int -> Int -> Array (Int, Int) e -> Bool
isSaddle rowNo colNo matrix = element >= (maximum currentRow) && element <= (minimum currentCol)
  where currentRow = rows matrix rowNo
        currentCol = cols matrix colNo
        element = matrix ! (rowNo, colNo)

rows :: Array (Int, Int) e -> Int -> [e]
rows matrix rowNo = [matrix ! (rowNo, col) | col <- [0..cols]]
  where (_, (_, cols)) = bounds matrix

cols :: Array (Int, Int) e -> Int -> [e]
cols matrix colNo = [matrix ! (row, colNo) | row <- [0..rows]]
  where (_, (rows, _)) = bounds matrix
