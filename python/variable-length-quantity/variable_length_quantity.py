def encode(numbers):
    results = []
    for number in numbers:
        block = number % 128
        number = number // 128
        result = [block]
        while number != 0:
            block = number % 128
            number = number // 128
            result = [block + 128] + result
        results += result
    return results

def decode(bytes_):
    groups = []
    group = []
    for byte in bytes_:
        if byte < 128:
            group.append(byte)
            groups.append(group)
            group = []
        else:
            group.append(byte - 128)
    if len(group) > 0:
        raise ValueError("Incomplete sequence")
    return [convert_number(group) for group in groups]

def convert_number(groups):
    number = 0
    groups.reverse()
    for idx, group in enumerate(groups):
        number = number + group * (128**idx)
    return number

#print(encode([0x2000, 0x123456, 0xfffffff, 0x0, 0x3fff, 0x4000]))
