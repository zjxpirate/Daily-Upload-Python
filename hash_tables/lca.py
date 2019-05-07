



# 7. compute the LCA, optimizing for close ancestors

def lca(node0, node1):
    iter0, iter1 = node0, node1
    nodes_on_path_to_root = set()

    while iter0 or iter1:
        # ascend tree in tandem for these two nodes.
        if iter0:
            if iter0 in nodes_on_path_to_root:
                return iter0
            nodes_on_path_to_root.add(iter0)
            iter0 = iter0.parent

        if iter1:
            if iter1 in nodes_on_path_to_root:
                return iter1
            nodes_on_path_to_root.add(iter1)
            iter1 = iter1.parent

    raise ValueError('node0 and node1 are not in the same tree')

