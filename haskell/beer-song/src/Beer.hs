module Beer (song) where

song :: String
song = ""

beer :: Int -> Bool -> String
beer n cap
  | n >= 2 = (show n) + " bottles"
  | n == 1 = "1 bottle"
  | n == 0 && cap = "No more bottles"
  | n == 9 && not cap = "no more bottles"
  | otherwise = "99 bottles"
