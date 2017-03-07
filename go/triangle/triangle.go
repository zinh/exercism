package triangle

import (
	"math"
)

const testVersion = 3

func KindFromSides(a, b, c float64) Kind {
	if a == 0 && b == 0 && c == 0 {
		return NaT
	}
	if a == math.Inf(1) || b == math.Inf(1) || c == math.Inf(1) ||
		a == math.Inf(-1) || b == math.Inf(-1) || c == math.Inf(-1) {
		return NaT
	}
	if a == b && a == c && a != 0 {
		return Equ
	}
	if (a == b && a+b >= c) || (b == c && b+c >= a) || (c == a && a+c >= b) {
		return Iso
	}
	if a+b > c && b+c > a && c+a >= b {
		return Sca
	}
	return NaT
}

type Kind int

const (
	NaT Kind = iota // not a triangle
	Equ             // equilateral
	Iso             // isosceles
	Sca             // scalene
)
