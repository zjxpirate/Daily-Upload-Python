


# 10. enumerate numbers of the form a+b*(2)**(1/2)

import math, bintrees

class Number:
    def __init__(self, a, b):
        self.a, self.b = a, b
        self.val = a + b * math.sqrt(2)

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val


def generate_first_k_a_b_sqrt2(k):

    # initial for 0 + 0 * sqrt(2).
    candidates = bintrees.RBTree([(Number(0, 0), None)])

    result = []
    while len(result) < k:
        next_smallest =candidates.pop_min()[0]

        print("candidates: ", candidates)
        print("next_smallest: ", next_smallest.val)

        result.append(next_smallest.val)
        # adds the next two numbers derived from next_smallest.
        candidates[Number(next_smallest.a + 1, next_smallest.b)] = None
        candidates[Number(next_smallest.a, next_smallest.b + 1)] = None

    return result

print(generate_first_k_a_b_sqrt2(10))


































