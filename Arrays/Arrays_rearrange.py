
list1 = [1, 4, 2, 6, 8, 4, 5, 2, 5, 10, 21, 32, 12, 11, 14, 3]

def rearrange(A):
    for i in range(len(A)):
        A[i : i + 2] = sorted(A[i : i + 2], reverse = i % 2)

    return A


result = rearrange(list1)

print(result)