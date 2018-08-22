module Isogram (isIsogram) where
import qualified Data.Map as Map
import Data.Char (toLower)

isIsogram :: String -> Bool
isIsogram str = fst $ foldl (\(result, acc) originalChar -> 
  let c = toLower originalChar in
  if c < 'a' || c > 'z' 
    then (True, acc) 
    else if not result || Map.member c acc 
      then (False, acc) 
      else (True, Map.insert c True acc)) 
  (True, Map.empty) str
