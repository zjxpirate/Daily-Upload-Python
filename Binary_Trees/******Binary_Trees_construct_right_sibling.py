


import functools



class BinaryTreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.next = None   # Populates this field.



def construct_right_sibling(tree):
    def populate_children_next_field(start_node):
        while start_node and start_node.left:

            # Populate left child's next field.
            start_node.left.next = start_node.right

            # Populate right child's next field if start_node is not the last node of level.
            start_node.right.next = start_node.next and start_node.next.left
            start_node = start_node.next



    while tree and tree.left:
        populate_children_next_field(tree)
        tree = tree.left










b = BinaryTreeNode(314, BinaryTreeNode(6 , BinaryTreeNode(271, BinaryTreeNode(28), BinaryTreeNode(0)), BinaryTreeNode(561, BinaryTreeNode(None), BinaryTreeNode(3, BinaryTreeNode(17)))), BinaryTreeNode(6, BinaryTreeNode(2, BinaryTreeNode(None), BinaryTreeNode(1, BinaryTreeNode(401, BinaryTreeNode(None), BinaryTreeNode(641)), BinaryTreeNode(257))), BinaryTreeNode(271, BinaryTreeNode(None), BinaryTreeNode(28))))




