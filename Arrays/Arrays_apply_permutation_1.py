

arr = ['a', 'b', 'c', 'd', 'e', 'f']

permutation = [3, 4, 1, 2, 5, 0]


def apply_permutation(perm, A):
    for i in range(len(A)):

        # Check if the element  at index i has not been moved by checking if
        # perm[i] is nonnegative.

        next = i
        while perm[next] >= 0:
            A[i], A[perm[next]] = A[perm[next]], A[i]
            temp = perm[next]

            # Subtracts len(perm) from an entry in perm to make it negative.
            # which indicating the corresponding move has been performed.

            perm[next] -= len(perm)
            next = temp

    #restore perm.
    perm[:] = [a + len(perm) for a in perm]

    return arr



result = apply_permutation(permutation, arr)

print(result)