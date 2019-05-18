

# 4. computing the h-index

list1 = [10, 3, 12, 7, 8, 5, 6, 4, 1, 9]

def h_index(citations):
    citations.sort()
    n = len(citations)
    for i, c in enumerate(citations):
        if c >= n - i:
            return n - i

    return 0

print(h_index(list1))


