module IsbnVerifier (isbn) where
import Data.Char (ord)

isbn :: String -> Bool
isbn s = validDigit digits
  where digits = normalize s

normalize ::String -> Maybe String
normalize isbn = [c | c <- isbn, c == 'X' || (c >= '0' && c <= '9')]

validDigit :: String -> Bool
validDigit digits
  | length digits == 10 = checkDigits digits
  | otherwise = False

checkDigits :: String -> Bool
checkDigits digits 
  | fst result `mod` 11 == 0 = True
  | otherwise = False
  where result = foldl (\memo digit -> (fst memo + snd memo * score digit, snd memo - 1)) (0, length digits) digits
        score digit
          | digit == 'X' = 10
          | otherwise = (ord digit) - (ord '0')
