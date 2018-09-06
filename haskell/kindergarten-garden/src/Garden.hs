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

type Garden = [(String, Plant)]

garden :: [String] -> String -> Garden
garden students plants = concat $ (map (zip studentList)) planList
  where planList = map stringToPlans (lines plants)
        studentList = students >>= replicate 2

lookupPlants :: String -> Garden -> [Plant]
lookupPlants student garden = map snd $ filter (\(name, plant) -> name == student) garden

stringToPlans :: String -> [Plant]
stringToPlans str = [charToPlant c | c <- str]

charToPlant c
  | c == 'C' = Clover
  | c == 'G' = Grass
  | c == 'R' = Radishes
  | c == 'V' = Violets
