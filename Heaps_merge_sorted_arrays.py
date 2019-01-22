

import heapq


def merge_sorted_arrays(sorted_arrays):
    min_heap = []

    # Builds a list of iterators for each array in sorted_arrays
    sorted_array_iters = [iter(x) for x in sorted_arrays]

    # Puts first element fom each iterator in min_heap.
    for i, it in enumerate(sorted_array_iters):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))



    result = []
    while min_heap:
        smallest_entry, smallest_array_i = heapq.heappop(min_heap)
        smallest_array_iter = sorted_array_iters[smallest_array_i]
        result.append(smallest_entry)
        next_element = next(smallest_array_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_array_i))

    return result





input = [[1, 1, 3, 5], [1, 2, 2, 4]]


print(merge_sorted_arrays(input))








