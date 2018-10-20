module Frequency (frequency, countChar) where

import Data.List.Split (chunksOf)
import Control.Parallel (par)
import Data.Map  (Map, empty, alter, unionWith)
import Data.Char (isLetter)
import qualified Data.Text as T (Text, unpack, toLower)

frequency :: Int -> [T.Text] -> Map Char Int
frequency nWorkers texts = 
  let jobs = chunksOf nWorkers (concat (map (T.unpack . T.toLower) texts))
      results = parMap countChar jobs
   in foldr (unionWith (+)) empty results

countChar :: String -> Map Char Int
countChar s = foldr (\char m -> alter f char m) empty (filter isLetter s)
  where f count = case count of Just c -> Just (c + 1)
                                Nothing -> Just 1

parMap :: (a -> b) -> [a] -> [b]
parMap _ [] = []
parMap f (x:xs) = f x `par` f x : (parMap f xs)
