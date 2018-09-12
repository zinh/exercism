class Node(object):
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.succeeding = succeeding
        self.previous = previous

class LinkedList(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def pop(self):
        if self.head != None:
            value = self.head.value
            self.head = self.head.previous
            return value

    def push(self, value):
        if self.head == None:
            node = Node(value)
            self.head = node
            self.tail = node
        else:
            node = Node(value, previous=self.head)
            self.head.succeeding = node
            self.head = node

    def shift(self):
        if self.tail != None:
            value = self.tail.value
            self.tail = self.tail.succeeding
            if self.tail != None:
              self.tail.previous = None
            return value

    def unshift(self, value):
        if self.tail == None:
            node = Node(value)
            self.tail = node
            self.head = node
        else:
            node = Node(value, succeeding=self.tail)
            self.tail.previous = node
            self.tail = node

    def __len__(self):
        l = 0
        current_node = self.head
        while current_node != None:
            current_node = current_node.previous
            l += 1
        return l

    def __iter__(self):
        return LinkedList(self.head, self.tail)

    def __next__(self):
        if self.tail == None:
            raise StopIteration
        else:
            value = self.tail.value
            self.tail = self.tail.succeeding
            return value
