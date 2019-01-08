
import random

list1 = [1, 3, 5, 7, 9, 11, 13, 15, 17]

def random_sampling(k, A):
    for i in range(k):

        # Generate a random index in [i, len(A) - 1].

        r = random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]

        return A


result = random_sampling(4, list1)

print(result)