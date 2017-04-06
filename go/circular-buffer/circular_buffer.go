package circular

const testVersion = 4

type Buffer struct {
  content []int
  pointer int
}

func NewBuffer(size int) *Buffer {
  return Buffer{content: []int{}, 0}
}

func (*Buffer) ReadByte() (byte, error)

func (*Buffer) WriteByte(c byte) error

func (*Buffer) Overwrite(c byte)

func (*Buffer) Reset()
