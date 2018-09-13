def make_diamond(letter):
    if letter == 'A':
        return 'A\n'
    max_length = 2 * (ord(letter) - ord('A') - 1) + 3
    lines = [make_line(chr(c), max_length) for c in range(ord('A'), ord(letter) + 1)]
    return '\n'.join(lines + list(reversed(lines))[1:]) + '\n'

def make_line(letter, max_length):
    space_between = 2 * (ord(letter) - ord('A') - 1) + 1
    padding_space = (max_length - space_between - 2) // 2
    spaces = lambda c: "".join([' '] * c)
    if space_between < 0:
      return spaces(padding_space) + letter + spaces(padding_space)
    else:
      return spaces(padding_space) + letter + spaces(space_between) + letter + spaces(padding_space)
