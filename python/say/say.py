def say(number):
    if number < 0 or number >= 1e12:
        raise ValueError('Invalid number')
    if number < 100:
        return less_than_99(number)
    if number < 1000:
        return hundred(number)
    return thousand(number)

def unit(number):
    m = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
            5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
            10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    return m.get(number)

def tenth(number):
    m = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 8: 'eighty'}
    if m.get(number):
        return m.get(number)
    elif 6 <= number <= 9:
        return f'{unit(number)}ty'
    else:
        return ''

def thousand(number):
    m = {1e9: 'billion', 1e6: 'million', 1e3: 'thousand', 1e2: 'hundred'}
    result = []
    for k, v in m.items():
        if number // k > 0:
            result.append(f'{hundred(number // k)} {v}')
            number = number % k
    if number > 0:
        result.append('and')
        result.append(hundred(number))
    return ' '.join(result)

def hundred(number):
    if number // 100 > 0:
        if number % 100 == 0:
            return f'{less_than_99(number // 100)} hundred'
        else:
            return f'{less_than_99(number // 100)} hundred and {less_than_99(number % 100)}'
    else:
        return less_than_99(number)

def less_than_99(number):
    if 0 <= number < 20:
        return unit(number)
    elif 20 <= number <= 99:
        if number % 10 != 0:
            return '-'.join([tenth(number // 10), unit(number % 10)])
        else:
            return tenth(number // 10)
