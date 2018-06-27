def decode(string):
    result = ""
    current_count = ""
    i = 0
    while i < len(string):
        c = string[i]
        if '0' <= c <= '9':
            current_count += c
        else:
            if current_count == '':
                result += c
            else:
                result += int(current_count) * c
            current_count = ''
        i += 1
    return result

def encode(string):
    current_count = 0
    current_c = ''
    result = ''
    string += ' '
    for (idx, c) in enumerate(string):
        if c != current_c or idx == len(string) - 1:
            result += str(current_count) + current_c if current_count > 1 else current_c
            current_c = c
            current_count = 1
        else:
            current_count += 1
    return result
