

from Binary_Trees_node import BinaryTreeNode


def tree_traversal(root):
    if root:
        print('Preorder: %d' % root.data)
        tree_traversal(root.left)

        print("\n")

        print('Inorder: %d' % root.data)
        tree_traversal(root.right)

        print("\n")

        print('Postorder: %d' % root.data)



b = BinaryTreeNode(1, BinaryTreeNode(2, BinaryTreeNode(4), BinaryTreeNode(5)), BinaryTreeNode(3, BinaryTreeNode(6), BinaryTreeNode(7)))


print(tree_traversal(b))
