module Bob (responseFor) where

responseFor :: String -> String
responseFor xs
  | length(trim xs) == 0 = "Fine. Be that way!"
  | onlyNumber xs = "Whatever."
  | allUpper xs = "Whoa, chill out!"
  | endWithQuestion(trim xs) = "Sure."
  | allNonCharacter xs = "Fine. Be that way!"
  | otherwise = "Whatever."
  where trim = unwords . words

onlyNumber :: String -> Bool
onlyNumber [] = True
onlyNumber (x:xs)
  | x == '!' || x == ' ' || x == ',' || x >= '0' && x <= '9' = onlyNumber xs
  | otherwise = False

containUpper :: String -> Bool
containUpper [] = False
containUpper (x:xs)
  | x >= 'A' && x <= 'Z' || x == '!' = True
  | otherwise = containUpper xs

containNonUpper :: String -> Bool
containNonUpper [] = False
containNonUpper (x:xs)
  | x >= 'a' && x <= 'z' = True
  | otherwise = containNonUpper xs

allUpper :: String -> Bool
allUpper xs = (containUpper xs) && not (containNonUpper xs)

endWithQuestion :: String -> Bool
endWithQuestion [] = False
endWithQuestion "?" = True
endWithQuestion (x:xs) = endWithQuestion xs

endWithExclamation :: String -> Bool
endWithExclamation [] = False
endWithExclamation "!" = True
endWithExclamation (x:xs) = endWithExclamation xs

allNonCharacter :: String -> Bool
allNonCharacter xs
  | length xs == 0 = True
allNonCharacter [] = True
allNonCharacter (x:xs)
  | x >= 'a' && x <= 'z' || x >= 'A' && x <= 'B' = False
  | otherwise = allNonCharacter xs
