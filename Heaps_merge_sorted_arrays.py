

import heapq


def merge_sorted_arrays(sorted_arrays):
    min_heap = []

    # Builds a list of iterators for each array in sorted_arrays
    sorted_array_iters = [iter(x) for x in sorted_arrays]
    #print(sorted_array_iters)


    print(min_heap)
    # Puts first element fom each iterator in min_heap.
    for i, it in enumerate(sorted_array_iters):
        #print(it)
        first_element = next(it, None)
        #print(first_element)
        if first_element is not None:
            #print(i)
            heapq.heappush(min_heap, (first_element, i))


    #print(min_heap)
    result = []
    while min_heap:
        smallest_entry, smallest_array_i = heapq.heappop(min_heap)
        #print(smallest_entry)
        #print(smallest_array_i)

        smallest_array_iter = sorted_array_iters[smallest_array_i]
        #print(smallest_array_iter)


        result.append(smallest_entry)
        #print(result)

        next_element = next(smallest_array_iter, None)
        if next_element is not None:
            #print(next_element)
            heapq.heappush(min_heap, (next_element, smallest_array_i))
            #print(result)

    return result





input = [[1, 1, 3, 5], [1, 2, 2, 4]]


print(merge_sorted_arrays(input))








