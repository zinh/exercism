package bob // package name must match the package name in bob_test.go
import "strings"

const testVersion = 2 // same as targetTestVersion
func Hey(s string) string {
	if AllUpper(s) {
		return "Whoa, chill out!"
	} 
        if EndWithQuestion(strings.TrimSpace(s)) {
		return "Sure."
	} 
        if AllNonCharacter(strings.TrimSpace(s)) {
		return "Fine. Be that way!"
	} 
        return "Whatever."
}

func EndWithQuestion(s string) bool {
	return len(s) > 0 && s[len(s)-1] == '?'
}

func AllUpper(s string) bool {
	containNonUpper := false
	containUpper := false
	for _, c := range s {
		if (c >= 'A' && c <= 'Z') || (c == '!') {
			containUpper = true
		} else if c >= 'a' && c <= 'z' {
			containNonUpper = true
		}
	}
	return containUpper && !containNonUpper && (strings.ToUpper(s) == s)
}

func AllNonCharacter(s string) bool {
	if len(s) == 0 {
		return true
	}
	for _, c := range s {
		if (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') {
			return false
		}
	}
	return false
}
