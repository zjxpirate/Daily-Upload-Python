

class BstNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right

    def __repr__(self):
        if self.right is not None:
            fmt = '{}({data!r}, {left!r}, {right!r})'
        elif self.left is not None:
            fmt = '{}({data!r}, {left!r})'
        else:
            fmt = '{}({data!r})'
        return fmt.format(type(self).__name__, **vars(self))

def insert(item, tree):
    if (item < tree.data):
        if (tree.left != None):
            insert(item, tree.left)
        else:
            tree.left = BstNode(item)
    else:
        if (tree.right != None):
            insert(item, tree.right)
        else:
            tree.right = BstNode(item)

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




# 4. test if the binary tree satisfy the bst property

def is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):
    if not tree:
        return True
    elif not low_range <= tree.data <= high_range:
        return False
    return (is_binary_tree_bst(tree.left, low_range, tree.data) and is_binary_tree_bst(tree.right, tree.data, high_range))

print(is_binary_tree_bst(tree_1))













