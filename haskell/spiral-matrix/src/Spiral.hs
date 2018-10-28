module Spiral (spiral) where

--import Data.Array (Array, listArray)

spiral :: Int -> [[Int]]
spiral 0 = []

spiral :: Int -> Int -> [[Int]]
spiral size topLeft n =
  let topRight = topLeft + n - 1
      bottomRight = 2 * (n - 1) + 1
      bottomLeft = bottomRight + n - 1
      innerMatrix = spiral (n - 1)
      firstRow = [i | i <- [topLeft..topRight]]
      lastRow = reverse [i | i <- [bottomRight..bottomLeft]]
   in firstRow : (appendNumber (topRight + 1) innerMatrix) ++ [lastRow]

appendNumber :: Int -> Int -> [[Int]] -> [[Int]]
appendNumber _ _ [] = []
appendNumber h t (xs:xss) = ((h : xs) ++ [t]) : appendNumber (h + 1) (t - 1) xs
