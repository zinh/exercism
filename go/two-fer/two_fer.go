// This is a "stub" file.  It's a little start on your solution.
// It's not a complete solution though; you have to write some code.

// Package twofer should have a package comment that summarizes what it's about.
// https://golang.org/doc/effective_go.html#commentary
package twofer
import "fmt"

// ShareWith needs a comment documenting it.
func ShareWith(name string) string {
	// Write some code here to pass the test suite.
	// Then remove all the stock comments.
	// They're here to help you get started but they only clutter a finished solution.
	// If you leave them in, reviewers will protest!
        if name != "" {
          return fmt.Sprintf("One for %s, one for me.", name)
        }
        return "One for you, one for me."
}
