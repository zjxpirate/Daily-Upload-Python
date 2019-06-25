

# 6. clone a graph

import collections

class GraphVertex:
    def __init__(self, label):
        self.label = label
        self.edge = []


def clone_graph(graph):
    if not graph:
        return None

    q = collections.deque([graph])
    vertex_map = {graph: GraphVertex(graph.label)}

    while q:
        v = q.popleft()
        for e in v.edges:
            # try to copy vertex e.
            if e not in vertex_map:
                vertex_map[e] = GraphVertex(e.label)
                q.append(e)
            # copy edge v->e.
            vertex_map[v].edges.append(vertex_map[e])

    return vertex_map[graph]


print(clone_graph(graph))


