package scrabble

import "strings"

const testVersion = 4

var scoreMaster = map[int][]string{1: {"A", "E", "I", "O", "U", "L", "N", "R", "S", "T"},
	2:  {"D", "G"},
	3:  {"B", "C", "M", "P"},
	4:  {"F", "H", "V", "W", "Y"},
	5:  {"K"},
	8:  {"J", "X"},
	10: {"Q", "Z"}}

func Score(word string) (result int) {
	scores := Transform(scoreMaster)
	result = 0
	for _, char := range strings.ToLower(word) {
		if scores[string(char)] > 0 {
			result += scores[string(char)]
		}
	}
	return result
}

func Transform(oldScores map[int][]string) map[string]int {
	result := map[string]int{}
	for score, chars := range oldScores {
		for _, char := range chars {
			result[strings.ToLower(char)] = score
		}
	}
	return result
}
