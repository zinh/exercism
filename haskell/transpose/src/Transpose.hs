module Transpose (transpose) where

transpose :: [String] -> [String]
transpose lines = transpose' lines

transpose' :: [String] -> [String]
transpose'  lines
  | all null lines = []
transpose' lines = [head line | line <- lines] : transpose' [tail line | line <- lines]

fillBlank :: [String] -> [String]
fillBlank lines =
  let maxLength = maximum (map length lines)
      fill line = if length line == maxLength then line else line ++ (replicate (maxLength - (length line)) ' ')
   in map fill lines
