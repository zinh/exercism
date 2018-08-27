module Raindrops (convert) where
import Data.List (intercalate)

convert :: Int -> String
convert n = 
  let divisions = [mapN d | d <- [3, 5, 7], mod n d == 0]
  in case divisions of
    [] -> show n
    _ -> intercalate "" divisions

mapN :: Int -> String
mapN 3 = "Pling"
mapN 5 = "Plang"
mapN 7 = "Plong"
