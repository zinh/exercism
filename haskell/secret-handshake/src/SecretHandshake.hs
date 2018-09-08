module SecretHandshake (handshake) where

import Data.Bits((.&.))
import qualified Data.Map as Map

handshake :: Int -> [String]
handshake 0 = []
handshake n = if (.&.) n 16 > 0 then reverse actions else actions
  where m = Map.fromList [(1, "wink"), (2, "double blink"), (4, "close your eyes"), (8, "jump")]
        actions = foldr (\b memo -> if (.&.) n b > 0 then (Map.findWithDefault "A" b m):memo else memo) [] [1, 2, 4, 8]
