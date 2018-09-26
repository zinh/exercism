module Clock (clockHour, clockMin, fromHourMin, toString) where
import Text.Printf (printf)

data Clock = Clock Int Int

instance Eq Clock where
  (Clock h1 m1) == (Clock h2 m2) = h1 == h2 && m1 == m2

instance Show Clock where
  show = toString

instance Num Clock where
  (Clock h1 m1) + (Clock h2 m2) = Clock (h1 + h2) (m1 + m2)
  (Clock h1 m1) - (Clock h2 m2) = Clock (h1 - h2) (m1 - m2)
  fromInteger minutes = Clock 0 (fromIntegral minutes)

clockHour :: Clock -> Int
clockHour (Clock hour _) = hour

clockMin :: Clock -> Int
clockMin (Clock _ minute) = minute

fromHourMin :: Int -> Int -> Clock
fromHourMin hour min = Clock hour min

toString :: Clock -> String
toString (Clock hour minute) = printf "%02d:%02d" hour minute
