module Series (slices) where
import Data.Char (digitToInt)

slices :: Int -> String -> [[Int]]
slices 0 [] = [[]]
slices _ [] = []
slices n lst@(x:xs)
  | (length lst) < n = []
  | n > 0 = (map digitToInt (x : l)) : (slices n xs)
  | n <= 0 = [] : (slices n xs)
      where l = take (n - 1) xs
