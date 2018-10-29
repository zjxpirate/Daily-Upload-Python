
list1 = [4, 3, 2, 5, 6, 1, -3, 0, -1, 1, 1]


def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]

    #keep the following invariants during partition
    #bottom group: A[:smaller]
    #middle group: A[smaller:equal]
    #unclassified group: A[equal:larger]
    #top group: A[larger:]

    smaller, equal, larger = 0, 0, len(A)

    #keep iterating as long as there is an unclassified element

    while equal < larger:
        #A[equal] is the incoming unclassified element
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif A[equal] == pivot:
            equal += 1
        else:   #A[equal] > pivot
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]


dutch_flag_partition(5, list1)

print(list1)


