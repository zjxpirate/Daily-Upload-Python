

import itertools, random, bisect

list1 = [3, 5, 7, 11]

prob1 = [0.5, 0.33, 0.11, 0.06]


def nonuniform_random_number_generation(values, probabilities):
    prefix_sum_of_probabilities = list(itertools.accumulate(probabilities))
    interval_idx = bisect.bisect(prefix_sum_of_probabilities, random.random())
    return values[interval_idx]


result = nonuniform_random_number_generation(list1, prob1)

print(result)