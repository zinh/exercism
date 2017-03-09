package pascal

const testVersion = 1

func Triangle(n int) [][]int {
	result := [][]int{{1}}
	if n == 1 {
		return result
	}
	for i := 1; i < n; i++ {
		previousRow := result[i-1]
		currentRow := []int{1}
		for j := 1; j <= i; j++ {
			if j >= len(previousRow) {
				currentRow = append(currentRow, 1)
			} else {
				currentRow = append(currentRow, previousRow[j]+previousRow[j-1])
			}
		}
		result = append(result, currentRow)
	}
	return result
}
