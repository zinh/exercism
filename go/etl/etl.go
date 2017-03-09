package etl

const testVersion = 1

var scoreMaster = map[int][]string{1: {"A", "E", "I", "O", "U", "L", "N", "R", "S", "T"},
	2:  {"D", "G"},
	3:  {"B", "C", "M", "P"},
	4:  {"F", "H", "V", "W", "Y"},
	5:  {"K"},
	8:  {"J", "X"},
	10: {"Q", "Z"}}

func Transform(oldScores map[int][]string) map[string]int {
  result := {}
  for score, chars := range oldScores {
  }
  return nil
}

func mapPoint(s string) int {
  for k, v := range scoreMaster {
    if contains(v, s) {
      return k
    }
  }
  return 0
}

func contains(chars []string, c string) bool {
  for _, char := range chars {
    if char == c {
      return true 
    }
  }
  return false
}
