module Beer (song) where
import Data.List (intercalate)

song :: String
song = intercalate "\n\n" [verse i | i <- [99, 98..0]] ++ "\n"

verse :: Int -> String
verse n
  | n == 0 = "No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall."
  | n == 1 = "1 bottle of beer on the wall, 1 bottle of beer.\nTake it down and pass it around, no more bottles of beer on the wall."
  | otherwise = beer_text ++ " of beer on the wall, " ++ beer_text ++ " of beer.\nTake one down and pass it around, " ++ beer (n - 1) False ++ " of beer on the wall."
  where beer_text = beer n True

beer :: Int -> Bool -> String
beer n cap
  | n >= 2 = (show n) ++ " bottles"
  | n == 1 = "1 bottle"
  | n == 0 && cap = "No more bottles"
  | n == 9 && not cap = "no more bottles"
  | otherwise = "99 bottles"
