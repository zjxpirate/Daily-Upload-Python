

# 5. deadlock detection

class GraphVertex:

    WHITE, GRAY, BLACK = range(3)

    def __init__(self):
        self.color = GraphVertex.WHITE
        self.edges = []


edges = [[0, 1], [1, 2], [2, 0]]
num_nodes = 3
graph = [GraphVertex() for _ in range(num_nodes)]

for (fr, to) in edges:
        if fr < 0 or fr >= num_nodes or to < 0 or to >= num_nodes:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])


def is_deadlocked(graph):
    def has_cycle(cur):
        # visiting a gray vertex means a cycle.
        if cur.color == GraphVertex.GRAY:
            return True

        cur.color = GraphVertex.GRAY   # marks current vertex as a gray one.
        # traverse the neighbor vertices.
        if any(next.color != GraphVertex.BLACK and has_cycle(next) for next in cur.edges):
            return True

        cur.color = GraphVertex.BLACK   # marks current vertex as black.
        return False

    return any(vertex.color == GraphVertex.WHITE and has_cycle(vertex) for vertex in graph)


print(is_deadlocked(graph))




