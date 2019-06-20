

# 6. the 3 sum problem

list1 = [11, 2, 5, 7, 3]

def has_two_sum(A, t):
    i, j = 0, len(A) - 1

    while i <= j:
        if A[i] + A[j] == t:
            return True
        elif A[i] + A[j] < t:
            i += 1
        else:   # A[i] + A[j] > t.
            j -= 1
    return False


def has_three_sum(A, t):
    A.sort()
    # finds if the sum of two numbers in A equals to t - a.
    return any(has_two_sum(A, t - a) for a in A)

print(has_three_sum(list1, 21))


