def handshake(code):
    m = {1: 'wink', 2: 'double blink', 4: 'close your eyes', 8: 'jump'}
    result = []
    actions = [action for n, action in m.items() if code & n > 0]
    if code & 16 > 0:
        return actions[::-1]
    else:
        return actions

def secret_code(actions):
    m = {'wink': 1, 'double blink': 2, 'close your eyes': 4, 'jump': 8}
    code = [m[action] for action in actions]
    if len(code) >= 2 and code[0] > code[1]:
        code.append(16)
    return sum(code)
