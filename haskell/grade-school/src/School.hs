module School (School, add, empty, grade, sorted) where

data School = School [(Int, [String])]
  deriving (Show)

add :: Int -> String -> School -> School
add gradeNum student (School []) = School [(gradeNum, [student])]
add gradeNum student (School lst) = School $ foldr f [] lst
  where f g@(grade, lst@(s:sx)) memo = if grade == gradeNum
                                          then (grade, insertStudent student lst) : memo
                                          else g:memo

add' :: Int -> String -> School -> School
add' gradeNum student (School []) lst = School (gradeNum, [student]):currentLst
add' gradeNum student (School x@(grade, s):xs) currentLst
  | gradeNum == grade = xs ++ (grade, student:s):currentLst
  | otherwise = add' gradeNum student (School x:currentLst)

insertStudent :: String -> [String] -> [String]
insertStudent student lst = if length(newList) == length(lst) 
                               then student:newList 
                               else newList
  where insertStudent' name memo = if student > name
                                      then name:student:memo
                                      else name:memo
        newList = foldr (insertStudent') [] lst

empty :: School
empty = School []

grade :: Int -> School -> [String]
grade gradeNum school = [] 

sorted :: School -> [(Int, [String])]
sorted (School lst) = lst
