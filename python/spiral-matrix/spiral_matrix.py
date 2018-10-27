def spiral(size):
    if size == 0:
        return []
    return fill_matrix(0, size - 1, 1, [[0 for col in range(0, size) ] for row in range(0, size)])

def fill_matrix(start_row, end_row, start_number, matrix):
    if start_row > end_row:
        return matrix
    i = 0
    for col in range(start_row, end_row + 1):
        matrix[start_row][col] = start_number + i
        i += 1
    for row in range(start_row + 1, end_row + 1):
        matrix[row][end_row] = start_number + i
        i += 1
    for col in range(end_row - 1, start_row - 1, -1):
        matrix[end_row][col] = start_number + i
        i += 1
    for row in range(end_row - 1, start_row, -1):
        matrix[row][start_row] = start_number + i
        i += 1
    return fill_matrix(start_row + 1, end_row - 1, start_number  + i, matrix)
