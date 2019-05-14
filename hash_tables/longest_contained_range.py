

# 13. find the length of a longest contained interval

list1 = [10, 5, 3, 11, 6, 100, 4]

def longest_contained_range(A):
    # unprocessed_entries records the existence of each entry in A.
    unprocessed_entries = set(A)
    print(unprocessed_entries)

    max_interval_size = 0
    while unprocessed_entries:
        a = unprocessed_entries.pop()
        print(a)

        # finds the lower bound of the largest range containing a
        lower_bound = a - 1
        while lower_bound in unprocessed_entries:
            unprocessed_entries.remove(lower_bound)
            lower_bound -= 1


        # finds the upper bound of the largest range containing a
        upper_bound = a + 1
        while upper_bound in unprocessed_entries:
            unprocessed_entries.remove(upper_bound)
            upper_bound += 1


        max_interval_size = max(max_interval_size, upper_bound - lower_bound - 1)


    return max_interval_size


print(longest_contained_range(list1))





