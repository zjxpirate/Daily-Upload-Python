

list1 = [0, 1, 2, 0, 2, 1, 1]

def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]

    #First pass: group elements smaller than pivoy.
    for i in range(len(A)):
        #look for a smaller element
        for j in range(i+1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break

    #second pass: group elements larger than pivot.
    for i in reversed(range(len(A))):
        #look for a larger element, stop when we reach an element less than
        #pivot, since first pass has moved them to the start of A.
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break


dutch_flag_partition(4, list1)
print(list1)








