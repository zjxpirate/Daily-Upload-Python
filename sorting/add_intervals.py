

import collections

# 8. merging intervals

Interval = collections.namedtuple('Interval', ('left', 'right'))


def add_interval(disjoint_intervals, new_interval):
    i, result = 0, []

    print(disjoint_intervals[i])

    # processes intervals in disjoint_intervals which come before new_interval
    while (i < len(disjoint_intervals) and new_interval.left > disjoint_intervals[i].right):
        print("hello")
        result.append(disjoint_intervals[i])
        i += 1

    # processes intervals in disjoint_intervals which overlap eith new_interval
    while (i < len(disjoint_intervals) and new_interval.right >= disjoint_intervals[i].left):
        # if [a, b] and [c, d] overlap, union is [min(a, c), max(b, d)]
        new_interval = Interval(min(new_interval.left, disjoint_intervals[i].left), max(new_interval.right, disjoint_intervals[i].right))
        i += 1

    # processes intervals in disjoint_intervals which come after new_interval
    return result + [new_interval] + disjoint_intervals[i:]





