def rebase(input_base, digits, output_base):
    if input_base <= 1 or output_base <= 1:
        raise ValueError("Base must be positive number")
    if any([digit < 0 or digit >= input_base for digit in digits]):
        raise ValueError("Digit must be positive number")
    number_in_base10 = to_base10(input_base, digits)
    return from_base10(output_base, number_in_base10)

def to_base10(input_base, digits):
    l = len(digits) - 1
    return sum([digit * input_base ** (l - pos) for pos, digit in enumerate(digits)])

def from_base10(output_base, number):
    digits = []
    while number > 0:
        digits.insert(0, number % output_base)
        number = number // output_base
    return digits
