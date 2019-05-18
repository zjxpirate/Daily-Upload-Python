

# 3. merge two sorted arrays

list1 = [11, 13, 17, 0, 0, 0, 0]
list2 = [3, 7, 8, 10]

def merge_two_sorted_arrays(A, m, B, n):
    a, b, write_idx = m - 1, n - 1, m + n - 1

    while a >= 0 and b >= 0:
        if A[a] > B[b]:
            A[write_idx] = A[a]
            a -= 1
        else:
            A[write_idx] = B[b]
            b -= 1
        write_idx -= 1

    while b >= 0:
        A[write_idx] = B[b]
        write_idx, b = write_idx - 1, b - 1

merge_two_sorted_arrays(list1, 3, list2, 4)

print(list1)




