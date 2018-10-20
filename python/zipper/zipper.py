class Zipper(object):
    def __init__(self, tree, focus = []):
        self.tree = tree
        self.focus = focus

    @staticmethod
    def from_tree(tree):
        return Zipper(tree)

    def value(self):
        return self.tree['value']

    def set_value(self, value):
        return Zipper({'value': value, 'left': self.tree['left'], 'right': self.tree['right']}, self.focus)

    def left(self):
        if self.tree['left'] is None:
            return None
        new_focus = self.focus + [('left', self.tree['value'], self.tree['right'])]
        return Zipper(self.tree['left'], new_focus)

    def set_left(self, tree):
        self.tree['left'] = tree
        return Zipper(self.tree, self.focus)

    def right(self):
        if self.tree['right'] is None:
            return None
        new_focus = self.focus + [('right', self.tree['value'], self.tree['left'])]
        return Zipper(self.tree['right'], new_focus)

    def set_right(self, tree):
        self.tree['right'] = tree
        return Zipper(self.tree, self.focus)

    def up(self):
        if not self.focus:
            return Zipper(self.tree)
        direction, value, branch = self.focus[-1]
        if direction == 'left':
            tree = {'value': value, 'left': self.tree, 'right': branch}
            return Zipper(tree, self.focus[0:-1])
        if direction == 'right':
            tree = {'value': value, 'left': branch, 'right': self.tree}
            return Zipper(tree, self.focus[0:-1])

    def to_tree(self):
        if not self.focus:
            return self.tree
        zipper = Zipper(self.tree, self.focus)
        while True:
            zipper = zipper.up()
            if not zipper.focus:
                return zipper.tree
