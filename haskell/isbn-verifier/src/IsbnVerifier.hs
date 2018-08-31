module IsbnVerifier (isbn) where

isbn :: String -> Bool
isbn s
  | validDigit s = True
  | otherwise = False

normalize ::String -> Maybe String
validDigit (c:str)
  | c == '-' || c == 'X' = True
  | c >= '0' && c <= '9' = True
  | otherwise = False
