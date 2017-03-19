package strand

const testVersion = 3

var rnaMap = map[rune]rune{
	'G': 'C',
	'C': 'G',
	'T': 'A',
	'A': 'U',
}

func ToRNA(s string) string {
	result := []rune{}
	for _, dna := range s {
		result = append(result, rnaMap[dna])
	}
	return string(result)
}
