module Clock (clockHour, clockMin, fromHourMin, toString) where
import Text.Printf (printf)

data Clock = Clock Int Int

instance Eq Clock where
  (Clock h1 m1) == (Clock h2 m2) = h1 == h2 && m1 == m2

instance Show Clock where
  show = toString

instance Num Clock where
  (Clock h1 m1) + (Clock h2 m2) = fromHourMin (h1 + h2) (m1 + m2)
  (Clock h1 m1) - (Clock h2 m2) = fromHourMin (h1 - h2) (m1 - m2)
  fromInteger minutes = fromHourMin 0 (fromIntegral minutes)

clockHour :: Clock -> Int
clockHour (Clock hour _) = hour

clockMin :: Clock -> Int
clockMin (Clock _ minute) = minute

fromHourMin :: Int -> Int -> Clock
fromHourMin hour min
  | min <= -60 = fromHourMin (hour - additionHour) (60 * additionHour + min)
  | min < 0 = fromHourMin (hour - 1) (60  + min)
  where additionHour = min `div` (-24)
fromHourMin hour min
  | min >= 60 = fromHourMin (hour + min `div` 60) (min `mod` 60)
fromHourMin hour min
  | hour >= 24 = Clock (hour `mod` 24) min
fromHourMin hour min
  | hour < 0 = Clock (24 * day + hour) min
  where day = if hour < (-24) then hour `div` (-24) + 1 else 1
fromHourMin hour min = Clock hour min

toString :: Clock -> String
toString (Clock hour minute) = printf "%02d:%02d" hour minute
