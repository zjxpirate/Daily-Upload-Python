




from Binary_Trees_node import BinaryTreeNode


def inorder_traversal(tree):
    s, result = [], []

    while s or tree:


        if tree:
            s.append(tree)

            # Going left.
            tree = tree.left
            #print("tree: ", tree)
            #print("s: ", s)

        else:
            #print(tree)
            # Going up.
            tree = s.pop()
            #print(tree)
            result.append(tree.data)
            # Going right.
            tree = tree.right
            #print(tree)
            #print("s: ", s)

    return result



b = BinaryTreeNode(314, BinaryTreeNode(6 , BinaryTreeNode(271, BinaryTreeNode(28), BinaryTreeNode(0)), BinaryTreeNode(561, BinaryTreeNode(None), BinaryTreeNode(3, BinaryTreeNode(17)))), BinaryTreeNode(6, BinaryTreeNode(2, BinaryTreeNode(None), BinaryTreeNode(1, BinaryTreeNode(401, BinaryTreeNode(None), BinaryTreeNode(641)), BinaryTreeNode(257))), BinaryTreeNode(271, BinaryTreeNode(None), BinaryTreeNode(28))))
#b = BinaryTreeNode(1, BinaryTreeNode(2, BinaryTreeNode(4), BinaryTreeNode(5)), BinaryTreeNode(3, BinaryTreeNode(6), BinaryTreeNode(7)))


print(inorder_traversal(b))







