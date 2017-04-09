module Bob (responseFor) where

responseFor :: String -> String
responseFor xs
  | allUpper xs = "Whoa, chill out!"
  | endWithQuestion xs = "Sure."
  | allNonCharacter xs = "Fine. Be that way!"
  | otherwise = "Whatever."

allUpper :: String -> Bool
allUpper [] = True
allUpper (x:xs) 
  | x >= 'a' && x <= 'z' = False
  | otherwise = allUpper xs

endWithQuestion :: String -> Bool
endWithQuestion [] = False
endWithQuestion "?" = True
endWithQuestion (x:xs) = endWithQuestion xs

endWithExclamation :: String -> Bool
endWithExclamation [] = False
endWithExclamation "!" = True
endWithExclamation (x:xs) = endWithExclamation xs

allNonCharacter :: String -> Bool
allNonCharacter [] = True
allNonCharacter (x:xs)
  | x >= 'a' && x <= 'z' || x >= 'A' && x <= 'B' = False
  | otherwise = allNonCharacter xs
