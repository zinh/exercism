module Isogram (isIsogram) where
import qualified Data.Map as Map

isIsogram :: String -> Bool
isIsogram = foldl (\acc c -> if Map.member acc c && then ) True Map.empty
