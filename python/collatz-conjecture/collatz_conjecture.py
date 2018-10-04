def collatz_steps(number):
    if number <= 0:
        raise ValueError("Must be a positive number")
    if number == 1:
        return 0
    if number % 2 == 0:
        return 1 + collatz_steps(number // 2)
    else:
        return 1 + collatz_steps(number * 3 + 1)
