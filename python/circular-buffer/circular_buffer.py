class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):
    def __init__(self, capacity):
        self.buffer = [None] * capacity
        self.head = -1
        self.tail = 0

    def read(self):
        if all([c == None for c in self.buffer]):
            raise BufferEmptyException("Buffer empty")
        val = self.buffer[self.tail]
        self.buffer[self.tail] = None
        self.tail = (self.tail + 1) % len(self.buffer)
        print(self.buffer)
        return val

    def write(self, data):
        next_head = (self.head + 1) % len(self.buffer)
        if self.buffer[next_head] != None:
            raise BufferFullException("Buffer full")
        self.buffer[next_head] = data
        self.head = next_head
        print(self.buffer)

    def overwrite(self, data):
        try:
            self.write(data)
        except BufferFullException as e:
            self.buffer[self.tail] = data
            self.tail = (self.tail + 1) % len(self.buffer)
        print(self.buffer)

    def clear(self):
        self.buffer = [None] * len(self.buffer)

#buf = CircularBuffer(2)
#buf.write('1')
#buf.overwrite('2')
