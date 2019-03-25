

#b = BinaryTreeNode(314, BinaryTreeNode(6 , BinaryTreeNode(271, BinaryTreeNode(28), BinaryTreeNode(0)), BinaryTreeNode(561, BinaryTreeNode(None), BinaryTreeNode(3, BinaryTreeNode(17)))), BinaryTreeNode(6, BinaryTreeNode(2, BinaryTreeNode(None), BinaryTreeNode(1, BinaryTreeNode(401, BinaryTreeNode(None), BinaryTreeNode(641)), BinaryTreeNode(257))), BinaryTreeNode(271, BinaryTreeNode(None), BinaryTreeNode(28))))
#b = BinaryTreeNode(1, BinaryTreeNode(2, BinaryTreeNode(4), BinaryTreeNode(5)), BinaryTreeNode(3, BinaryTreeNode(6), BinaryTreeNode(7)))


from Binary_Trees_node import BinaryTreeNode



def inorder_traversal(tree):
    prev, result = None, []
    while tree:
        if prev is tree.parent:
            # we came down to tree from prev.
            if tree.left:  # Keep going left.
                next = tree.left
            else:
                result.append(tree.data)
                # Done with left, so go right if right is not empty. Otherwise, go up.
                next = tree.right or tree.parent

        elif tree.left is prev:
            # We came up to tree from its left child.
            result.append(tree.data)
            # Done with left, so go right if right is not empty. Otherwise, go up.
            next = tree.right or tree.parent

        else:   # Done with both children, so move up.
            next = tree.parent


        prev, tree = tree, next


    return result










