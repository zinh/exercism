module Prime (nth) where

nth :: Int -> Maybe Integer
nth n
  | n <= 0 = Nothing
  | otherwise = Just $ toInteger $ last (take n [k | k <- [2..], isPrime k])

isPrime :: Int -> Bool
isPrime n =
  let limit = round (sqrt (fromIntegral n))
      d = [p | p <- [2..limit], n `mod` p == 0]
  in null d
