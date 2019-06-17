

# 9. The knapsack problem

import collections

Item = collections.namedtuple('Item', ('weight', 'value'))

thing = [
    Item(weight=5, value=60),
    Item(weight=3, value=50),
    Item(weight=4, value=70),
    Item(weight=2, value=30)
]

def optimum_subject_to_capacity(items, capacity):

    # returns the optimum value when we choose from items[:k + 1] and have a
    # capacity of available_capacity.

    def optimum_sbject_to_item_and_capacity(k, available_capacity):

        if k < 0:
            # no items can be chosen.
            return 0

        if V[k][available_capacity] == -1:

            without_curr_item = optimum_sbject_to_item_and_capacity(k - 1, available_capacity)

            with_curr_item = (0 if available_capacity < items[k].weight else (items[k].value + optimum_sbject_to_item_and_capacity(k - 1, available_capacity - items[k].weight)))

            V[k][available_capacity] = max(without_curr_item, with_curr_item)

        return V[k][available_capacity]

    # V[i][j] holds the optimum value when we choose from items[:i + 1] and have
    # a capacity of j.
    V = [[-1] * (capacity + 1) for _ in items]
    print(V)
    return optimum_sbject_to_item_and_capacity(len(items) - 1, capacity)


print(optimum_subject_to_capacity(thing, 5))




