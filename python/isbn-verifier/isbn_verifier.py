def verify(isbn):
    isbn = isbn.replace('-', '')
    if len(isbn) != 10:
        return False
    sum = 0
    for idx, c in enumerate(isbn):
        if (c == 'X' and idx != 9) or (c != 'X' and (ord(c) < ord('0') or ord(c) > ord('9'))):
            return False
        val = (ord(c) - 48) if c != 'X' else 10
        #print (val, idx)
        sum += val * (10 - idx)
    if (sum % 11) == 0:
        return True
    else:
        return False
