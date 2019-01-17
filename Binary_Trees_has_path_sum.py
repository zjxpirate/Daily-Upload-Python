


from Binary_Trees_node import BinaryTreeNode



def has_path_sum(tree, remaining_weight):
    if not tree:
        return False
    if not tree.left and not tree.right:   # Leaf.
        return remaining_weight == tree.data

    # Non-leaf
    return (has_path_sum(tree.left, remaining_weight - tree.data) or has_path_sum(tree.right, remaining_weight - tree.data))



b = BinaryTreeNode(1, BinaryTreeNode(2, BinaryTreeNode(4), BinaryTreeNode(5)), BinaryTreeNode(3, BinaryTreeNode(6), BinaryTreeNode(7)))


print(has_path_sum(b, 7))




