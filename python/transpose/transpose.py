def transpose(input_lines):
    if len(input_lines) == 0:
        return ''
    input_lines = input_lines.split('\n')
    max_length = max([len(line) for line in input_lines])
    return "\n".join([map_line(col, input_lines) for col in range(0, max_length)])

def map_line(col, lines):
    return "".join([calc_value(row, col, line, lines) for row, line in enumerate(lines)])

# Look ahead
def ahead_blank(row, col, lines):
    return all([col >= len(lines[p_row]) for p_row in range(row, len(lines))])

def calc_value(row, col, line, lines):
    if col < len(line):
        return line[col]
    elif ahead_blank(row, col, lines):
        return ''
    else:
        return ' '
