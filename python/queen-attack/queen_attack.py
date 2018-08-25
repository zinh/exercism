class Queen(object):
    def __init__(self, row, column):
        if row < 0 or row >= 8 or column < 0 or column >= 8:
            raise ValueError("Invalid position")
        self.row = row
        self.col = column

    def can_attack(self, another_queen):
        if another_queen.row == self.row and another_queen.col == self.col:
            raise ValueError("Same position")
        return self.same_column(self.col, another_queen.col) or self.same_row(self.row, another_queen.row) or self.same_diagonal(self.row, self.col, another_queen.row, another_queen.col)

    def same_column(self, col1, col2):
        return col1 == col2

    def same_row(self, row1, row2):
        return row1 == row2

    def same_diagonal(self, row1, col1, row2, col2):
        return (row1 - row2)**2 == (col1 - col2)**2
