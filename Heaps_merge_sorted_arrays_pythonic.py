

import heapq

# Pythonic solution, uses the heapq.merge() method which takes multiple inputs.

def merge_sorted_arrays_pythonic(sorted_arrays):
    return list(heapq.merge(*sorted_arrays))




input = [[1, 3, 5], [2, 4, 6]]


print(merge_sorted_arrays_pythonic(input))



