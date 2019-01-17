




from Binary_Trees_utils import binary_tree_to_string, equal_binary_trees



class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None, size=None):
        self.data = data
        self.left = left
        self.right = right
        self.size = size




    def __eq__(self, other):
        return equal_binary_trees(self, other)

    def __repr__(self):
        return str(binary_tree_to_string(self))

    def __str__(self):
        return self.__repr__()








b = BinaryTreeNode(1, BinaryTreeNode(2, BinaryTreeNode(5)), BinaryTreeNode(3))



#print(b)



#print(b.left.right)
#print(b.right)