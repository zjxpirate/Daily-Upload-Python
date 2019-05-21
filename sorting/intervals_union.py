

import collections

# 9. compute the union of intervals

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

Interval = collections.namedtuple('Interval', ('left', 'right'))

#array(tuple(int[left value], bool[left is closed], int[right value], bool[right is closed]))

#[[610, false, 613, true], [204, true, 205, true]]

inter = [
        Interval(Endpoint(False, 610), Endpoint(True, 613)),
        Interval(Endpoint(True, 204), Endpoint(True, 205)),
        Interval(Endpoint(True, 1117), Endpoint(True, 1124)),
        Interval(Endpoint(False, 379), Endpoint(True, 381)),
        Interval(Endpoint(True, 136), Endpoint(False, 137))
    ]


def union_of_intervals(intervals):

    # Empty input.
    if not intervals:
        return []

    # Sort intervals according to left endpoints of intervals.
    intervals.sort(key=lambda i: (i.left.val, not i.left.is_closed))
    print(intervals)

    result = [intervals[0]]
    print(result)

    for i in intervals:

        if intervals and (i.left.val < result[-1].right.val or (i.left.val == result[-1].right.val and (i.left.is_closed or result[-1].right.is_closed))):
            if (i.right.val > result[-1].right.val or (i.right.val == result[-1].right.val and i.right.is_closed)):
                result[-1] = Interval(result[-1].left, i.right)
        else:
            result.append(i)

    return result



print(union_of_intervals(inter))








