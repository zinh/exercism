module Brackets (arePaired) where

arePaired :: String -> Bool
arePaired xs = 
  let result = foldl check (Just []) xs
   in case result of
        Just [] -> True
        otherwise -> False

check :: Maybe [Char] -> Char -> Maybe [Char]
check Nothing _ = Nothing
check (Just stack) element
  | isOpen element = Just (element:stack)
  | isClose element = case stack of
                        [] -> Nothing
                        (x:xs) -> if isPair x element then Just xs else Nothing
  | otherwise = Just stack

isOpen :: Char -> Bool
isOpen c = case c of
             '[' -> True
             '(' -> True
             '{' -> True
             _ -> False

isClose :: Char -> Bool
isClose c = case c of 
              ']' -> True
              ')' -> True
              '}' -> True
              _ -> False

isPair :: Char -> Char -> Bool
isPair '(' ')' = True
isPair '[' ']' = True
isPair '{' '}' = True
isPair _ _ = False
