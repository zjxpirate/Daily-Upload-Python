
from bstNode import BstNode, insert

tree_1 = BstNode(19, None, None)

insert(7, tree_1)
insert(43, tree_1)
insert(3, tree_1)
insert(11, tree_1)
insert(23, tree_1)
insert(47, tree_1)
insert(2, tree_1)
insert(5, tree_1)
insert(17, tree_1)
insert(37, tree_1)
insert(53, tree_1)
insert(13, tree_1)
insert(29, tree_1)
insert(41, tree_1)
insert(31, tree_1)

s = BstNode(3, None, None)
b = BstNode(17, None, None)

# 7. compute the LCA in a bst

# input nodes are nonempty and the key at s is less than or equal to that at b.
def find_LCA(tree, s, b):
    while tree.data < s.data or tree.data > b.data:
        #keep searching since tree is outside of [s, b].
        while tree.data < s.data:
            tree = tree.right # LCA must be in tree's right child.
        while tree.data > b.data:
            tree = tree.left # LCA must be in tree's left child.

    # now, s.data <= tree.data && tree.data <= b.data
    return tree

print(find_LCA(tree_1, s, b))





















