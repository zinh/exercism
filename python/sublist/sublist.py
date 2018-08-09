EQUAL = 1
SUBLIST = 2
SUPERLIST = 3
UNEQUAL = 4

def check_lists(first_list, second_list):
    if len(first_list) == 0 and len(second_list) > 0:
        return SUBLIST
    if len(first_list) >0 and len(second_list) == 0:
        return SUPERLIST
    if first_list == second_list:
        return EQUAL
    if len(first_list) > len(second_list) and sublist(first_list, second_list):
        return SUPERLIST
    if len(first_list) < len(second_list) and sublist(second_list, first_list):
        return SUBLIST
    return UNEQUAL

def sublist(first_list, second_list):
    for idx, item in enumerate(first_list):
        is_sublist = True
        for idx2, second in enumerate(second_list):
            if idx + idx2 >= len(first_list) or first_list[idx + idx2] != second:
                is_sublist = False
                break
        if is_sublist:
            return True
    return False
