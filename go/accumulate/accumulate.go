package accumulate

const testVersion = 1

func Accumulate(items []string, f func(string) string) (result []string) {
	for _, item := range items {
		result = append(result, f(item))
	}
	return result
}
