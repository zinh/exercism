def say(number):
    if number < 0:
        raise ValueError('Invalid number')
    return unit(number)

def unit(number):
    m = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
            5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
            10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
            15: 'fifteen'}
    return m.get(number)

def tenth(number):
    m = {2: 'twenty', 3: 'thirty', 4: 'fourty', 5: 'fifty'}
    if m.get(number):
        return m.get(number)
    elif 6 <= number <= 9:
        return f'{unit(number)}ty'
