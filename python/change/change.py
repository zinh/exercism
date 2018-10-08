def find_minimum_coins(total_change, coins):
    if total_change < 0:
        raise ValueError("Invalid total_change")
    all_results = []
    find_coins(total_change, coins, {}, all_results)
    if all_results == []:
        raise ValueError("No solution")
    min_result = min(all_results, key=lambda result: sum(result.values()))
    return [coin for coin, count in min_result.items() for i in range(1, count + 1)]

def find_coins(total_change, coins, current_result, all_results):
    if total_change == 0:
        all_results.append(current_result)
        return current_result
    valid_coins = list(filter(lambda coin: coin <= total_change, coins))
    if valid_coins == []:
        return None
    for current_coin in valid_coins:
        max_coin = total_change // current_coin
        for i in range(0, max_coin + 1):
            result = {coin: count for coin, count in current_result.items()}
            result[current_coin] = i
            find_coins(total_change - i * current_coin, filter(lambda coin: coin != current_coin, valid_coins), result, all_results)
