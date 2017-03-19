package anagram
import "fmt"

const testVersion = 1

func Detect(s string, dic []string) []string {
  result := []string{}
  for _, word := range dic {
    if isAnagram(s, word) {
      result = append(result, word)
    }
  }
  return result
}

func isAnagram(s string, d string) bool {
  // fmt.Printf("Source: %s, Dest: %s", s, d)
  // fmt.Printf(" Source: %s, Dest: %s\n", sortString(s), sortString(d))
  return sortString(s) == sortString(d)
}

func sortString(s string) string {
  fmt.Println(s)
  sortedArr := []rune{}
  for _, char := range s {
    fmt.Printf("\nCurrent: %s, new char: %s\n", string(sortedArr), string(char))
    i := len(sortedArr) - 1
    for ;i > 0; i-- {
      if sortedArr[i] <= char {
        break
      }
    }
    if i < 0 || i >= len(sortedArr)-1 {
      sortedArr = append(sortedArr, char)
    } else {
      halfTail := sortedArr[i:]
      halfHead := sortedArr[0:i]
      fmt.Printf("i = %d, HalfHead: %s, HalfTail: %s\n", i, string(halfHead), string(halfTail))
      //tmp := append(halfHead, char)
      fmt.Println(halfHead, char, halfTail)
      //sortedArr = append(tmp, halfTail...)
    }
  }
  return string(sortedArr)
}
