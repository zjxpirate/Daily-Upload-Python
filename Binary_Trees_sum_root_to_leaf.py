


from Binary_Trees_node import BinaryTreeNode


def sum_root_to_leaf(tree, partial_path_sum = 0):

    if not tree:
        return 0

    partial_path_sum = partial_path_sum * 2 + tree.data

    if not tree.left and not tree.right:  #leaf
        return partial_path_sum

    # Non-leaf.
    return (sum_root_to_leaf(tree.left, partial_path_sum) + sum_root_to_leaf(tree.right, partial_path_sum))




b = BinaryTreeNode(1, BinaryTreeNode(0, BinaryTreeNode(0), BinaryTreeNode(1)), BinaryTreeNode(1, BinaryTreeNode(0), BinaryTreeNode(1)))

print(sum_root_to_leaf(b))
