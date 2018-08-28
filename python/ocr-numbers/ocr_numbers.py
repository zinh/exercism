def convert(input_grid):
    # 011 1
    # 001 222 010 2
    # 222 011 3
    # 010 020 011 4
    # 010 222 001 5
    # 011 222 001 6
    # 200 011 7
    # 011 222 011 8
    # 010 222 011 9
    # 011 202 011 0
    # Using longest matching series
    for col in range(0, len(input_grid)):
