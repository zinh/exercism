package wordcount

import "strings"

const testVersion = 3

// Use this return type.
type Frequency map[string]int

// Just implement the function.
func WordCount(phrase string) Frequency {
	result := Frequency{}
	for _, word := range tokenizer(strings.ToLower(phrase)) {
		result[word] += 1
	}
	return result
}

func tokenizer(phrase string) []string {
	delimiter := []rune{' ', ',', '\n'}
	word := []rune{}
	words := []string{}
	for index, char := range phrase {
		if char == '\'' {
			if len(word) > 0 && phrase[index+1] != ' ' {
				word = append(word, char)
			}
		} else if c := contains(delimiter, char); c && len(word) > 0 {
			words = append(words, string(word))
			word = []rune{}
		} else if !c && !ignoreChar(char) {
			word = append(word, char)
		}
	}
	if len(word) != 0 {
		words = append(words, string(word))
	}
	return words
}

func contains(chars []rune, char rune) bool {
	for _, c := range chars {
		if char == c {
			return true
		}
	}
	return false
}

func ignoreChar(c rune) bool {
	return !((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9'))
}
