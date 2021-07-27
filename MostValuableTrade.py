lows = [1.0, 2.0, 5.0, 10.0, 11.0, 4.5, 4.3]
highs = [10, 4.5, 6.1, 12, 100, 88, 5]
starts = [2, 3, 5.5, 11, 11, 5, 4.8]

print(f'Lows - {len(lows)}')
print(lows)
print(f'Highs - {len(highs)}')
print(highs)
print(f'Starts - {len(starts)}')
print(starts)

# Assertions
# A low must always be less than a high for a given day
# A start must always be greater than or equal to a low
# A start must be less than or equal to a high
# Buys and sells must take place at the start of the day
# A sell must take place after a buy

# Naive solution
# Scan the array for the biggest in order rise between start and high


naive_max = 0

for index, start in enumerate(starts):
    print(index)
    for futureStart in starts[index + 1:]:
        diff = futureStart - start
        naive_max = diff if diff > naive_max else naive_max

print(naive_max)


# Divide and conquer solution
# Split array in half and search each subset
# Split until array size is 2 and then start calculating
class Result:
    maximum = None
    minimum = None
    best_sale_price = None

    def __init__(self, maximum, minimum, best_sale_price):
        self.maximum = maximum
        self.minimum = minimum
        self.best_sale_price = best_sale_price


def search_for_best_sale_price(array: []) -> Result:
    if array is None or len(array) == 0:
        return Result(0, 0, 0)

    if len(array) == 1:
        return Result(array[0], array[0], float('-inf'))

    result_left = search_for_best_sale_price(array[:len(array) // 2])
    result_right = search_for_best_sale_price(array[len(array) // 2:])

    local_maximum = max(result_left.maximum, result_right.maximum)
    local_minimum = min(result_left.minimum, result_right.minimum)

    local_best = max(result_left.best_sale_price, result_right.best_sale_price, result_right.maximum - result_left.minimum)

    return Result(local_maximum, local_minimum, local_best)


print('Divide and conquer')

result = search_for_best_sale_price(starts)

print(result.best_sale_price)

print('O(n) solution')

minimum = starts[0]
max_profit = 0

for x in starts:
    minimum = x if x < minimum else minimum
    max_profit = x - minimum if x - minimum > max_profit else max_profit

print(max_profit)

