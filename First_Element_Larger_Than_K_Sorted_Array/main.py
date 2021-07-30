# Find the first element in a sorted array larger than K
import math

array = [20, 22, 22.5, 33.7, 80, 900, 1011]
elementToFind = 10000


# Naive solution
def linear_search(k: int):
    for i in array:
        if i > k:
            return i


# Divide and conquer based solution
def divide_and_conquer(k: int, elements: []) -> int:
    if len(elements) == 1:
        return elements[0] if elements[0] > k else None

    mid_point = len(elements) // 2
    target_element = elements[mid_point]
    result = None

    if target_element <= k: # If the target_element is less than k we search to the right for larger numbers
        return divide_and_conquer(k, elements[mid_point:])
    elif target_element > k:
        result = divide_and_conquer(k, elements[:mid_point])
        return result if result is not None and result < target_element else target_element


print(linear_search(elementToFind))
print(divide_and_conquer(elementToFind, array))




