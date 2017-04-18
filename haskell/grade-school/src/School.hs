module School (School, add, empty, grade, sorted) where
import qualified Data.Map as Map

data School = School (Map.Map Int [String])
  deriving (Show)

add :: Int -> String -> School -> School
add gradeNum student (School m) = case Map.lookup gradeNum m of
                                    Just students -> School (Map.insert gradeNum (insertStudent student students) m)
                                    Nothing -> School (Map.insert gradeNum [student] m)

insertStudent :: String -> [String] -> [String]
insertStudent student lst = if length(newList) == length(lst) 
                               then student:newList 
                               else newList
  where insertStudent' name memo = if student > name
                                      then name:student:memo
                                      else name:memo
        newList = foldr (insertStudent') [] lst

empty :: School
empty = School Map.empty

grade :: Int -> School -> [String]
grade gradeNum (School m) = case Map.lookup gradeNum m of
                              Just students -> students
                              Nothing -> []

sorted :: School -> [(Int, [String])]
sorted (School m) = Map.toList m
