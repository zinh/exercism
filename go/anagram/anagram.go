package anagram

import "strings"

const testVersion = 1

func Detect(s string, dic []string) []string {
	result := []string{}
	for _, word := range dic {
		if isAnagram(strings.ToLower(s), strings.ToLower(word)) {
			result = append(result, strings.ToLower(word))
		}
	}
	return result
}

func isAnagram(s string, d string) bool {
	return (s != d) && (sortString(s) == sortString(d))
}

func sortString(s string) string {
	r := []rune(s)
	for i := 0; i < len(r); i++ {
		min := i
		for j := i; j < len(r); j++ {
			if r[min] > r[j] {
				min = j
			}
		}
		r[i], r[min] = r[min], r[i]
	}
	return string(r)
}
