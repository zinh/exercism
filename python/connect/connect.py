class ConnectGame:
    def __init__(self, board):
        self.board = [row.strip().split(' ') for row in board.split('\n')]

    def get_winner(self):
        if len(self.board) == 1 and len(self.board[0]) == 1:
            return self.board[0][0]
        if self.connected_board('O', self.board):
            return 'O'
        if self.connected_board('X', self.transpose(self.board)):
            return 'X'
        return ''

    # return adjacent cells
    def adjecent_cells(self, row, col):
        return [(row - 1, col), (row - 1, col + 1), 
         (row, col - 1), (row, col + 1), 
         (row + 1, col - 1), (row + 1, col)]

    def connected_board(self, player, board):
        starts = [[(0, col)] for col, first_cell in enumerate(board[0]) if first_cell == player]
        if starts == []:
            return False
        new_cell_inserted = False
        while True:
            for cells in starts:
                for row, col in cells:
                  for neighbor_cell in self.connected_cells(board, row, col):
                      if neighbor_cell[0] == len(board) - 1:
                          return True
                      if neighbor_cell not in cells:
                          cells.append(neighbor_cell)
                          new_cell_inserted = True
            if not new_cell_inserted:
                break
            new_cell_inserted = False
        return False

    def connected_cells(self, board, row, col):
        current_cell = board[row][col]
        return [(r, c) for r, c in self.adjecent_cells(row, col) if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == current_cell]

    def transpose(self, board):
        return [[row[col] for row in board] for col in range(0, len(board[0]))]
