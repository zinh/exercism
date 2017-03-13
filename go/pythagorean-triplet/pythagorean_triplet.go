package pythagorean

import "fmt"

const testVersion = 1

type Triplet [3]int

func Range(min, max int) []Triplet {
	result := []Triplet{}
	for i := min; i <= max; i++ {
		triplets := FindTriplet(min, i)
		for _, triplet := range triplets {
			result = append(result, triplet)
		}
	}
	return result
}

func Sum(p int) (result []Triplet) {
	result = []Triplet{}
	triplets := Range(1, p)
	fmt.Println(triplets)
	for _, triplet := range triplets {
		if triplet[0]+triplet[1]+triplet[2] == p {
			result = append(result, triplet)
		}
	}
	return result
}

func FindTriplet(min, n int) [][3]int {
	result := [][3]int{}
	for i := min; i <= n; i++ {
		for j := i; j <= n; j++ {
			if i*i+j*j == n*n {
				result = append(result, [3]int{i, j, n})
			}
		}
	}
	return result
}
