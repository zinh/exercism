package slice

const testVersion = 1

func All(n int, s string) []string {
	if n == len(s) {
		return []string{s}
	}
	if n > len(s) {
		return nil
	}
	result := []string{UnsafeFirst(n, s)}
	result = append(result, All(n, string([]rune(s)[1:]))...)
	return result
}

func UnsafeFirst(n int, s string) string {
	return string([]rune(s)[:n])
}

func First(n int, s string) (first string, ok bool) {
	if n > len(s) {
		return "", false
	}
	return string([]rune(s)[:n]), true
}
