



from Binary_Trees_node import BinaryTreeNode



def exterior_binary_tree(tree):

    def is_leaf(node):
        return not node.left and not node.right

    # Computes the nodes from the root to the leftmost leaf followed by all the leaves in subtree.
    def left_boundary_and_leaves(subtree, is_boundary):
        if not subtree:
            return []
        return (([subtree] if is_boundary or is_leaf(subtree) else []) + left_boundary_and_leaves(subtree.left, is_boundary) + left_boundary_and_leaves(subtree.right, is_boundary and not subtree.left))

    # Computes the leaves in left-to-right order followed by the rightmost leaf to the root path in subtree.
    def right_boundary_and_leaves(subtree, is_boundary):
        if not subtree:
            return []
        return (right_boundary_and_leaves(subtree.left, is_boundary and not subtree.right) + right_boundary_and_leaves(subtree.right, is_boundary) + ([subtree] if is_boundary or is_leaf(subtree) else []))


    return ([tree] + left_boundary_and_leaves(tree.left, is_boundary=True) + right_boundary_and_leaves(tree.right, is_boundary=True) if tree else [])









b = BinaryTreeNode(314, BinaryTreeNode(6 , BinaryTreeNode(271, BinaryTreeNode(28), BinaryTreeNode(0)), BinaryTreeNode(561, BinaryTreeNode(None), BinaryTreeNode(3, BinaryTreeNode(17)))), BinaryTreeNode(6, BinaryTreeNode(2, BinaryTreeNode(None), BinaryTreeNode(1, BinaryTreeNode(401, BinaryTreeNode(None), BinaryTreeNode(641)), BinaryTreeNode(257))), BinaryTreeNode(271, BinaryTreeNode(None), BinaryTreeNode(28))))


print(exterior_binary_tree(b))


