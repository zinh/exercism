package queenattack

import "errors"

const testVersion = 2

func CanQueenAttack(q1 string, q2 string) (bool, error) {
	if len(q1) != 2 || len(q2) != 2 || q1 == q2 {
		return false, errors.New("Invalid input")
	}
	x1, y1 := convertAxis(q1)
	x2, y2 := convertAxis(q2)
	if x1 > 8 || x1 <= 0 || x2 > 8 || x2 <= 0 || y1 > 8 || y1 <= 0 || y2 > 8 || y2 <= 0 {
		return false, errors.New("Out of range")
	}
	if (x1 == x2) || (y1 == y2) {
		return true, nil
	}
	if Abs(x1-y1) == Abs(x2-y2) {
		return true, nil
	}
	return false, nil
}

func convertAxis(s string) (int, int) {
	chars := []rune(s)
	x, y := chars[0], chars[1]
	return int(x - 'a' + 1), int(y - '0')
}

func Abs(n int) int {
	if n > 0 {
		return n
	}
	return -n
}
