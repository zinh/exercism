module Robot
    ( Bearing(East,North,South,West)
    , bearing
    , coordinates
    , mkRobot
    , simulate
    , turnLeft
    , turnRight
    ) where

data Bearing = North
             | East
             | South
             | West
             deriving (Eq, Show)

data Robot = Robot Coordinate Bearing

data Coordinate = Coordinate Integer Integer

data Matrix2D = Matrix2D Integer Integer Integer Integer

bearing :: Robot -> Bearing
bearing (Robot _ bearing) =  bearing

coordinates :: Robot -> (Integer, Integer)
coordinates (Robot (Coordinate a b) _) = (a, b)

mkRobot :: Bearing -> (Integer, Integer) -> Robot
mkRobot direction (a, b) = Robot (Coordinate a b) direction

simulate :: Robot -> String -> Robot
simulate (Robot c@(Coordinate m n) bearing) (x:xs)
  | x == 'R' = simulate (Robot coordinate (turnRight bearing)) xs
  | x == 'L' = simulate (Robot coordinate (turnLeft bearing)) xs
  | x == 'A' = simulate (Robot (Coordinate (m + a) (n + b)) bearing) xs
  where (a, b) = mapBearing bearing

turnLeft :: Bearing -> Bearing
turnLeft direction = mul Matrix2D 0 (-1) 1 0 (mapBearing direction)

turnRight :: Bearing -> Bearing
turnRight direction = mul (Matrix2D 0 1 (-1) 0) (mapBearing direction)

mul :: Matrix2D -> Coordinate -> Coordinate
mul (Matrix2D x11 x12 x21 x22) (Coordinate a b) = Coordinate (x11 * a + x12 * b) (x21 *  a + x22 * b)

mapBearing :: Bearing -> Coordinate
mapBearing b
  | b == North = Coordinate 0 1
  | b == East = Coordinate 1 0
  | b == South = Coordinate 0 (-1)
  | b == West = Coordinate (-1) 0
