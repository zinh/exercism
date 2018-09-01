height = 4
width = 3

def convert(input_grid):
    lines = [input_grid[i:i + height] for i in range(0, len(input_grid), height)]
    return ','.join([convert_line(line) for line in lines])

# line: array of string
def convert_line(line):
    #import pdb; pdb.set_trace()
    line_width = len(line[0])
    return "".join([analyze_number([row[col:col + width] for row in line]) for col in range(0, line_width, width)])

# number: 3x4
def analyze_number(number):
    if len(number) != height or len(number[0]) != width:
        raise ValueError('Invalid number')
    m = {'0': [" _ ", "| |", "|_|"], '1': ["   ", "  |", "  |"], '2': [" _ ", " _|", "|_ "], 
         '3': [" _ ", " _|", " _|"], '4': ["   ", "|_|", "  |"], '5': [" _ ", "|_ ", " _|"], 
         '6': [" _ ", "|_ ", "|_|"], '7': [" _ ", "  |", "  |"], '8': [" _ ", "|_|", "|_|"], 
         '9': [" _ ", "|_|", " _|"]}
    for num, bitmaps in m.items():
        if compare_bitmaps(number, bitmaps):
            return num
    return '?'

def compare_bitmaps(number, bitmaps):
    for idx, bitmap in enumerate(bitmaps):
        if bitmap != number[idx]:
            return False
    return True
