

# 7. making wired connections

import collections

class GraphVertex:
    def __init__(self):
        self.d = -1
        self.edges = []


def is_any_placement_feasible(graph):
    def bfs(s):
        s.d = 0
        q = collections.deque([s])

        while q:
            for t in q[0].edges:
                if t.d == -1:   # unvisited vertex.
                    t.d = q[0].d + 1
                    q.append(t)
                elif t.d == q[0].d:
                    return False
            del q[0]

        return True

    return all(bfs(v) for v in graph if v.d == -1)







