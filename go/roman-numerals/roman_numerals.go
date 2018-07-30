package romannumerals

import (
	"errors"
	"strings"
)

const testVersion = 3

var huns = []string{"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"}
var tens = []string{"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"}
var ones = []string{"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"}

func ToRomanNumeral(n int) (string, error) {
	if n <= 0 || n >= 4000 {
		return "", errors.New("Out of range")
	}
	results := []string{}
	for n >= 1000 {
		results = append(results, "M")
		n -= 1000
	}
	results = append(results, huns[n/100])
	n = n % 100

	results = append(results, tens[n/10])
	n = n % 10

	results = append(results, ones[n])
	return strings.Join(results, ""), nil
}
