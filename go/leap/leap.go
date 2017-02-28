// Leap stub file

// The package name is expected by the test program.
package leap

// testVersion should match the targetTestVersion in the test file.
const testVersion = 3

// It's good style to write a comment here documenting IsLeapYear.
func IsLeapYear(n int) bool {
  if n % 4 == 0 {
    if n % 100 == 0 {
      if n % 400 == 0 {
        return true
      } else {
        return false
      }
    }else{
      return true
    }
  } else {
    return false
  }
}
