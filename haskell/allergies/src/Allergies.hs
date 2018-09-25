module Allergies (Allergen(..), allergies, isAllergicTo) where

import Data.Bits ((.&.))
import Data.Map.Strict (fromList, findWithDefault, keys)

data Allergen = Eggs
              | Peanuts
              | Shellfish
              | Strawberries
              | Tomatoes
              | Chocolate
              | Pollen
              | Cats
              deriving (Eq, Ord)

m = fromList [(Eggs, 1), (Peanuts, 2), (Shellfish, 4), (Strawberries, 8), (Tomatoes, 16), (Chocolate, 32), (Pollen, 64), (Cats, 128)] 

allergiesMap :: Allergen -> Int
allergiesMap allergen = findWithDefault 0 allergen m

allergies :: Int -> [Allergen]
allergies score = filter (`isAllergicTo` score) (keys m)

isAllergicTo :: Allergen -> Int -> Bool
isAllergicTo allergen score = (.&.) score (allergiesMap allergen) > 0
