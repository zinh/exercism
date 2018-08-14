def encode(message, rails):
    rows = [[] for r in range(0, rails)]
    r = 0
    direction = 1
    for idx, c in enumerate(message):
        rows[r] += [c]
        if r == rails - 1:
            direction = -1
        elif r == 0:
            direction = 1
        r = r + direction
    return ''.join([''.join(row) for row in rows])


def decode(encoded_message, rails):
    rows = []
    for r in range(0, rails):
        distance = 2 * (rails - 2) + 1 - 2*r
        print(r, distance)
        rows += [encoded_message[r::distance]]
    return rows

print(decode('WECRLTEERDSOEEFEAOCAIVDEN', 3))
