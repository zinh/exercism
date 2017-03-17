package palindrome

import (
	"errors"
	"strconv"
)

const testVersion = 1
const MaxUint = ^uint(0)
const MaxInt = int(MaxUint >> 1)

type Product struct {
	Product        int      // palindromic, of course
	Factorizations [][2]int //list of all possible two-factor factorizations of Product, within given limits, in order
}

func Products(min, max int) (pmin, pmax Product, e error) {
	if min > max {
		return Product{}, Product{}, errors.New("fmin > fmax")
	}
	minP := MaxInt // MaxInt
	maxP := -1
	for i := min; i <= max; i++ {
		for j := min; j <= max; j++ {
			if p := i * j; isPalindrome(p) {
				if minP > p {
					minP = p
				}

				if maxP < p {
					maxP = p
				}
			}
		}
	}
	if maxP == -1 {
		return Product{}, Product{}, errors.New("No palindromes")
	}
	pmin = Product{Product: minP, Factorizations: factorize(minP, min, max)}
	pmax = Product{Product: maxP, Factorizations: factorize(maxP, min, max)}
	return pmin, pmax, nil
}

func isPalindrome(n int) (result bool) {
	chars := []rune(strconv.Itoa(n))
	for i, j := 0, len(chars)-1; i < j; i, j = i+1, j-1 {
		chars[i], chars[j] = chars[j], chars[i]
	}
	return string(chars) == strconv.Itoa(n)
}

func factorize(n, min, max int) (result [][2]int) {
	upper := max
	for i := min; ; i++ {
		if i >= upper {
			break
		}
		if d := n / i; n%i == 0 && d >= min && d <= max {
			result = append(result, [2]int{i, d})
			upper = d
		}
	}
	return result
}
