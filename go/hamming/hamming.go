package hamming
import "errors"

const testVersion = 5

func Distance(a, b string) (int, error) {
  distance := 0
  bs,as := []rune(b), []rune(a)
  if len(as) != len(bs){
    return -1, errors.New("length mismatch")
  }
  for index, c := range as {
    if bs[index] != c{
      distance += 1
    }
  }
  return distance, nil
}
