package lsproduct

import "errors"

const testVersion = 4

func LargestSeriesProduct(s string, n int) (int, error) {
	digits := convertDigit(s)
	if len(s) == 0 && n == 0 {
		return 1, nil
	}
	if digits == nil {
		return 0, errors.New("Invalid characters")
	}
	if n < 0 || n > len(digits) {
		return 0, errors.New("Out of range")
	}
	result := 0
	for i := 0; i <= len(digits)-n; i++ {
		p := 1
		for j := 0; j < n; j++ {
			p *= digits[i+j]
		}
		if p > result {
			result = p
		}
	}
	return result, nil
}

func convertDigit(s string) (result []int) {
	for _, digit := range s {
		if digit >= '0' && digit <= '9' {
			result = append(result, int(digit-'0'))
		} else {
			return nil
		}
	}
	return result
}
