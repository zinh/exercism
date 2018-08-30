module Phone (number) where

number :: String -> Maybe String
number xs =
  let numbers = [c | c <- xs, c >= '0' && c <= '9']
  in isValid(numbers)

isValid :: String -> Maybe String
isValid numbers
  | l < 10 || l > 11 = Nothing
  | l == 11 && head(numbers) /= '1' = Nothing
  | l == 11 = normalize (tail numbers)
  | l == 10 = normalize numbers
  | otherwise = Just numbers
  where l = length(numbers)

normalize :: String -> Maybe String
normalize numbers
  | head numbers == '1' || head numbers == '0' = Nothing
  | numbers !! 3 == '1' || numbers !! 3 == '0' = Nothing
  | otherwise = Just numbers
