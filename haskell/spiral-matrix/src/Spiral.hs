module Spiral (spiral) where

import Data.Array (Array, listArray)

spiral :: Int -> [[Int]]
spiral 0 = []
spiral n = spiralArray listArray (0, n - 1) [listArray (0, n - 1) [0 | j <- [0..(n - 1)]] | i <- [0..(n - 1)]]
