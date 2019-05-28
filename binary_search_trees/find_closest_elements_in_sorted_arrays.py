
from bstNode import BstNode, insert

tree_1 = BstNode(19, None, None)

insert(7, tree_1)
insert(43, tree_1)
insert(3, tree_1)
insert(11, tree_1)
insert(23, tree_1)
insert(47, tree_1)
insert(2, tree_1)
insert(5, tree_1)
insert(17, tree_1)
insert(37, tree_1)
insert(53, tree_1)
insert(13, tree_1)
insert(29, tree_1)
insert(41, tree_1)
insert(31, tree_1)



# 9. find the closest entries in three sorted arrays

import bintrees

#list1 = [[3, 6, 9, 12, 15], [8, 16, 24]]
list1 = [[5, 10, 15], [3, 6, 9, 12, 15], [8, 16, 24]]

def find_closest_elements_in_sorted_arrays(sorted_arrays):

    min_distance_so_far = float('inf')

    # stores array iterators in each entry.
    iters = bintrees.RBTree()

    for idx, sorted_array in enumerate(sorted_arrays):
        it = iter(sorted_array)

        print("it: ", it)

        first_min = next(it, None)

        print("first_min: ", first_min)

        print("idx: ", idx)
        print("sorted_array: ", sorted_array)

        if first_min is not None:
            iters.insert((first_min, idx), it)

            print("iters: ", iters)

    print("\n")
    while True:

        min_value, min_idx = iters.min_key()

        print("min_value: ", min_value)
        print("min_idx: ", min_idx)

        max_value = iters.max_key()[0]

        print("max_value: ", max_value)

        min_distance_so_far = min(max_value - min_value, min_distance_so_far)

        print("min_distance_so_far: ", min_distance_so_far)


        it = iters.pop_min()[1]

        print("iters: ", iters)

        next_min = next(it, None)
        print("next_min: ", next_min)


        # return if some array has no remaining elements.
        if next_min is None:
            return min_distance_so_far
        iters.insert((next_min, min_idx), it)
        print("iters: ", iters)
        print("\n")

print(find_closest_elements_in_sorted_arrays(list1))








