package acronym

import (
	"fmt"
	"strings"
)

const testVersion = 2

func Abbreviate(term string) string {
	result := ""
	newWord := true
	normalCase := false
	for _, c := range term {
		if c == ' ' || c == '-' {
			newWord = true
		} else {
			if newWord {
				result += strings.ToUpper(fmt.Sprintf("%c", c))
			} else {
				if c < 65 || c > 90 {
					normalCase = true
				} else {
					if normalCase {
						result += strings.ToUpper(fmt.Sprintf("%c", c))
					}
				}
			}
			newWord = false
		}
	}
	return result
}
