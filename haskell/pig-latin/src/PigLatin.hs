module PigLatin (translate) where

import Data.List.Split (splitOn)
import Data.List (intercalate)

translate :: String -> String
translate xs = intercalate " " $ map translateWord (splitOn " " xs)

translateWord :: String -> String
translateWord xs
  | startVowel xs = xs ++ "ay" 
  | quAtSecondPosition xs = tail (moveConsonantUntil ('u'==) xs) ++ "uay"
  | yAfterConsonants xs = moveConsonantUntil ('y'==) xs ++ "ay"
  | otherwise = (moveConsonantUntil isVowel xs) ++ "ay"

startVowel :: String -> Bool
startVowel ('y':'t':_) = True
startVowel ('x':'r':_) = True
startVowel (c:_) = isVowel c
startVowel _ = False

quAtSecondPosition :: String -> Bool
quAtSecondPosition ('q':'u':_) = True
quAtSecondPosition (c:'q':'u':_) = not (isVowel c)
quAtSecondPosition _ = False

isVowel :: Char -> Bool
isVowel c = any (c==) ['a', 'e', 'i', 'o', 'u']

yAfterConsonants :: String -> Bool
yAfterConsonants (c:'y':_) = if isVowel c then False else True
yAfterConsonants (c:xs) = if isVowel c then False else yAfterConsonants xs
yAfterConsonants [] = False

twoLetterEndWithY :: String -> Bool
twoLetterEndWithY (c:'y':[]) = True
twoLetterEndWithY _ = False

moveConsonantUntil :: (Char -> Bool) -> String -> String
moveConsonantUntil _ [] = []
moveConsonantUntil f xss@(x:xs) = if f x then xss else moveConsonantUntil f (xs ++ [x])
