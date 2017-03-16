package sieve

const testVersion = 1

func Sieve(limit int) (primes []int) {
	s := map[int]bool{}
	for i := 2; i < limit; i++ {
		for j := 2; ; j++ {
			if i*j > limit {
				break
			} else {
				s[i*j] = true
			}
		}
	}
	for i := 2; i <= limit; i++ {
		if !s[i] {
			primes = append(primes, i)
		}
	}
	return primes
}
