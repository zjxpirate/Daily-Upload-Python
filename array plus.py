
carry_in = [1,3,9]

carry_out = [9,9,9]


def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1

    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A


print(plus_one(carry_in))

print(plus_one(carry_out))
