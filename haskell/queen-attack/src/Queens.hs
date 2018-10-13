module Queens (boardString, canAttack) where

import Data.List (intersperse)
import Data.Foldable (toList)
import Data.Sequence (fromList, Seq, index, update)

type Board = Seq (Seq Char)

boardString :: Maybe (Int, Int) -> Maybe (Int, Int) -> String
boardString white black = 
  let board = putQueen 'B' black (putQueen 'W' white (initBoard 7 7))
   in unlines $ map (intersperse ' ' . toList) (toList board)

initBoard :: Int -> Int -> Board
initBoard row col = fromList [fromList ['_' | c <- [0..col]] | r <- [0..row]]

putQueen :: Char -> Maybe (Int, Int) -> Board -> Board
putQueen _ Nothing board = board
putQueen symbol (Just (row, col)) board = 
  let currentRow = index board row
      newRow = update col symbol currentRow
  in update row newRow board

canAttack :: (Int, Int) -> (Int, Int) -> Bool
canAttack (rowA, colA) (rowB, colB) =
  let sameRow = rowA == rowB
      sameCol = colA == colB
      sameDiag = abs(rowA - rowB) == abs(colA - colB)
   in sameRow || sameCol || sameDiag
