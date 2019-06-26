

# 9. team photo day - 2

class GraphVertex:
    def __init__(self):
        self.edges = []
        # set max_distance = 0 to indicate unvisited vertex.
        self.max_distance = 0

edges = [[2, 7], [3, 6], [3, 4], [1, 5]]

k = 20

graph = [GraphVertex() for _ in range(k)]

for (fr, to) in edges:
    if fr < 0 or fr >= k or to < 0 or to >= k:
        raise RuntimeError('Invalid vertex index')
    graph[fr].edges.append(graph[to])


def find_largest_number_teams(graph):
    def dfs(curr):
        curr.max_distance = max(((vertex.max_distance if vertex.max_distance != 0 else dfs(vertex)) + 1 for vertex in curr.edges), default = 1)
        return curr.max_distance

    return max(dfs(g) for g in graph if g.max_distance == 0)


print(find_largest_number_teams(graph))






