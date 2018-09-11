class Node(object):
    def __init__(self, value, next_node):
        self.value = value
        self.next = next_node

    def value(self):
        return self.value

    def next(self):
        return self.next

class LinkedList(object):
    def __init__(self, values=[]):
        if len(values) == 0:
            self.root = None
        else:
            values = values[::-1]
            self.root = Node(values[0], None)
            prev_node = self.root
            for value in values[1:]:
                current_node = Node(value, None)
                prev_node.next = current_node
                prev_node = current_node

    def __len__(self):
        current_node = self.root
        l = 0
        while current_node != None:
            l += 1
            current_node = current_node.next
        return l

    def __iter__(self):
        return self

    def __next__(self):
        if self.root == None:
            raise StopIteration
        else:
            current_value = self.root.value
            self.root = self.root.next
            return current_value

    def head(self):
        if self.root != None:
            return self.root
        else:
            raise EmptyListException("Empty list")

    def push(self, value):
        if self.root == None:
            self.root = Node(value, None)
        else:
            newNode = Node(value, self.root)
            self.root = newNode

    def pop(self):
        if self.root == None:
            raise EmptyListException("Empty list")
        value = self.root.value
        self.root = self.root.next
        return value

    def reversed(self):
        if self.root == None:
            return LinkedList([])
        prev_node = self.root
        current_node = self.root.next
        prev_node.next = None
        while current_node != None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.root = prev_node
        return self

class EmptyListException(Exception):
    pass
