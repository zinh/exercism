module Diamond (diamond) where
import Data.Char (ord)

diamond :: Char -> Maybe [String]
diamond c =
  let maxWidth = (spaceBetween c) + 2
      downDirection = [generateRow i maxWidth | i <- ['A'..c]]
  in Just (downDirection ++ drop 1 (reverse downDirection))

spaceBetween :: Char -> Int
spaceBetween c = 2 * (ord(c) - ord('A') - 1) + 1

spacePadding :: Char -> Int -> Int
spacePadding c maxWidth = (maxWidth - 2 - (spaceBetween c)) `div` 2

generateRow :: Char -> Int -> String
generateRow 'A' maxWidth = replicate ((maxWidth - 1) `div` 2) ' ' ++ "A" ++ replicate ((maxWidth - 1) `div` 2) ' '
generateRow c maxWidth = (replicate (spacePadding c maxWidth) ' ') ++ [c] ++ (replicate (spaceBetween c) ' ') ++ [c] ++ (replicate (spacePadding c maxWidth) ' ')
