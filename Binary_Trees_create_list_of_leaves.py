



from Binary_Trees_node import BinaryTreeNode


def create_list_of_leaves(tree):
    if not tree:
        return []
    if not tree.left and not tree.right:
        return [tree]

    # First do the left subtree, and then do the right subtree.

    return create_list_of_leaves(tree.left) + create_list_of_leaves(tree.right)



b = BinaryTreeNode(314, BinaryTreeNode(6 , BinaryTreeNode(271, BinaryTreeNode(28), BinaryTreeNode(0)), BinaryTreeNode(561, BinaryTreeNode(None), BinaryTreeNode(3, BinaryTreeNode(17)))), BinaryTreeNode(6, BinaryTreeNode(2, BinaryTreeNode(None), BinaryTreeNode(1, BinaryTreeNode(401, BinaryTreeNode(None), BinaryTreeNode(641)), BinaryTreeNode(257))), BinaryTreeNode(271, BinaryTreeNode(None), BinaryTreeNode(28))))


print(create_list_of_leaves(b))


