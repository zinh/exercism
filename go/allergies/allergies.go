package allergies

const testVersion = 1

var dict = map[string]uint{
	"eggs":         1,
	"peanuts":      2,
	"shellfish":    4,
	"strawberries": 8,
	"tomatoes":     16,
	"chocolate":    32,
	"pollen":       64,
	"cats":         128,
}

func Allergies(score uint) []string {
	result := []string{}
	for allergic := range dict {
		if AllergicTo(score, allergic) {
			result = append(result, allergic)
		}
	}
	return result
}

func AllergicTo(score uint, allergic string) bool {
	return (score & dict[allergic]) == dict[allergic]
}
