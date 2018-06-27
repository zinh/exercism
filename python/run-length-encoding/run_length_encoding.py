def decode(string):
    return string

def encode(string):
    current_count = 0
    current_c = ''
    result = ''
    for c in string:
        if c == current_c:
            current_count += 1
        else:
            result += str(current_count) + current_c if current_count > 1 else current_c
            current_c = c
            current_count = 1
    return result
