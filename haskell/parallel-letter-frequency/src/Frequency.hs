module Frequency (frequency, executeChunk) where

import Data.List.Split (chunksOf)
import Control.Parallel (par)
import Data.Map  (Map, empty, alter)
import qualified Data.Text as T (Text, foldl')

frequency :: Int -> [T.Text] -> Map Char Int
frequency _ _ = empty
frequency nWorkers texts = 
  let jobs = map executeChunk (chunksOf nWorkers texts)
   in empty

executeChunk :: T.Text -> Map Char Int
executeChunk text = T.foldl' (\memo c -> alter f c memo) empty text
  where f value = case value of Just a -> Just (a + 1)
                                Nothing -> Just 1
