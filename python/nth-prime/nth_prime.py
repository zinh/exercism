def nth_prime(positive_number):
    if positive_number <= 0:
        raise ValueError("Non-positive number")
    n, i = 0, 2
    prime_list = []
    while True:
        if is_prime(i, prime_list):
            prime_list.append(i)
            n += 1
            if n == positive_number:
                break
        i += 1
    return i

def is_prime(number, prime_list):
    for divisor in prime_list:
        if number % divisor == 0:
            return False
    return True
