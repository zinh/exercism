def slices(series, length):
    if length <= 0 or len(series) < length:
        raise ValueError("Invalid length")
    start_pos = 0
    end_pos = start_pos + length
    results = []
    while end_pos <= len(series):
        results.append(series[start_pos:end_pos])
        start_pos += 1
        end_pos = start_pos + length
    return results
