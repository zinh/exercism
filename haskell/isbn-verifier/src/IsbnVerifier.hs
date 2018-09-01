module IsbnVerifier (isbn, normalize) where
import Data.Char (ord)

isbn :: String -> Bool
isbn s = 
  case digits of 
    Just validDigits -> if length validDigits /= 10 then False else validate validDigits
    Nothing -> False
  where digits = normalize s

normalize ::String -> Maybe String
normalize isbn = sequence (map f $ zip [0..] str)
  where str = [c | c <- isbn, c /= '-']
        f (idx, c)
          | (c >= '0' && c <= '9') || (c == 'X' && idx == 9) = Just c
          | otherwise = Nothing

validate :: String -> Bool
validate digits = 
  case totalScore `mod` 11 of 
    0 -> True
    otherwise -> False
  where totalScore = foldl f 0 $ zip [0..] digits
        f score (idx, c) 
          | c == 'X' = score + (10 - idx) * 10
          | otherwise = score + (10 - idx) * ((ord c) - (ord '0'))
