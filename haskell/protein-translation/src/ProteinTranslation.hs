module ProteinTranslation(proteins) where
import Data.List.Split (chunksOf)
import Data.List (foldl')

proteins :: String -> Maybe [String]
proteins rna = sequence $ fst (foldl' mapProteins ([], False) chunks)
  where chunks = chunksOf 3 rna
        mapProteins (chunks, stopped) chunk
          | stopped = (chunks, True)
          | p == Just "STOP" = (chunks, True)
          | otherwise = (chunks ++ [p], False)
              where p = mapProtein chunk

mapProtein :: String -> Maybe String
mapProtein seq
  | seq == "AUG" = Just "Methionine"
  | seq == "UUU" || seq == "UUC" = Just "Phenylalanine"
  | seq == "UUA" || seq == "UUG" = Just "Leucine"
  | seq == "UCU" || seq == "UCC" || seq == "UCA" || seq == "UCG" = Just "Serine"
  | seq == "UAU" || seq == "UAC" = Just "Tyrosine"
  | seq == "UGU" || seq == "UGC" = Just "Cysteine"
  | seq == "UGG" = Just "Tryptophan"
  | seq == "UAA" || seq == "UAG" || seq == "UGA" = Just "STOP"
  | otherwise = Nothing
