package bob // package name must match the package name in bob_test.go
import "strings"

const testVersion = 2 // same as targetTestVersion
func Hey(s string) string {
  if AllUpper(s) {
    return "Whoa, chill out!"
  } else if EndWithQuestion(strings.TrimSpace(s)) {
    return "Sure."
  } else if AllNonCharacter(s) {
    return "Fine. Be that way!"
  } else {
    return "Whatever."
  }
}

func EndWithQuestion(s string) bool {
  return s[len(s) - 1] == '?'
}

func AllUpper(s string) bool {
  containNonUpper := false
  containUpper := false
  for _, c := range(s) {
    if (c >= 'A' && c <= 'Z') || (c == '!') || (c == ' ') || (c == '?'){
      containUpper = true
    } else {
      containNonUpper = true
    }
  }
  return containUpper && !containNonUpper
}

func AllNonCharacter(s string) bool {
  for _, c := range(s) {
    if (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') {
      return false
    }
  }
  return false
}
