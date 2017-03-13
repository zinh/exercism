package isogram

import "strings"

const testVersion = 1

func IsIsogram(w string) bool {
	charMap := map[rune]int{}
	for _, c := range strings.ToUpper(w) {
		if c == ' ' || c == '-' {
			continue
		}
		if charMap[c] > 0 {
			return false
		} else {
			charMap[c] = 1
		}
	}
	return true
}
