package circular

const testVersion = 4

type Buffer

func NewBuffer(size int) *Buffer

func (*Buffer) ReadByte() (byte, error)

func (*Buffer) WriteByte(c byte) error

func (*Buffer) Overwrite(c byte)

func (*Buffer) Reset()
