package summultiples

func SumMultiples(n int, divisors ...int) int {
	c := make(chan []int, len(divisors))
	result := []int{}
	sum := 0
	for _, divisor := range divisors {
		SumMultiple(n, divisor, c)
	}
	for range divisors {
		select {
		case i := <-c:
			result = append(result, i...)
		}
	}
	for _, i := range deDup(result) {
		sum += i
	}
	return sum
}

func SumMultiple(n int, divisor int, c chan []int) {
	sum := []int{}
	p := divisor
	for p < n {
		sum = append(sum, p)
		p = p + divisor
	}
	c <- sum
}

func deDup(numbers []int) []int {
	result := []int{}
	for _, num := range numbers {
		existed := false
		for _, r := range result {
			if r == num {
				existed = true
				break
			}
		}
		if !existed {
			result = append(result, num)
		}
	}
	return result
}
