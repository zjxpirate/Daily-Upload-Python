


import collections

# 9. find the smallest subarray covering all values

para = ["apple", "banana", "apple", "apple", "dog", "cat", "apple", "dog", "banana", "apple", "cat", "dog"]
key = ["apple", "apple"]

Subarray = collections.namedtuple('Subarray', ('start', 'end'))

def find_smallest_subarray_covering_set(paragraph, keywords):

    keywords_to_cover = collections.Counter(keywords)
    print(keywords_to_cover)

    result = Subarray(-1, -1)
    print(result)

    remaining_to_cover = len(keywords)
    print(remaining_to_cover)

    left = 0

    for right, p in enumerate(paragraph):
        if p in keywords:
            keywords_to_cover[p] -= 1
            if keywords_to_cover[p] >= 0:
                remaining_to_cover -= 1

        # keeps advancing left until keywords_to_cover does not contain all keywords.
        while remaining_to_cover == 0:
            if result == (-1, -1) or right - left < result[1] - result[0]:
                result = (left, right)
            pl = paragraph[left]
            if pl in keywords:
                keywords_to_cover[pl] += 1
                if keywords_to_cover[pl] > 0:
                    remaining_to_cover += 1
            left += 1

    return result

print(find_smallest_subarray_covering_set(para, key))


