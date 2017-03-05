package raindrops

import (
	"strconv"
)

const testVersion = 2

func Convert(n int) string {
	result := ""
	if n%3 == 0 {
		result = result + "Pling"
	}
	if n%5 == 0 {
		result = result + "Plang"
	}
	if n%7 == 0 {
		result = result + "Plong"
	}
	if result == "" {
		result = strconv.Itoa(n)
	}
	return result
}
