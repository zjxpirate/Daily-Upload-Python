
import bisect


# 2. compute the intersection of two sorted arrays

list1 = [2, 3, 3, 5, 5, 6, 7, 7, 8, 12]
list2 = [5, 5, 6, 8, 8, 9, 10, 10]

# 1) brute-force approach
# time complexity O(mn)
def intersect_two_sorted_arrays(A, B):
    return [a for i, a in enumerate(A) if (i == 0 or a != A[i-1]) and a in B]

print(intersect_two_sorted_arrays(list1, list2))




# 2) binary search improved version
# time complexity O(mlogn)
def intersect_two_sorted_arrays_2(A, B):
    def is_present(k):
        i = bisect.bisect_left(B, k)
        return i < len(B) and B[i] == k

    return [
        a for i, a in enumerate(A)
        if (i == 0 or a != A[i - 1]) and is_present(a)
    ]

print(intersect_two_sorted_arrays_2(list1, list2))




# 3) best improved version
# time complexity O(m + n)
def intersect_two_sorted_arrays_3(A, B):
    i, j, intersection_A_B = 0, 0, []
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i - 1]:
                intersection_A_B.append(A[i])
            i, j = i + 1, j + 1
        elif A[i] < B[j]:
            i += 1
        else:   # A[i] > B[j]
            j += 1
    return intersection_A_B

print(intersect_two_sorted_arrays_3(list1, list2))


