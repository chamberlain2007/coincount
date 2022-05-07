coin_count = 69
coin_values = [25, 10, 5, 1]
target_value = 420

cache = {}

def get_possible_values(coin_count, target_value, max_value):
    cache_key = (coin_count, target_value, max_value)

    if cache_key in cache:
        return cache[cache_key]
    
    results = []

    if coin_count == 1:
        for coin_value in coin_values:
            if coin_value <= max_value and coin_value == target_value:
                results.append([coin_value])
    else:
        for coin_value in coin_values:
            if coin_value <= max_value and coin_value <= target_value:
                for possible_values in get_possible_values(coin_count - 1, target_value - coin_value, coin_value):
                    if len(possible_values) > 0:
                        res = [coin_value]
                        res.extend(possible_values)
                        results.append(res)
    
    cache[cache_key] = results

    return results

def count_values(possible_values):
    return ", ".join(f'{possible_values.count(x)} x {x}' for x in coin_values[::-1])
    
possible_values = get_possible_values(coin_count, target_value, coin_values[0])

print("\n".join(count_values(x) for x in possible_values))
print(f'{len(possible_values)} combinations found')