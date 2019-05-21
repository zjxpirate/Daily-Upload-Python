

import collections


Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

Interval = collections.namedtuple('Interval', ('left', 'right'))


inter = [
    Interval(left= 0, right= 3),
    Interval(left= 2, right= 4),
    Interval(left= 3, right= 4),
    Interval(left= 5, right= 7),
    Interval(left= 7, right= 8),
    Interval(left= 8, right= 11),
    Interval(left= 9, right= 11),
    Interval(left= 12, right= 14),
    Interval(left= 12, right= 16),
    Interval(left= 13, right= 15),
    Interval(left= 16, right= 17)
]


def union_of_intervals(intervals):

    # Empty input.
    if not intervals:
        return []

    # Sort intervals according to left endpoints of intervals.
    intervals.sort(key=lambda i: (i.left.val, not i.left.is_closed))
    result = [intervals[0]]
    for i in intervals:
        if intervals and (i.left.val < result[-1].right.val or
                          (i.left.val == result[-1].right.val and
                           (i.left.is_closed or result[-1].right.is_closed))):
            if (i.right.val > result[-1].right.val or
                (i.right.val == result[-1].right.val and i.right.is_closed)):
                result[-1] = Interval(result[-1].left, i.right)
        else:
            result.append(i)
    return result



print(union_of_intervals(inter))
