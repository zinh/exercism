module WordCount (wordCount) where

import Data.Char (isAlphaNum, toLower)
import qualified Data.Map as Map

wordCount :: String -> [(String, Int)]
wordCount = Map.toList . (foldl countWord Map.empty) . (map normalizeWord) . (filter isWord) . words . concatMap preprocess

preprocess :: Char -> String
preprocess c
  | c == ',' = ", "
  | otherwise = [c]

isWord :: String -> Bool
isWord word
  | length word == 1 && not (isAlphaNum(word !! 0)) = False
  | otherwise = True

normalizeWord :: String -> String
normalizeWord = (map toLower) . reverse . removePrefix . reverse . removePrefix

removePrefix :: String -> String
removePrefix (c:[]) = [c]
removePrefix xss@(c:xs) = if isAlphaNum c then xss else removePrefix xs

countWord :: Map.Map String Int -> String -> Map.Map String Int
countWord m word = 
  let c = Map.findWithDefault 0 word m
  in Map.insert word (c + 1) m
