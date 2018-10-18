import Control.Concurrent

main = do
  m <- newEmptyMVar
  forkIO $ do
    v <- takeMVar m
    putStrLn ("Received: " ++ show v)
  putStrLn "Sending to thread"
  putMVar m "wwaakke uuupp"
