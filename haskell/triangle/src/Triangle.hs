module Triangle (TriangleType(..), triangleType) where

data TriangleType = Equilateral
                  | Isosceles
                  | Scalene
                  | Illegal
                  deriving (Eq, Show)

triangleType :: (Num a, Ord a, Eq a) => a -> a -> a -> TriangleType
triangleType a b c
  | not (validTriangle a b c) || allEqual a b c && a == 0 = Illegal
  | allEqual a b c = Equilateral
  | twoEqual a b c = Isosceles
  | otherwise = Scalene

allEqual :: (Num a, Eq a) => a -> a -> a -> Bool
allEqual a b c = a == b && b == c && c == a

twoEqual :: (Num a, Eq a) => a -> a -> a -> Bool
twoEqual a b c = a == b || b ==c || c == a

validTriangle :: (Num a, Ord a) => a -> a -> a -> Bool
validTriangle a b c = all ((<=) 0) [a + b - c, b + c - a, c + a - b]
