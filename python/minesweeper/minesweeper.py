def board(input_board_array):
    valid_array(input_board_array)
    return [map_row(input_board_array, row_num, row) for row_num, row in enumerate(input_board_array)]

def valid_array(input_board_array):
    for a in input_board_array:
        if len(a) != len(input_board_array[0]):
            raise ValueError("Difference length")
        for c in a:
            if c != ' ' and c !=  '*':
                raise ValueError("Invalid cell value")

def adjacent_cells(row, col, max_row, max_col):
    return {(row + i, col + j) 
            for i in [-1, 0, 1] 
            for j in [-1, 0, 1] 
            if row + i >= 0 and col + j >= 0 and row + i < max_row and col + j < max_col} - {(row, col)}

def count_adjacent(input_board_array, row_num, col_num):
    score = sum([1 if input_board_array[r][c] == "*" else 0 for r, c in adjacent_cells(row_num, col_num, len(input_board_array), len(input_board_array[0]))])
    return str(score) if score > 0 else ' '

def map_row(input_board_array, row_num, row):
    return "".join([count_adjacent(input_board_array, row_num, col_num) if cell != '*' else '*' for col_num, cell in enumerate(row)])
