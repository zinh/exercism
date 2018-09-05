module Garden
    ( Plant (..)
    , garden
    , lookupPlants
    ) where

data Plant = Clover
           | Grass
           | Radishes
           | Violets
           deriving (Eq, Show)

type Garden = ([Plant], [Plant])

garden :: [String] -> String -> Garden
garden students plants = map stringToPlans lines plants

lookupPlants :: String -> Garden -> [Plant]
lookupPlants student garden = error "You need to implement this function."

stringToPlans :: String -> [Plant]
stringToPlans str = [charToPlant c | c <- str]

charToPlant c
  | 'C' = Clover
  | 'G' = Grass
  | 'R' = Radishes
  | 'V' = Violets
