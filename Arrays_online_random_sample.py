
import itertools, random

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]



# Assumption: there are at least k elements in the stream.

def online_random_sample(stream, k):

    # Store the first k elements
    sampling_results = list(itertools.islice(stream, k))

    # Have read the first k elements.
    num_seen_so_far = k
    for x in stream:
        num_seen_so_far += 1

        # Generate a random number in [0, num_seen_so_far - 1], and if this
        # number is in [0, k - 1], we replace that element from the sample with x.
        idx_to_replace = random.randrange(num_seen_so_far)
        if idx_to_replace < k:
            sampling_results[idx_to_replace] = x

    return sampling_results


result = online_random_sample(list1, 5)

print(result)


