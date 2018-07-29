def numeral(number):
    m = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
    result = []
    for num, roman in m.items():
