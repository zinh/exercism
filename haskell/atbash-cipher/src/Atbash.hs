module Atbash (decode, encode) where

import Data.List (intercalate)
import Data.Char (ord, chr, toLower, isAlphaNum, isNumber)
import Data.List.Split (chunksOf)

decode :: String -> String
decode cipherText = map decodeChar (filter isAlphaNum cipherText)

encode :: String -> String
encode plainText = (intercalate " " . chunksOf 5 . map encodeChar) (filter isAlphaNum plainText)

encodeChar :: Char -> Char
encodeChar c
  | isNumber c = c
encodeChar c =
  let n = (ord . toLower) c
      distanceFromA = n - ord 'a'
  in chr $ ord 'z' - distanceFromA

decodeChar :: Char -> Char
decodeChar c
  | isNumber c = c
decodeChar c =
  let n = (ord . toLower) c
      distanceFromZ = ord 'z' - n
  in chr $ ord 'a' + distanceFromZ
