module Triangle (rows) where

rows :: Int -> [[Integer]]
rows x = (reverse . rows') x

rows' :: Int -> [[Integer]]
rows' x
  | x <= 0 = []
rows' 1 = [[1]]
rows' 2 = [[1, 1], [1]]
rows' x =
  let triangle@(r:_) = rows' (x - 1)
  in (1:(nextRow r)) : triangle

nextRow :: [Integer] -> [Integer]
nextRow [] = []
nextRow (x:[]) = [1]
nextRow (x1:xs@(x2:_)) = (x1 + x2) : (nextRow xs)
