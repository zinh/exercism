package letter

const testVersion = 1

type FreqMap map[rune]int

func Frequency(s string) FreqMap {
	m := FreqMap{}
	for _, r := range s {
		m[r]++
	}
	return m
}

func ConcurrentFrequency(lines []string) FreqMap {
	c := make(chan FreqMap)
	result := FreqMap{}
	for _, line := range lines {
		go FrequencyWithChannel(line, c)
	}
	for i := 1; i <= 3; i++ {
		select {
		case r := <-c:
			for char, count := range r {
				result[char] += count
			}
		}
	}
	return result
}

func FrequencyWithChannel(s string, c chan FreqMap) {
	c <- Frequency(s)
}
