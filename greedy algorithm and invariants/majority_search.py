

# 7. find the majority element
list1 = ['b', 'a', 'c', 'a', 'a', 'b', 'a', 'a', 'c', 'a']

def majority_search(stream):

    candidate, candidate_count = None, 0

    for it in stream:
        if candidate_count == 0:
            candidate, candidate_count = it, candidate_count + 1
        elif candidate == it:
            candidate_count += 1
        else:
            candidate_count -= 1

    return candidate


print(majority_search(list1))




