def binary_search(list_of_numbers, number):
    if len(list_of_numbers) == 0 or number < list_of_numbers[0] or number > list_of_numbers[-1]:
        raise ValueError("Not found")
    if len(list_of_numbers) == 1 and list_of_numbers[0] != number:
        raise ValueError("Not found")
    if len(list_of_numbers) == 1 and list_of_numbers[0] == number:
        return 0
    return binary_search_recur(list_of_numbers, number, 0, len(list_of_numbers))

def binary_search_recur(list_of_numbers, number, lower, upper):
    if upper <= lower or ((upper - lower) == 1 and list_of_numbers[upper] != number and list_of_numbers[lower] != number):
        raise ValueError("Not found")
    mid = (upper + lower) // 2
    if mid >= len(list_of_numbers):
        raise ValueError("Not found")
    if list_of_numbers[mid] == number:
        return mid
    elif list_of_numbers[mid] > number:
        return binary_search_recur(list_of_numbers, number, lower, mid)
    else:
        return binary_search_recur(list_of_numbers, number, mid, upper)
