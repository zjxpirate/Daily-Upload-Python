






def binary_tree_depth_order(tree):
    result = []
    if not tree:
        return result


    curr_depth_nodes = [tree]

    while curr_depth_nodes:
        result.append([curr.data for curr in curr_depth_nodes])
        curr_depth_nodes = [
            child for curr in curr_depth_nodes for child in (curr.left, curr.right) if child
        ]

    return result




