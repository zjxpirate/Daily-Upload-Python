
import itertools
import heapq


def top_k(k, stream):

    # Entries are compared by their lengths.
    min_heap = [(len(s), s) for s in itertools.islice(stream, k)]

    heapq.heapify(min_heap)

    for next_string in stream:
        # Push next_string and pop the shortest string in min_heap.
        heapq.heappushpop(min_heap, (len(next_string), next_string))


    return [p[1] for p in heapq.nsmallest(k, min_heap)]



stream = ["abc", "abcd", "abcde", "abcdef"]


print(top_k(1, stream))