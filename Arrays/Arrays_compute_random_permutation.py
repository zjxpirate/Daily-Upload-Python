
import random


list1 = [1, 3, 5, 7, 9]


def random_sampling(k, A):
    for i in range(k):
        #Generate a random index in [i, len(A) - 1]
        r = random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]




def compute_random_permutation(n):
    permutation = list(range(n))
    random_sampling(n, permutation)
    return permutation

result = compute_random_permutation(6)


print(result)
