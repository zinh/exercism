package brackets

import "errors"

const testVersion = 4

type stack struct {
	data []string
}

type stacky interface {
	Push(string)
	Pop() (string, error)
}

func (s *stack) Push(item string) {
	s.data = append(s.data, item)
}

func (s *stack) Pop() (string, error) {
	if len(s.data) == 0 {
		return "", errors.New("Pop empty stack")
	}
	item := s.data[len(s.data)-1]
	if len(s.data) == 1 {
		s.data = []string{}
	} else {
		s.data = s.data[0 : len(s.data)-1]
	}
	return item, nil
}

func Bracket(s string) (bool, error) {
	stack := stack{data: []string{}}
	for _, char := range s {
		if char == '{' || char == '[' || char == '(' {
			stack.Push(string(char))
		} else {
			item, err := stack.Pop()
			if err != nil {
				return false, nil
			}
			if (char - []rune(item)[0]) > 2 {
				return false, nil
			}
		}
	}
	if len(stack.data) == 0 {
		return true, nil
	}
	return false, nil
}
