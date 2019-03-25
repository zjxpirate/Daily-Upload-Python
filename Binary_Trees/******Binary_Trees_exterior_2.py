


import functools
from Binary_Trees_node import BinaryTreeNode




def exterior_binary_tree(tree):

    # Computes the nodes from the root to the leftmost leaf.
    def left_boundary(subtree):
        if not subtree or (not subtree.left and not subtree.right):
            return
        exterior.append(subtree)
        if subtree.left:
            left_boundary(subtree.left)
        else:
            left_boundary(subtree.right)

    # Computes the nodes from the rightmost leaf to the root.
    def right_boundary(subtree):
        if not subtree or (not subtree.left and not subtree.right):
            return
        if subtree.right:
            right_boundary(subtree.right)
        else:
            right_boundary(subtree.left)
        exterior.append(subtree)

    # Compute the leaves in left-to-right order.
    def leaves(subtree):
        if not subtree:
            return
        if not subtree.left and not subtree.right:
            exterior.append(subtree)
            return
        leaves(subtree.left)
        leaves(subtree.right)

    if not tree:
        return []

    exterior = [tree]
    left_boundary(tree.left)
    leaves(tree.left)
    leaves(tree.right)
    right_boundary(tree.right)
    return exterior










b = BinaryTreeNode(314, BinaryTreeNode(6 , BinaryTreeNode(271, BinaryTreeNode(28), BinaryTreeNode(0)), BinaryTreeNode(561, BinaryTreeNode(None), BinaryTreeNode(3, BinaryTreeNode(17)))), BinaryTreeNode(6, BinaryTreeNode(2, BinaryTreeNode(None), BinaryTreeNode(1, BinaryTreeNode(401, BinaryTreeNode(None), BinaryTreeNode(641)), BinaryTreeNode(257))), BinaryTreeNode(271, BinaryTreeNode(None), BinaryTreeNode(28))))


print(exterior_binary_tree(b))


