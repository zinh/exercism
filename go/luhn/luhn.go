package luhn

const testVersion = 2

func Valid(s string) bool {
	tmp := []int{}
	filteredS := Filter(s)
	if len(filteredS) < 2 {
		return false
	}
	for index, digit := range filteredS {
		if len(filteredS)%2 == index%2 {
			if digit*2 > 9 {
				tmp = append(tmp, digit*2-9)
			} else {
				tmp = append(tmp, digit*2)
			}
		} else {
			tmp = append(tmp, digit)
		}
	}
	sum := 0
	for _, digit := range tmp {
		sum += digit
	}
	if sum%10 == 0 {
		return true
	}
	return false
}

func Filter(s string) (result []int) {
	for _, char := range s {
		if char >= '0' && char <= '9' {
			result = append(result, int(char-'0'))
		} else if char == ' ' {
			continue
		} else {
			return nil
		}
	}
	return result
}
