module DNA (nucleotideCounts) where

import Data.Map (Map, fromList, lookup, insert)

nucleotideCounts :: String -> Either String (Map Char Int)
nucleotideCounts xs = foldr nucleotideCounts' (Right (fromList [('A',0),('C',0),('G',0),('T',0)])) xs

nucleotideCounts' :: Char -> Either String (Map Char Int) -> Either String (Map Char Int)
nucleotideCounts' _ (Left s) = Left s
nucleotideCounts' x (Right m) = case Data.Map.lookup x m of
                                  Just n -> Right (Data.Map.insert x (n + 1) m)
                                  otherwise -> Left "Invalid Strand"
