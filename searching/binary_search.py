


# 1. Binary Search
list1 = [5, 6, 7, 8, 9, 10, 11, 12, 13]

def bsearch(t, A):
    L, U = 0, len(A) - 1
    while L <= U:
        M = L + (U - L) // 2  # M = (L + U) // 2 will cause overflow
        if A[M] < t:
            L = M + 1
        elif A[M] == t:
            return M
        else:
            U = M - 1

    return -1

print(bsearch(9, list1))


















