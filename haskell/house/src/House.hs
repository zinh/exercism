module House (rhyme) where

import Data.List (intercalate)

rhyme :: String
rhyme = intercalate "\n\n" $ [if n == 12 then reciteVerse n ++ "\n" else reciteVerse n | n <- [1..12]]

m :: [(String, String)]
m = [("the house that Jack built", "lay in"),
  ("the malt","ate"),
  ("the rat","killed"),
  ("the cat","worried"),
  ("the dog","tossed"),
  ("the cow with the crumpled horn","milked"),
  ("the maiden all forlorn","kissed"),
  ("the man all tattered and torn","married"),
  ("the priest all shaven and shorn","woke"),
  ("the rooster that crowed in the morn","kept"),
  ("the farmer sowing his corn","belonged to"),
  ("the horse and the hound and the horn","")]

reciteVerse :: Int -> String
reciteVerse 1 = "This is the house that Jack built."
reciteVerse n = intercalate "\n" $ reverse [if s == n - 1 then "This is " ++ fst (m !! s) else "that " ++ (snd (m !! s)) ++ " " ++ (fst (m !! s)) ++ if s == 0 then "." else ""| s <- [0..(n - 1)]]
