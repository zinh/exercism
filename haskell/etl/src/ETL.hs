module ETL (transform) where

import Data.Map (Map, toList, fromList)
import Data.Char (toLower)

transform :: Map a String -> Map Char a
transform legacyData = Data.Map.fromList $ foldr f [] (Data.Map.toList legacyData)
  where f (k, x:xs) memo = f (k, xs) ((toLower x, k):memo)
        f (_, []) memo = memo
