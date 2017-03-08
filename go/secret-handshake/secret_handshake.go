package secret

import (
	"fmt"
	"strconv"
)

const testVersion = 1

func Handshake(code uint) []string {
	displayTxt := map[int]string{1: "wink", 10: "double blink", 100: "close your eyes", 1000: "jump"}
	result := []string{}
	binValue := ToBin(code)
	reverse := false
	if binValue >= 10000 {
		reverse = true
		binValue = binValue % 10000
	}
	for _, divisor := range []int{1000, 100, 10, 1} {
		if binValue >= divisor && (binValue/divisor) >= 0 {
			result = append(result, displayTxt[divisor])
			binValue = binValue % divisor
		}
	}
	if reverse {
		return result
	} 
        if {
		return Reverse(result)
	}
}

func ToBin(n uint) int {
	i, _ := strconv.Atoi(fmt.Sprintf("%b", int(n)))
	return i
}

func Reverse(numbers []string) []string {
	for i := 0; i < len(numbers)/2; i++ {
		j := len(numbers) - i - 1
		numbers[i], numbers[j] = numbers[j], numbers[i]
	}
	return numbers
}
