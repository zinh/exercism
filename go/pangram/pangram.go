package pangram

const testVersion = 1

func IsPangram(s string) bool {
	charCount := make(map[rune]int)
	for i := 0; i < 26; i++ {
		charCount[rune('a'+i)] = 0
	}

	for _, c := range s {
		if c >= 65 && c <= 90 {
			c = c + 32
		}
		if charCount[c] == 0 {
			charCount[c] += 1
		}
	}

	for _, count := range charCount {
		if count == 0 {
			return false
		}
	}
	return true
}
