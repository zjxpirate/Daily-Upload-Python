
import random



def random_subset(n, k):
    changed_elements = {}

    for i in range(k):
        # Generate a random index between i and n-1, inclusive.
        rand_idx = random.randrange(i, n)
        rand_idx_mapped = changed_elements.get(rand_idx, rand_idx)
        i_mapped = changed_elements.get(i, i)
        changed_elements[rand_idx] = i_mapped
        changed_elements[i] = rand_idx_mapped

    return [changed_elements[i] for i in range(k)]


result = random_subset(100, 7)

print(result)

