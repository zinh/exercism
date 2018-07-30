def numeral(number):
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    result = []
    while number >= 1000:
        result.append('M')
        number -= 1000
    result.append(hundreds[number // 100])
    number = number % 100
    result.append(tens[number // 10])
    number = number % 10
    result.append(ones[number])
    return ''.join(result)
