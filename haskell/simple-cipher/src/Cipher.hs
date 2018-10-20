module Cipher (caesarDecode, caesarEncode, caesarEncodeRandom) where

import Data.Char (ord, chr)
import System.Random
import Data.Array.IO
import Control.Monad

caesarDecode :: String -> String -> String
caesarDecode key encodedText = map decode $ zip encodedText (cycle key)
  where decode (c, k) = chr $ ord 'a' + ((ord c - ord 'a' - ord k + ord 'a') `mod` 26)

caesarEncode :: String -> String -> String
caesarEncode key text = map encode $ zip text (cycle key)
  where encode (c, k) = chr $ ord 'a' + ((ord c - ord 'a' + ord k - ord 'a') `mod` 26)

caesarEncodeRandom :: String -> IO (String, String)
caesarEncodeRandom text = do
  key <- shuffle (take 1000 (cycle ['a'..'z']))
  return (key, caesarEncode key text)

shuffle :: [a] -> IO [a]
shuffle xs = do
  ar <- newArray n xs
  forM [1..n] $ \i -> do
      j <- randomRIO (i,n)
      vi <- readArray ar i
      vj <- readArray ar j
      writeArray ar j vi
      return vj
  where
    n = length xs
    newArray :: Int -> [a] -> IO (IOArray Int a)
    newArray n xs =  newListArray (1,n) xs
