module Isogram (isIsogram) where
import qualified Data.Map as Map
import Data.Char (toLower)

isIsogram :: String -> Bool
isIsogram str = fst $ foldl (\(result, acc) c -> if (toLower c) < 'a' || (toLower c) > 'z' then (True, acc) else if not result || Map.member (toLower c) acc then (False, acc) else (True, Map.insert (toLower c) True acc)) (True, Map.empty) str
