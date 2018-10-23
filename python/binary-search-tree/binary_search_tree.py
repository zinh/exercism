class TreeNode(object):
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        fmt = 'TreeNode(data={}, left={}, right={})'
        return fmt.format(self.data, self.left, self.right)

    def insert(self, value):
        if self.data >= value:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = TreeNode(value)
        else:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = TreeNode(value)
        return self

    def traverse(self):
        left = [] if self.left is None else self.left.traverse()
        right = [] if self.right is None else self.right.traverse()
        return left + [self.data] + right

class BinarySearchTree(object):
    def __init__(self, tree_data):
        root = TreeNode(tree_data[0])
        for value in tree_data[1:]:
            root.insert(value)
        self.root = root

    def data(self):
        return self.root

    def sorted_data(self):
        return self.root.traverse()
