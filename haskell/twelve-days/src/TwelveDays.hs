module TwelveDays (recite) where
import Data.List (intercalate)

recite :: Int -> Int -> [String]
recite start stop = [sentence i | i <- [start..stop]]

sentence :: Int -> String
sentence 1 = "On the first day of Christmas my true love gave to me, a Partridge in a Pear Tree."
sentence n = "On the " ++ numbering n ++ " day of Christmas my true love gave to me, " ++ intercalate ", " [gift i | i <- [n, (n-1)..2]] ++ ", and a Partridge in a Pear Tree."

numbering :: Int -> String
numbering n =
  case n of
    1 -> "first"
    2 -> "second"
    3 -> "third"
    4 -> "fourth"
    5 -> "fifth"
    6 -> "sixth"
    7 -> "seventh"
    8 -> "eighth"
    9 -> "ninth"
    10 -> "tenth"
    11 -> "eleventh"
    12 -> "twelfth"

gift :: Int -> String
gift n =
  case n of
    1 -> "a Partridge in a Pear Tree"
    2 -> "two Turtle Doves"
    3 -> "three French Hens"
    4 -> "four Calling Birds"
    5 -> "five Gold Rings"
    6 -> "six Geese-a-Laying"
    7 -> "seven Swans-a-Swimming"
    8 -> "eight Maids-a-Milking"
    9 -> "nine Ladies Dancing"
    10 -> "ten Lords-a-Leaping"
    11 -> "eleven Pipers Piping"
    12 -> "twelve Drummers Drumming"
