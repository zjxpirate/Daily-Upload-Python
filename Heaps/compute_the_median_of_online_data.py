

import itertools, heapq, math


# 1. Heaps bootcamp top_k()
# import itertools
# import heapq
#
# stream = ['abc', 'abcde', 'abcdefg', 'abcdefghi']
#
# def top_k(k, stream):
#
#     # Entries are compared by their lengths.
#
#     min_heap = [(len(s), s) for s in itertools.islice(stream, k)]
#     heapq.heapify(min_heap)
#
#     for next_string in stream:
#
#         # Push next_string and pop the shortest string in min_heap.
#         heapq.heappushpop(min_heap, (len(next_string), next_string))
#
#     return [p[1] for p in heapq.nsmallest(k, min_heap)]
#     #return [p[1] for p in itertools.islice(min_heap, k)]
#     #return min_heap
#
# print(top_k(2, stream))




# # 2. Merge sorted files
#
# sorted_arrays = [[3, 5, 7], [0, 6], [0, 6, 28]]
#
# def merge_sorted_arrays(sorted_arrays):
#
#     min_heap = []
#
#     # Builds a list of iterators for each array in sorted_arrays.
#     sorted_arrays_iters = [iter(x) for x in sorted_arrays]
#
#     # Puts first element from each iterator in min_heap.
#     for i, it in enumerate(sorted_arrays_iters):
#         first_element = next(it, None)
#         if first_element is not None:
#             heapq.heappush(min_heap, (first_element, i))
#
#     result = []
#
#     while min_heap:
#         smallest_entry, smallest_array_i = heapq.heappop(min_heap)
#         smallest_array_iter = sorted_arrays_iters[smallest_array_i]
#         result.append(smallest_entry)
#         next_element = next(smallest_array_iter, None)
#         if next_element is not None:
#             heapq.heappush(min_heap, (next_element, smallest_array_i))
#     return result
#
# print(merge_sorted_arrays(sorted_arrays))




# # 3. Merge sorted files pythonic way
# sorted_arrays = [[3, 5, 7], [0, 6], [0, 6, 28]]
#
# import heapq
# def merge_sorted_arrays_pythonic(sorted_arrays):
#     return list(heapq.merge(*sorted_arrays))
#
# print(merge_sorted_arrays_pythonic(sorted_arrays))




## 4. Sort an increasing decreasing array
#
# list1 = [57, 131, 493, 294, 221, 339, 418, 452, 442, 190]
#
# def sort_k_increasing_decreasing_array(A):
#
#     # Decomposes A into a set of sorted arrays.
#     sorted_subarrays = []
#     INCREASING, DECREASING = range(2)
#     subarray_type = INCREASING
#     start_idx = 0
#
#     for i in range(1, len(A) + 1):
#         if (i == len(A) or (A[i - 1] < A[i] and subarray_type == DECREASING) or (A[i - 1] >= A[i] and subarray_type == INCREASING)):
#             sorted_subarrays.append(A[start_idx:i] if subarray_type == INCREASING else A[i - 1:start_idx - 1:-1])
#             start_idx = i
#             subarray_type = (DECREASING if subarray_type == INCREASING else INCREASING)
#
#     return merge_sorted_arrays(sorted_subarrays)
#
# print(sort_k_increasing_decreasing_array(list1))




# # 5. Pythonic solution, uses a stateful object to trace the monotonic subarrays.
#
# list1 = [57, 131, 493, 294, 221, 339, 418, 452, 442, 190]
#
# def sort_k_increasing_decreasing_array_pythonic(A):
#     class Monotonic:
#         def __init__(self):
#             self._last = float('-inf')
#         def __call__(self, curr):
#             result = curr < self._last
#             self._last = curr
#             return result
#
#     return merge_sorted_arrays([list(group)[::-1 if is_decreasing else 1] for is_decreasing, group in itertools.groupby(A, Monotonic())])
#
# print(sort_k_increasing_decreasing_array_pythonic(list1))




## 6. Sort an almost sorted array
#
# list2 = [3, -1, 2, 6, 4, 5, 8]
#
# def sort_approximately_sorted_array(sequence, k):
#     k+=1
#     min_heap = []
#
#     # Add the first k elements into the min_heap. Stop if there are fewer than k elements.
#     for x in itertools.islice(sequence, k):
#         heapq.heappush(min_heap, x)
#
#     result = []
#
#     # for every new element, add it to min_heap and extract the smallest.
#     for x in sequence[k:]:
#         smallest = heapq.heappushpop(min_heap, x)
#         result.append(smallest)
#
#     # sequence is exhausted, iteratively extracts the remaining elements.
#     while min_heap:
#         smallest = heapq.heappop(min_heap)
#         result.append(smallest)
#
#     return result
#
# print(sort_approximately_sorted_array(list2, 2))




## 7. Compute the k closest stars
#
# list3 = [[4,4,4], [5,5,5], [1,1,1], [3,3,3]]
#
# class Star:
#     def __init__(self, x, y, z):
#         self.x, self.y, self.z = x, y, z
#
#     @property
#     def distance(self):
#         return math.sqrt(self.x**2 + self.y**2 + self.z**2)
#
#     def __lt__(self, rhs):
#         return self.distance < rhs.distance
#
# def find_closest_k_stars(stars, k):
#     # max_heap to store the closest k stars seen so far.
#     max_heap = []
#     for star in stars:
#         # Add each star to the max-heap. If the max-heap size exceeds k, remove
#         # the maximum element fron the max-heap.
#         # As python has only min-heap, insert tuple (negative of distance,star)
#         # to sort in reversed distance order.
#         heapq.heappush(max_heap, (-star.distance, star))
#         if len(max_heap) == k + 1:
#             heapq.heappop(max_heap)
#
#     # Iteratively extract from the max-heap. which yields the stars sorted
#     # according from furthest to closest.
#     return [s[1] for s in heapq.nlargest(k, max_heap)]
#
#
#
# print(find_closest_k_stars(list3, 3))




## 8. Compute the median of online data

list5 = [1, 0, 3, 5, 2, 0, 1]

def online_median(sequence):
    # min_heap stores the larger half seen so far.
    min_heap = []
    # max_heap stores the smaller half seen so far.
    # values in max_heap are negative.
    max_heap = []
    result = []

    for x in sequence:
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, x))
        # ensure min_heap and max_heap have equal number of elements if an even number
        # of elements is read; otherwise, min_heap must have one more element than max_heap.
        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        result.append(0.5 * (min_heap[0] + (-max_heap[0])) if len(min_heap) == len(max_heap) else min_heap[0])


    return result

print(online_median(list5))




# 9. Compute the k largest elements in a max-heap




















