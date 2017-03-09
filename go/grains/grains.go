package grains

import "errors"

const testVersion = 1

func Square(n int) (uint64, error) {
	if n <= 0 || n > 64 {
		return 0, errors.New("Error")
	}
	return 1 << uint(n-1), nil
}

func Total() uint64 {
	var sum uint64 = 0
	for i := 1; i <= 64; i++ {
		n, _ := Square(i)
		sum += n
	}
	return sum
}
