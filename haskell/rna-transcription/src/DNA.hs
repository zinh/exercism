module DNA (toRNA) where

toRNA :: String -> Maybe String
toRNA = mapM toSingleRNA

toSingleRNA :: Char -> Maybe Char
toSingleRNA x = case x of
                  'G' -> Just 'C'
                  'C' -> Just 'G'
                  'T' -> Just 'A'
                  'A' -> Just 'U'
                  otherwise -> Nothing
