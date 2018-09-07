from math import ceil

def binary_search(list_of_numbers, number):
    if len(list_of_numbers) == 0:
        raise ValueError("Not found")
    return binary_search_recur(list_of_numbers, number, 0, len(list_of_numbers))

def binary_search_recur(list_of_numbers, number, lower, upper):
    if upper <= lower:
        raise ValueError("Not found")
    print(lower, upper)
    mid = ceil((upper + lower) / 2)
    if mid >= len(list_of_numbers):
        raise ValueError("Not found")
    if list_of_numbers[mid] == number:
        return mid
    elif list_of_numbers[mid] > number:
        return binary_search_recur(list_of_numbers, number, lower, mid)
    else:
        return binary_search_recur(list_of_numbers, number, mid, upper)

print(binary_search([1, 3, 4, 6, 8, 9, 11], 0))
