module Anagram (anagramsFor) where
import Data.List (sort)
import Data.Char (toLower)

anagramsFor :: String -> [String] -> [String]
anagramsFor xs xss = foldr (\str result -> if sortStr str == sorted && normalized str /= normalized xs then str:result else result) [] xss
  where normalized str = map toLower str
        sortStr = sort . normalized
        sorted = sortStr xs
