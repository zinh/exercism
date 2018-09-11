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
        pass

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
        else:
            self.root = self.root.next

    def reversed(self):
        current_node = self.root

class EmptyListException(Exception):
    pass
