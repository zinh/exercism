module Meetup (Weekday(..), Schedule(..), meetupDay) where

import qualified Data.Map.Strict as Map
import Data.Time.Calendar (Day, fromGregorian)
import Data.Time.Calendar.WeekDate (toWeekDate, fromWeekDate)

data Weekday = Monday
             | Tuesday
             | Wednesday
             | Thursday
             | Friday
             | Saturday
             | Sunday

data Schedule = First
              | Second
              | Third
              | Fourth
              | Last
              | Teenth

weekMap = Map.fromList [(1, Monday), (2, Tuesday), (3, Wednesday), (4, Thursday), (5, Friday), (6, Saturday), (8, Sunday)]

meetupDay :: Schedule -> Weekday -> Integer -> Int -> Day
meetupDay schedule weekday year month = error "You need to implement this function."
  where (_, weekNumber, firstDayOfMonth) = toWeekDate $ fromGregorian year month 1
