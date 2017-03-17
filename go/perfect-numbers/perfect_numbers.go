package perfect

const testVersion = 1

type Classification int

const (
  ClassificationDeficient Classification = iota
  ClassificationPerfect
  ClassificationAbundant
)

const (
  ErrOnlyPositive error = iota
)

func Classify(n uint64) (Classification, error) {
  return ClassificationPerfect, nil
}
