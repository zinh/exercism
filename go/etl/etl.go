package etl

import "strings"

const testVersion = 1

func Transform(oldScores map[int][]string) map[string]int {
	result := map[string]int{}
	for score, chars := range oldScores {
		for _, char := range chars {
			result[strings.ToLower(char)] = score
		}
	}
	return result
}
