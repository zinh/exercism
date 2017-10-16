package circular

import ("errors")

const testVersion = 4

type Buffer struct {
  content []byte
  current int
  first int
}

func NewBuffer(size int) *Buffer {
  return &Buffer{content: make([]byte, size), current: 0, first: 0}
}

func (b *Buffer) ReadByte() (byte, error) {
  if b.current == b.first {
    return 0, errors.New("Empty buffer")
  }
  return b.content[current], nil
}

func (*Buffer) WriteByte(c byte) error

func (*Buffer) Overwrite(c byte)

func (*Buffer) Reset()
