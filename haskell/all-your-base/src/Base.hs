module Base (Error(..), rebase) where

data Error a = InvalidInputBase | InvalidOutputBase | InvalidDigit a
    deriving (Show, Eq)

rebase :: Integral a => a -> a -> [a] -> Either (Error a) [a]
rebase inputBase outputBase inputDigits
  | inputBase <= 1 = Left InvalidInputBase
  | outputBase <= 1 = Left InvalidOutputBase
  | any invalidDigit inputDigits = Left (InvalidDigit (head $ filter invalidDigit inputDigits))
  where invalidDigit digit = digit < 0 || digit >= inputBase
rebase inputBase outputBase inputDigits = 
  let number = toBase10 inputDigits inputBase
      outputDigits = reverse $ fromBase10 number outputBase
  in Right outputDigits

toBase10 :: Integral a => [a] -> a -> a
toBase10 digits inputBase = 
  let add digit (idx, total) = (idx + 1, total + digit * inputBase ^ idx)
  in snd $ foldr add (0, 0) digits

fromBase10 :: Integral a => a -> a -> [a]
fromBase10 0 _ = []
fromBase10 number outputBase = (number `mod` outputBase) : fromBase10 (number `div` outputBase) outputBase
