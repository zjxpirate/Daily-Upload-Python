

# 1. fibonacci time: O(n)   space: O(n)

def fibonacci_1(n, cache={}):
    if n <= 1:
        return n
    elif n not in cache:
        cache[n] = fibonacci_1(n-1) + fibonacci_1(n-2)
    return cache[n]

#print(fibonacci(5))




# 2. fibonacci time: O(n)   space: O(1)

def fibonacci_2(n):
    if n <= 1:
        return n

    f_minus_2, f_minus_1 = 0, 1
    for _ in range(1, n):
        f = f_minus_2 + f_minus_1
        f_minus_2, f_minus_1 = f_minus_1, f
    return f_minus_1

print(fibonacci_2(5))



# 3. find max subarray

import itertools

list1 = [904, 40, 523, 12, -335, -385, -124, 481, -31]

def find_maximum_subarray(A):
    min_sum = max_sum = 0
    for running_sum in itertools.accumulate(A):
        min_sum = min(min_sum, running_sum)
        max_sum = max(max_sum, running_sum - min_sum)
    return max_sum

print(find_maximum_subarray(list1))








