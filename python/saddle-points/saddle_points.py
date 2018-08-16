def saddle_points(matrix):
    if len(matrix) == 0:
        return set()
    if len({len(row) for row in matrix}) > 1:
        raise ValueError("Invalid matrix")
    return {(r, col) if row_compare(cell, row) and col_compare(cell, col, matrix) else None for (r, row) in enumerate(matrix) for (col, cell) in enumerate(row)} - {None}

def row_compare(number, row):
    return all([number >= c for c in row])

def col_compare(number, col, matrix):
    column = [row[col] for row in matrix]
    return all(number <= c for c in column)
