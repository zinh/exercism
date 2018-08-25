def is_paired(input_string):
    pairs = {')': '(', '}': '{', ']': '['}
    stack = []
    for symbol in input_string:
        for c in pairs.values():
            if symbol == c:
                stack.append(symbol)
                break
        for c in pairs:
            if symbol == c and len(stack) > 0 and stack[-1] == pairs[c]:
                stack.pop()
                break
            elif symbol == c:
                return False
    return True if len(stack) == 0 else False
