from functools import reduce

class Matrix(object):
    def __init__(self, matrix_string):
        rows = [list(map(lambda c: int(c), row.split(' '))) for row in matrix_string.split('\n')]
        cols = [[None] * len(rows) for c in rows[0]]
        for row_num, row in enumerate(rows):
            for col_num, i in enumerate(row):
                cols[col_num][row_num] = i
        self.rows = rows
        self.cols = cols

    def row(self, index):
        return self.rows[index]

    def column(self, index):
        return self.cols[index]
