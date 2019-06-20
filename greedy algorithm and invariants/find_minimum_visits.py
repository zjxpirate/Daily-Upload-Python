

# 4. the interval covering problem

import collections
import operator

Interval = collections.namedtuple('Interval', ('left', 'right'))

list1 = [
    Interval(left=1, right=2),
    Interval(left=2, right=3),
    Interval(left=3, right=4),
    Interval(left=2, right=3),
    Interval(left=3, right=4),
    Interval(left=4, right=5)
]

def find_minimum_visits(intervals):

    # sort intervals based on the right endpoints.
    intervals.sort(key=operator.attrgetter('right'))
    last_visit_time, num_visits = float('-inf'), 0

    for interval in intervals:
        if interval.left > last_visit_time:
            # the current right endpoint, last_visit_time, will not cover any more intervals.
            last_visit_time = interval.right
            num_visits += 1

    return num_visits


print(find_minimum_visits(list1))




