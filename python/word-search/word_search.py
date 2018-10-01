class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch(object):
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def search(self, word):
        origins = [self.adjacent_points(Point(x, y), len(word)) for x, row in enumerate(self.puzzle) for y, cell in enumerate(row) if cell == word[0]]
        for origin in origins:
            for line in origin:
                if self.detect_word(line) == word:
                    return (Point(line[0][1], line[0][0]), Point(line[-1][1], line[-1][0]))

    def adjacent_points(self, origin, length):
        directions = [(1,0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        return [self.line_through(origin, length, direction) for direction in directions]

    def line_through(self, origin, length, direction):
        return [(origin.x + d * direction[0], origin.y + d * direction[1]) for d in range(0, length)]

    def detect_word(self, line):
        try:
          return "".join([self.puzzle[point[0]][point[1]] for point in line])
        except:
          return None
