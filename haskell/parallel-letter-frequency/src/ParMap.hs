module ParMap(parallelMap) where
import Control.Parallel (par, pseq)

parallelMap :: (a -> b) -> [a] -> [b]
parallelMap f (x:xs) =
  let r = f x
   in r `par` r : (parallelMap f xs)
parallelMap _ _ = []

forceList :: [a] -> ()
forceList (x:xs) = x `pseq` forceList xs
forceList _ = ()

stricterMap :: (a -> b) -> [a] -> [b]
stricterMap f xs = forceList xs `seq` map f xs
