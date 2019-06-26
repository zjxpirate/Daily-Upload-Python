

# 8. transform one string to another

import collections, string

D = ["bat", "cot", "dog", "dag", "dot", "cat"]
s = "cat"
t = "dog"

# uses bfs to find the least steps of transformation.
def transform_string(D, s, t):

    StringWithDistance = collections.namedtuple('StringWithDistance', ('candidate_string', 'distance'))
    q = collections.deque([StringWithDistance(s, 0)])
    D.remove(s)   # marks s as visited by erasing it in D.

    while q:
        f = q.popleft()
        # returns if we find a match.
        if f.candidate_string == t:
            return f.distance   # number of steps reaches t.

        # tries all possible transformations of f.candidate_string.
        for i in range(len(f.candidate_string)):
            for c in string.ascii_lowercase:   # iterates through 'a' ~ 'z'.
                cand = f.candidate_string[:i] + c + f.candidate_string[i + 1:]
                if cand in D:
                    D.remove(cand)
                    q.append(StringWithDistance(cand, f.distance + 1))

    return -1   # cannot find a possible transformation.


print(transform_string(D, s, t))







