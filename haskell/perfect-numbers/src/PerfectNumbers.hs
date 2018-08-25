module PerfectNumbers (classify, Classification(..)) where

data Classification = Deficient | Perfect | Abundant deriving (Eq, Show)

classify :: Int -> Maybe Classification
classify num
  | num < 1 = Nothing
classify num 
  | s == num = Just Perfect
  | s < num = Just Deficient
  | otherwise = Just Abundant
  where s = foldr (\x acc -> if num `mod` x == 0 then acc + x else acc) 0 [1..(div num 2)]
