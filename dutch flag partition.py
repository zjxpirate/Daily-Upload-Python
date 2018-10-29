
list1 = [22, 13, 14, 1, 12, 4, 6, 1, 89, 23, 12, 14, 56, 64, 23]

def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    #first pass: group elements smaller than pivot.
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1

    #second pass: group elements larger than pivot
    larger = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1


dutch_flag_partition(14, list1)

print(list1)
